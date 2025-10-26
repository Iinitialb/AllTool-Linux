# 🛠️ AllTool & Installer Scripts - Features Overview

This documentation summarizes the main **features** of the provided Python scripts with added emojis for better readability.

<img width="1035" height="835" alt="Screenshot From 2025-10-26 13-12-19" src="https://github.com/user-attachments/assets/93438892-d83d-4df9-9c08-b29e1a5f42f6" />


---

## 1️⃣ AllTool Script (`AllTool.py`)

A **multi-functional CLI tool** for Linux systems.  

### 🔹 Key Functionalities

- **File & Disk Management**
  - `create <filename>` 📄: Create a file and its folders if needed.
  - `format <disk> <type>` ⚠️: Format disk (supported types: NTFS, EXT4, VFAT).

- **System Refresh**
  - `refresh` 🔄: Refresh script setup, update permissions, and add `~/bin` to PATH.

- **Help & Language Support**
  - `help [lang]` 💡: Show commands and descriptions in **en, fr, ar, de**.

- **Audio/Video Management**
  - `sound <file|playlist.txt>` 🔊: Play audio files or playlists (supports `.mp3`, `.wav`, `.ogg`, `.flac`, `.aac`, `.m4a`).
  - `video <path>` 🎬: Play video files with `ffplay`.
  - `downloadvs <url>` ⬇️: Download video/audio from supported websites using `yt-dlp`.

- **Network & System Info**
  - `netspeed` 🌐: Measure network speed using `speedtest-cli`.
  - `sif` 🖥️: Show detailed system info with `inxi`.
  - `sf` 📂: Show files in current directory.
  - `up` 🔍: Check for system updates.

- **Power Management**
  - `power [subcommand]` 🔋: Manage power profiles and system actions.
    - `pws`: Power-saver mode
    - `pwn`: Balanced mode
    - `pwp`: Performance mode
    - `pwst`: Show current power mode
    - `pwo`: Shutdown
    - `pwr`: Reboot
    - `pwl`: Logout
    - `pwsu`: Suspend
    - `pwh`: Hibernate
    - `pwlo`: Lock screen

- **Script Runner**
  - `run <script>` 🚀: Auto-detect and run Python, Bash, JavaScript, Perl, Ruby, PHP, Java, or C/C++ scripts.

- **Security & Hashes**
  - `psg <length> [options]` 🔐: Generate secure passwords.
  - `hs <file> <hash_type>` 🛡️: Calculate file hash (supports `md5, sha1, sha256, sha512, blake2b, blake2s`).

- **Web & Weather**
  - `sr <topic>` 🔎: Search web using AI-powered methods.
  - `wea <city>` 🌦️: Get weather info for a city.

- **Pomodoro Timer**
  - `pr <sessions>` 🍅: Start a Pomodoro timer with configurable sessions.
  - `pr stop` ⏹️: Stop the running timer.
  - `pr st` 📊: Show Pomodoro status and recent activity.

- **Updater**
  - `upa [st|pv]` ⬆️: Update AllTool to stable (`st`) or preview (`pv`) version.

- **Terminal**
  - `cl` 🧹: Clear the terminal.
  - `un` ❌: Uninstall AllTool.

---

## 2️⃣ Installer Script (`Installer.py`)

A helper script for **installing system packages and self-deletion**.  

### 🔹 Key Functionalities

- **Installer Deletion**
  - Delete installer after installation ✅ or keep it ℹ️.

- **Command Runner**
  - `run_command(cmd, description)` 🔧: Run system commands with progress messages and success/failure notifications.

- **System Packages Installation**
  - Supports major distributions:
    - **Debian/Ubuntu** 🐧: `apt`
    - **Arch Linux** 🌲: `pacman`
    - **Fedora** 🐾: `dnf`
    - **OpenSUSE** 🌀: `zypper`
  - Installs tools for:
    - Audio/Video: `mpv`, `ffmpeg`, `yt-dlp`
    - Networking: `speedtest-cli`
    - System Info: `inxi`
    - Power Management: `power-profiles-daemon`
    - Programming Runtimes: `python3`, `nodejs`, `ruby`, `php`, `java`, `g++`
    - Python Packages: `requests`, `beautifulsoup4`

- **Error Handling & Logs**
  - Shows clear ✅ success or ❌ failure messages.
  - Guides user for missing dependencies installation.

---

## 🔹 Notes

- Both scripts are intended for **Linux-based systems**.
- Supports **automatic detection of system tools and distributions**.
- Includes **interactive prompts** to confirm critical actions like formatting disks or uninstalling the tool.
- Uses emojis to enhance readability and UX in CLI.

---

### 🏁 Summary

Together, these scripts provide a **complete toolkit** for system management, multimedia handling, web searches, security tasks, and productivity timers—all in **one CLI utility** with user-friendly messages.
