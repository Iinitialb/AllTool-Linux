#!/usr/bin/env python3
import os
import sys
import subprocess
import shutil
import time

# ---------------- Utility Functions ----------------
def run_command(cmd, description="", show_output=True):
    """Run shell command with optional progress and output"""
    try:
        if description:
            print(f"🔧 {description}...")
        if show_output:
            subprocess.run(cmd, check=True)
        else:
            subprocess.run(cmd, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    except subprocess.CalledProcessError as e:
        print(f"❌ Error running: {' '.join(cmd)}\n{e}")

def progress_bar(task, duration=2):
    """Show a simple progress bar"""
    print(f"{task}: ", end="")
    for _ in range(20):
        time.sleep(duration / 20)
        print("█", end="", flush=True)
    print(" ✅")

# ---------------- Detect Distribution ----------------
def detect_distribution():
    try:
        with open("/etc/os-release") as f:
            os_info = f.read().lower()
        if "debian" in os_info or "ubuntu" in os_info:
            return "debian-based"
        elif "arch" in os_info:
            return "arch-based"
        elif "fedora" in os_info:
            return "fedora-based"
        elif "suse" in os_info:
            return "opensuse-based"
    except FileNotFoundError:
        pass
    return None

# ---------------- System Packages Installation ----------------
def install_system_packages(distribution, selected_packages=None):
    if not distribution:
        print("⚠️  Unknown distribution, skipping system packages.")
        return

    print(f"📦 Installing system packages for {distribution}...")

    all_packages = {
        "debian-based": [
            "mpv", "speedtest-cli", "ntfs-3g", "e2fsprogs", "dosfstools",
            "ffmpeg", "yt-dlp", "coreutils", "inxi", "power-profiles-daemon",
            "nodejs", "npm", "ruby", "php", "openjdk-11-jdk", "g++",
            "python3-pip", "python3-requests", "python3-bs4"
        ],
        "arch-based": [
            "mpv", "speedtest-cli", "ntfs-3g", "e2fsprogs", "dosfstools",
            "ffmpeg", "yt-dlp", "coreutils", "inxi", "power-profiles-daemon",
            "nodejs", "npm", "ruby", "php", "jdk-openjdk", "gcc",
            "python-pip", "python-requests", "python-beautifulsoup4"
        ],
        "fedora-based": [
            "mpv", "speedtest-cli", "ntfs-3g", "e2fsprogs", "dosfstools",
            "ffmpeg", "yt-dlp", "coreutils", "inxi", "power-profiles-daemon",
            "nodejs", "npm", "ruby", "php", "java-11-openjdk-devel", "gcc-c++",
            "python3-pip", "python3-requests", "python3-beautifulsoup4"
        ],
        "opensuse-based": [
            "mpv", "speedtest-cli", "ntfs-3g", "e2fsprogs", "dosfstools",
            "ffmpeg", "yt-dlp", "coreutils", "inxi", "power-profiles-daemon",
            "nodejs", "npm", "ruby", "php", "java-11-openjdk-devel", "gcc-c++",
            "python3-pip", "python3-requests", "python3-beautifulsoup4"
        ]
    }

    packages = selected_packages if selected_packages else all_packages[distribution]

    if distribution == "debian-based":
        install_cmd = ["sudo", "apt", "install", "-y"]
    elif distribution == "arch-based":
        install_cmd = ["sudo", "pacman", "-S", "--noconfirm"]
    elif distribution == "fedora-based":
        install_cmd = ["sudo", "dnf", "install", "-y"]
    else:
        install_cmd = ["sudo", "zypper", "install", "-y"]

    for pkg in packages:
        print(f"➡️ Installing {pkg}...")
        progress_bar(f"Installing {pkg}", 1)
        run_command(install_cmd + [pkg], f"Installing {pkg}", show_output=False)
        print(f"✅ {pkg} installed.\n")

# ---------------- Python Packages Installation ----------------
def install_python_packages(selected_packages=None):
    print("🐍 Installing Python packages...")
    packages = selected_packages if selected_packages else ["requests", "beautifulsoup4"]
    for pkg in packages:
        print(f"➡️ Installing {pkg} via pip...")
        progress_bar(f"Installing {pkg}", 1)
        run_command([sys.executable, "-m", "pip", "install", pkg], f"Installing {pkg}", show_output=False)
        print(f"✅ {pkg} installed.\n")

# ---------------- Setup AllTool ----------------
def setup_alltool():
    """Setup AllTool in the system"""
    print("🔧 Setting up AllTool...")

    installer_dir = os.path.dirname(os.path.abspath(__file__))
    script_path = os.path.join(installer_dir, "AllTools.py")

    # Create bin directory
    bin_dir = os.path.expanduser("~/bin")
    os.makedirs(bin_dir, exist_ok=True)

    # Copy script to bin directory
    target_path = os.path.join(bin_dir, "alltool")

    if not os.path.exists(script_path):
        print("❌ AllTools.py not found in installer directory.")
        return False

    if os.path.abspath(script_path) == os.path.abspath(target_path):
        print(f"ℹ️ Source and destination are the same ({script_path}). Skipping copy.")
    else:
        try:
            shutil.copy(script_path, target_path)
            os.chmod(target_path, 0o755)
            print(f"✅ AllTools.py copied to {target_path}")
        except Exception as e:
            print(f"❌ Failed to copy AllTools.py: {e}")
            return False

    # Update PATH temporarily
    os.environ["PATH"] = os.path.expanduser("~/bin:") + os.environ["PATH"]
    print("✅ PATH temporarily updated.")
    print("💡 Run 'source ~/.bashrc' or 'source ~/.zshrc' to make it permanent.")
    return True

# ---------------- Delete Installer ----------------
def delete_installer():
    while True:
        choice = input("🧹 Do you want to delete this installer after setup? (y/N): ").strip().lower()
        if choice in ["y", "yes"]:
            try:
                os.remove(os.path.abspath(__file__))
                print("🗑️ Installer deleted successfully.")
            except Exception as e:
                print(f"❌ Failed to delete installer: {e}")
            break
        elif choice in ["n", "no", ""]:
            print("Installer retained.")
            break
        else:
            print("❌ Invalid input. Please type 'y' or 'n'.")

# ---------------- Main Installer ----------------
def main():
    print("🚀 AllTool Installer")
    print("=" * 60)

    # Installation mode loop
    while True:
        choice = input("Choose installation mode: 1) Install all  2) Manual selection: ").strip()
        if choice in ['1', '2']:
            break
        print("❌ Invalid choice. Please enter 1 or 2.")

    # Detect distribution
    distribution = detect_distribution()
    if distribution:
        print(f"✅ Detected distribution: {distribution}")
        while True:
            confirm = input(f"Proceed with {distribution} installation? (y/N): ").strip().lower()
            if confirm in ['y', 'yes', 'n', 'no', '']:
                if confirm not in ['y', 'yes']:
                    print("❌ Installation cancelled.")
                    return
                break
            print("❌ Invalid input. Please type 'y' or 'n'.")
    else:
        print("❌ Could not detect distribution automatically.")
        dist_map = {"1": "debian-based", "2": "arch-based", "3": "fedora-based", "4": "opensuse-based"}
        while True:
            dist_choice = input("Choose your distribution (1: debian, 2: arch, 3: fedora, 4: opensuse): ").strip()
            distribution = dist_map.get(dist_choice)
            if distribution:
                break
            print("❌ Invalid distribution choice. Please enter 1, 2, 3, or 4.")

    # Manual selection mode
    system_packages = None
    python_packages = None
    if choice == '2':
        # Full package list display
        all_system_packages = {
            "debian-based": [
                "mpv", "speedtest-cli", "ntfs-3g", "e2fsprogs", "dosfstools",
                "ffmpeg", "yt-dlp", "coreutils", "inxi", "power-profiles-daemon",
                "nodejs", "npm", "ruby", "php", "openjdk-11-jdk", "g++",
                "python3-pip", "python3-requests", "python3-bs4"
            ],
            "arch-based": [
                "mpv", "speedtest-cli", "ntfs-3g", "e2fsprogs", "dosfstools",
                "ffmpeg", "yt-dlp", "coreutils", "inxi", "power-profiles-daemon",
                "nodejs", "npm", "ruby", "php", "jdk-openjdk", "gcc",
                "python-pip", "python-requests", "python-beautifulsoup4"
            ],
            "fedora-based": [
                "mpv", "speedtest-cli", "ntfs-3g", "e2fsprogs", "dosfstools",
                "ffmpeg", "yt-dlp", "coreutils", "inxi", "power-profiles-daemon",
                "nodejs", "npm", "ruby", "php", "java-11-openjdk-devel", "gcc-c++",
                "python3-pip", "python3-requests", "python3-beautifulsoup4"
            ],
            "opensuse-based": [
                "mpv", "speedtest-cli", "ntfs-3g", "e2fsprogs", "dosfstools",
                "ffmpeg", "yt-dlp", "coreutils", "inxi", "power-profiles-daemon",
                "nodejs", "npm", "ruby", "php", "java-11-openjdk-devel", "gcc-c++",
                "python3-pip", "python3-requests", "python3-beautifulsoup4"
            ]
        }.get(distribution, [])

        # Show system packages
        print("\n📦 Available system packages:")
        for i, pkg in enumerate(all_system_packages, start=1):
            print(f"{i}) {pkg}")

        while True:
            selection = input("\nEnter numbers of system packages to install (comma separated): ").strip()
            try:
                indices = [int(x) - 1 for x in selection.split(",") if x.isdigit()]
                system_packages = [all_system_packages[i] for i in indices if 0 <= i < len(all_system_packages)]
                if system_packages:
                    print(f"✅ Selected packages: {', '.join(system_packages)}")
                    break
                print("❌ No valid packages selected.")
            except Exception:
                print("❌ Invalid input. Please enter valid numbers separated by commas.")

        # Show Python packages
        python_pkg_list = ["requests", "beautifulsoup4"]
        print("\n🐍 Available Python packages:")
        for i, pkg in enumerate(python_pkg_list, start=1):
            print(f"{i}) {pkg}")

        while True:
            selection_py = input("\nEnter numbers of Python packages to install (comma separated): ").strip()
            try:
                indices_py = [int(x) - 1 for x in selection_py.split(",") if x.isdigit()]
                python_packages = [python_pkg_list[i] for i in indices_py if 0 <= i < len(python_pkg_list)]
                if python_packages:
                    print(f"✅ Selected Python packages: {', '.join(python_packages)}")
                    break
                print("❌ No valid Python packages selected.")
            except Exception:
                print("❌ Invalid input. Please enter valid numbers separated by commas.")

    # Run installations
    install_system_packages(distribution, selected_packages=system_packages)
    install_python_packages(selected_packages=python_packages)

    setup_alltool()
    print("\n✅ Installation process finished!")
    print("💡 Run: source ~/.bashrc (or ~/.zshrc) to update your PATH.")
    delete_installer()

if __name__ == "__main__":
    main()
