import subprocess

linux = input("whish linux you use?(debian-based, arch-based, fedora-based): ")
if linux == "debian-based":
    subprocess.run(["sudo", "apt", "install", "mpv", "speedtest-cli", "ntfs-3g", "e2fsprogs", "dosfstools", "ffmpeg", "yt-dlp", "coreutils"])
elif linux == "arch-based":
    subprocess.run(["sudo", "pacman", "-S", "mpv", "speedtest-cli", "ntfs-3g", "e2fsprogs", "dosfstools", "ffmpeg", "yt-dlp", "coreutils"])
elif linux == "fedora-based":
    subprocess.run(["sudo", "dnf", "install", "mpv", "speedtest-cli", "ntfs-3g", "e2fsprogs", "dosfstools", "ffmpeg", "yt-dlp", "coreutils"])
else:
    print("Unsupported Linux distribution type.")

print("All tools have been installed.")
print("Organizing files...")
subprocess.run(["mkdir", "-p", "~/bin"])
subprocess.run(["mv", "AllTools.py", "~/bin/alltool"])
subprocess.run(["chmod", "+x", "~/bin/alltool"])
subprocess.run(["echo", 'export PATH="$HOME/bin:$PATH"', ">>", "~/.bashrc"])
print("All done! you can remove AllToolInstaller.py now!")