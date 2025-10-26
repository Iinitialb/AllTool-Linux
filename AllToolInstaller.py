#!/usr/bin/env python3
import subprocess
import os
import sys
import shutil

# ---------------- Installer Deletion ----------------
def delete_installer():
    while True:
        choice = input("Do you want to delete this installer? (y/N): ").strip().lower()
        if choice in ("y", "yes", ""):
            try:
                os.remove(os.path.abspath(__file__))
                print("✅ Installer deleted.")
            except Exception as e:
                print(f"❌ Could not delete installer: {e}")
            break
        elif choice in ("n", "no"):
            print("ℹ️ Installer retained.")
            break
        else:
            print("❌ Invalid choice. Please type 'y' or 'n'.")

# --------------------- Updating Terminal --------------------
def update_terminal():
    terminal = os.environ.get("SHELL", "unknown").split("/")[-1]
    print(f"Current terminal: {terminal}")
    if terminal == "bash":
        config_file = "~/.bashrc"
    elif terminal == "zsh":
        config_file = "~/.zshrc"
    elif terminal == "fish":
        config_file = "~/.config/fish/config.fish"
    else:
        config_file = "~/.bashrc"  # fallback
    subprocess.run(["source", config_file], shell=True)

# ---------------- Command Runner ----------------
def run_command(cmd, description, show_output=True):
    """Run a system command with optional output display."""
    print(f"🔧 {description}...")
    try:
        if show_output:
            result = subprocess.run(cmd, check=True)
        else:
            result = subprocess.run(cmd, check=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
        print(f"✅ {description} completed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ {description} failed: {e}")
        return False

# ---------------- System Packages Installation ----------------
def install_system_packages(distribution):
    packages = {
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

    if distribution not in packages:
        print(f"❌ Unsupported distribution: {distribution}")
        return False

    package_list = packages[distribution]
    total_packages = len(package_list)

    print(f"📦 Installing {total_packages} system packages for {distribution}...")

    for i, pkg in enumerate(package_list, start=1):
        if distribution == "debian-based":
            cmd = ["sudo", "apt", "install", "-y", pkg]
        elif distribution == "arch-based":
            cmd = ["sudo", "pacman", "-S", "--noconfirm", pkg]
        elif distribution == "fedora-based":
            cmd = ["sudo", "dnf", "install", "-y", pkg]
        elif distribution == "opensuse-based":
            cmd = ["sudo", "zypper", "install", "-y", pkg]

        run_command(cmd, f"Installing {pkg}", show_output=True)

        # Progress bar
        percent = int((i / total_packages) * 100)
        bar_length = 30
        filled_length = int(bar_length * i // total_packages)
        bar = "█" * filled_length + "-" * (bar_length - filled_length)
        print(f"Progress: |{bar}| {percent}% completed\n")

    return True

# ---------------- Python Packages Installation ----------------
def install_python_packages():
    python_packages = ["requests", "beautifulsoup4"]
    total_packages = len(python_packages)

    for i, package in enumerate(python_packages, start=1):
        print(f"\n🐍 Installing Python package: {package}")
        run_command([sys.executable, "-m", "pip", "install", package], f"Installing {package}")

        percent = int((i / total_packages) * 100)
        bar_length = 30
        filled_length = int(bar_length * i // total_packages)
        bar = "█" * filled_length + "-" * (bar_length - filled_length)
        print(f"Progress: |{bar}| {percent}% completed\n")

    print("\n✅ All Python packages installed!")

# ---------------- AllTools Setup ----------------
def setup_alltool():
    print("🔧 Setting up AllTools...")

    bin_dir = os.path.expanduser("~/bin")
    os.makedirs(bin_dir, exist_ok=True)

    script_path = os.path.join(os.getcwd(), "AllTools.py")
    target_path = os.path.join(bin_dir, "alltool")

    if os.path.exists(script_path):
        shutil.copy(script_path, target_path)
        os.chmod(target_path, 0o755)
        print(f"✅ AllTools.py copied to {target_path}")
    else:
        print("❌ AllTools.py not found in current directory")
        return False

    # ---------------- Update PATH ----------------
    path_line = 'export PATH="$HOME/bin:$PATH"'

    # Update current Python session PATH
    os.environ["PATH"] = os.path.expanduser("~/bin:") + os.environ["PATH"]
    print(f"ℹ️ PATH updated for current session: {os.environ['PATH']}")

    # Update shell config for future sessions
    shell_configs = {
        "bash": "~/.bashrc",
        "zsh": "~/.zshrc",
        "fish": "~/.config/fish/config.fish"
    }
    shell = os.environ.get("SHELL", "").split("/")[-1]
    config_file = os.path.expanduser(shell_configs.get(shell, "~/.bashrc"))

    try:
        if os.path.exists(config_file):
            with open(config_file, "r") as f:
                content = f.read()
            if path_line not in content:
                with open(config_file, "a") as f:
                    f.write(f"\n# Added by alltool installer\n{path_line}\n")
                print(f"✅ PATH added to {config_file} for future sessions")
            else:
                print(f"ℹ️ PATH already exists in {config_file}")
        else:
            with open(config_file, "w") as f:
                f.write(f"# Shell config created by alltool installer\n{path_line}\n")
            print(f"✅ Created {config_file} with PATH configuration")
    except Exception as e:
        print(f"❌ Error updating PATH in {config_file}: {e}")

    print("⚠️ Note: For full effect in this shell, you may need to run:")
    print(f"       source {config_file}  # or restart your terminal")

    return True

# ---------------- Distribution Detection ----------------
def detect_distribution():
    print("🔍 Detecting your Linux distribution...")
    if os.path.exists("/etc/os-release"):
        with open("/etc/os-release") as f:
            content = f.read().lower()
        if any(x in content for x in ["ubuntu", "debian", "linuxmint", "elementary", "pop", "kali", "parrot"]):
            return "debian-based"
        if any(x in content for x in ["arch", "manjaro", "endeavour", "garuda", "artix"]):
            return "arch-based"
        if any(x in content for x in ["fedora", "centos", "rhel", "rocky", "alma", "amazon"]):
            return "fedora-based"
        if any(x in content for x in ["opensuse", "suse", "sled", "sles"]):
            return "opensuse-based"
    return None

# ---------------- Main Installer ----------------
def main():
    print("🚀 AllTool Installer - Installing all dependencies for AllTools.py")
    print("=" * 60)

    distribution = detect_distribution()
    if distribution:
        print(f"✅ Detected distribution: {distribution}")
        confirm = input(f"Proceed with {distribution} installation? (y/N): ").strip().lower()
        if confirm not in ['y', 'yes']:
            print("❌ Installation cancelled.")
            return
    else:
        print("❌ Could not automatically detect your distribution.")
        choice = input("Choose your distribution (1: debian, 2: arch, 3: fedora, 4: opensuse): ").strip()
        distribution_map = {"1": "debian-based", "2": "arch-based", "3": "fedora-based", "4": "opensuse-based"}
        distribution = distribution_map.get(choice)
        if not distribution:
            print("❌ Invalid choice.")
            return

    install_system_packages(distribution)
    install_python_packages()
    setup_alltool()

    print("\n" + "=" * 60)
    print("✅ Installation completed successfully!")
    delete_installer()

if __name__ == "__main__":
    main()