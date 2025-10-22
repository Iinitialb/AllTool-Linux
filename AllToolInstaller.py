#!/usr/bin/env python3
import subprocess
import os
import sys


def install_system_packages(distribution):
    """Install system packages based on distribution"""
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
    
    package_lists = {
        "debian-based": "apt",
        "arch-based": "pacman",
        "fedora-based": "dnf",
        "opensuse-based": "zypper"
    }
    
    if distribution not in packages:
        print(f"❌ Unsupported distribution: {distribution}")
        return False
    
    package_manager = package_lists[distribution]
    package_list = packages[distribution]
    
    if distribution == "debian-based":
        cmd = ["sudo", "apt", "update"]
        run_command(cmd, "Updating package lists")
        cmd = ["sudo", "apt", "install", "-y"] + package_list
    elif distribution == "arch-based":
        cmd = ["sudo", "pacman", "-S", "--noconfirm"] + package_list
    elif distribution == "fedora-based":
        cmd = ["sudo", "dnf", "install", "-y"] + package_list
    elif distribution == "opensuse-based":
        cmd = ["sudo", "zypper", "install", "-y"] + package_list
    
    return run_command(cmd, f"Installing system packages for {distribution}")

def install_python_packages():
    """Install Python packages via pip"""
    python_packages = ["requests", "beautifulsoup4"]
    
    for package in python_packages:
        cmd = [sys.executable, "-m", "pip", "install", package]
        run_command(cmd, f"Installing Python package: {package}")

def setup_alltool():
    """Setup alltool in the system"""
    print("🔧 Setting up alltool...")
    
    # Create bin directory
    bin_dir = os.path.expanduser("~/bin")
    os.makedirs(bin_dir, exist_ok=True)
    
    # Copy script to bin directory
    script_path = os.path.join(os.getcwd(), "AllTools.py")
    target_path = os.path.join(bin_dir, "alltool")
    
    if os.path.exists(script_path):
        run_command(["cp", script_path, target_path], "Copying AllTools.py to ~/bin/alltool")
        run_command(["chmod", "+x", target_path], "Making alltool executable")
    else:
        print("❌ AllTools.py not found in current directory")
        return False
    
    # Setup PATH in shell config
    shell_configs = {
        "bash": "~/.bashrc",
        "zsh": "~/.zshrc",
        "fish": "~/.config/fish/config.fish"
    }
    
    shell = os.environ.get("SHELL", "").split("/")[-1]
    config_file = os.path.expanduser(shell_configs.get(shell, "~/.bashrc"))
    
    path_line = 'export PATH="$HOME/bin:$PATH"'
    
    # Check if PATH is already set
    if os.path.exists(config_file):
        with open(config_file, "r") as f:
            content = f.read()
            if path_line in content:
                print(f"ℹ️ PATH already configured in {config_file}")
            else:
                with open(config_file, "a") as f:
                    f.write(f"\n# Added by alltool installer\n{path_line}\n")
                print(f"✅ PATH configured in {config_file}")
    else:
        with open(config_file, "w") as f:
            f.write(f"# Shell configuration\n{path_line}\n")
        print(f"✅ Created {config_file} with PATH configuration")
    
    return True

def detect_distribution():
    """Automatically detect the Linux distribution"""
    print("🔍 Detecting your Linux distribution...")
    
    # Check for /etc/os-release (most modern systems)
    if os.path.exists("/etc/os-release"):
        with open("/etc/os-release", "r") as f:
            content = f.read().lower()
            
        # Debian-based detection
        if any(keyword in content for keyword in ["ubuntu", "debian", "linuxmint", "elementary", "pop", "kali", "parrot"]):
            return "debian-based"
        
        # Arch-based detection
        if any(keyword in content for keyword in ["arch", "manjaro", "endeavour", "garuda", "artix"]):
            return "arch-based"
        
        # Fedora-based detection
        if any(keyword in content for keyword in ["fedora", "centos", "rhel", "rocky", "alma", "amazon"]):
            return "fedora-based"
        
        # openSUSE-based detection
        if any(keyword in content for keyword in ["opensuse", "suse", "sled", "sles"]):
            return "opensuse-based"
    
    # Fallback: Check for package managers
    if run_command(["which", "apt"], "Checking for apt", silent=True):
        return "debian-based"
    elif run_command(["which", "pacman"], "Checking for pacman", silent=True):
        return "arch-based"
    elif run_command(["which", "dnf"], "Checking for dnf", silent=True):
        return "fedora-based"
    elif run_command(["which", "zypper"], "Checking for zypper", silent=True):
        return "opensuse-based"
    
    return None

def run_command(cmd, description, silent=False):
    """Run a command and handle errors gracefully"""
    if not silent:
        print(f"🔧 {description}...")
    try:
        result = subprocess.run(cmd, check=True, capture_output=True, text=True)
        if not silent:
            print(f"✅ {description} completed successfully")
        return True
    except subprocess.CalledProcessError as e:
        if not silent:
            print(f"❌ {description} failed: {e}")
            print(f"Error output: {e.stderr}")
        return False

def main():
    print("🚀 AllTool Installer - Installing all dependencies for AllTools.py")
    print("=" * 60)
    
    # Auto-detect distribution
    distribution = detect_distribution()
    
    if distribution:
        print(f"✅ Detected distribution: {distribution}")
        confirm = input(f"Proceed with {distribution} installation? (y/N): ").strip().lower()
        if confirm not in ['y', 'yes']:
            print("❌ Installation cancelled.")
            return
    else:
        print("❌ Could not automatically detect your distribution.")
        print("\nAvailable distributions:")
        print("1. debian-based (Ubuntu, Debian, Linux Mint, etc.)")
        print("2. arch-based (Arch Linux, Manjaro, EndeavourOS, etc.)")
        print("3. fedora-based (Fedora, CentOS, RHEL, etc.)")
        print("4. opensuse-based (openSUSE, SUSE Linux Enterprise)")
        
        choice = input("\nWhich Linux distribution do you use? (1-4): ").strip()
        
        distribution_map = {
            "1": "debian-based",
            "2": "arch-based", 
            "3": "fedora-based",
            "4": "opensuse-based"
        }
        
        distribution = distribution_map.get(choice)
        if not distribution:
            print("❌ Invalid choice. Please run the installer again.")
            return
    
    print(f"\n📦 Installing packages for {distribution}...")
    
    # Install system packages
    if not install_system_packages(distribution):
        print("❌ Failed to install system packages")
        return
    
    # Install Python packages
    print("\n🐍 Installing Python packages...")
    install_python_packages()
    
    # Setup alltool
    print("\n⚙️ Setting up alltool...")
    if not setup_alltool():
        print("❌ Failed to setup alltool")
        return
    
    print("\n" + "=" * 60)
    print("✅ Installation completed successfully!")
    print("\n📋 Next steps:")
    print("1. Restart your terminal or run: source ~/.bashrc (or ~/.zshrc)")
    print("2. Test the installation: alltool help")
    print("3. Check requirements: alltool requirement")
    print("4. You can now remove AllToolInstaller.py")
    print("\n🎉 Enjoy using alltool!")

if __name__ == "__main__":
    main()