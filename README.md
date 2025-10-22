# AllTools - Comprehensive Linux Utility Tool

<img width="1006" height="660" alt="Screenshot From 2025-10-21 19-02-54" src="https://github.com/user-attachments/assets/2812eae7-4dbe-4bef-84c7-4496a5c8eb1a" />


## Overview
AllTools is a powerful command-line utility that provides a comprehensive suite of tools for Linux users. It combines file management, system control, media handling, network tools, and development utilities into a single, easy-to-use interface.

## 🚀 Core Features

### 📁 File Management
- **File Creation**: Create files with automatic directory creation
- **File Listing**: Quick directory listing with `sf` command
- **File Hashing**: Calculate MD5, SHA1, SHA256, SHA512, BLAKE2B, and BLAKE2S hashes
- **Script Execution**: Auto-detect and run scripts in multiple languages (Python, Bash, JavaScript, Perl, Ruby, PHP, Java, C/C++)

### 💾 Disk Management
- **Disk Formatting**: Format disks with NTFS, EXT4, and VFAT filesystems
- **Safe Formatting**: Interactive confirmation before destructive operations
- **Multi-format Support**: Support for Windows, Linux, and universal filesystems

### 🎵 Media & Entertainment
- **Audio Playback**: Play audio files in multiple formats (WAV, MP3, OGG, FLAC, AAC, M4A)
- **Playlist Support**: Play audio playlists from text files
- **Video Playback**: Play video files with FFplay integration
- **Media Download**: Download videos and audio from supported websites using yt-dlp

### 🌐 Network & Internet
- **Speed Testing**: Test internet connection speed with speedtest-cli
- **Web Search**: Search the web using DuckDuckGo integration
- **Weather Information**: Get weather data for any city worldwide
- **Video/Audio Download**: Download content from YouTube, Vimeo, and other platforms

### ⚡ System Control & Power Management
- **Power Profiles**: Switch between power-saver, balanced, and performance modes
- **System Control**: Shutdown, reboot, logout, suspend, hibernate
- **Screen Locking**: Lock screen functionality
- **Power Status**: Check current power mode

### 🔧 System Information & Maintenance
- **System Info**: Display detailed system information with inxi
- **Update Checking**: Check for system updates across multiple package managers
- **Package Manager Support**: Works with APT, Pacman, DNF, and Zypper
- **Requirements Check**: Verify all dependencies are installed

### 🔐 Security & Utilities
- **Password Generation**: Generate secure passwords with customizable options
- **Character Set Control**: Include/exclude lowercase, uppercase, digits, special characters
- **Hash Verification**: Verify file integrity with multiple hash algorithms
- **Secure Operations**: Safe file operations with confirmation prompts

### 🌍 Multi-Language Support
- **Help System**: Available in English, French, Arabic, and German
- **Localized Interface**: Context-aware help in multiple languages
- **Cultural Adaptation**: Region-specific formatting and terminology

### 🛠️ Development Tools
- **Multi-Language Runtime**: Support for Python, Node.js, Perl, Ruby, PHP, Java, C/C++
- **Auto-Detection**: Automatically detect script type and execute appropriately
- **Compiler Integration**: Automatic compilation for C/C++ code
- **JAR Execution**: Run Java applications seamlessly

## 📋 Command Reference

### File Operations
```bash
alltool create <filename>           # Create file with auto-directory creation
alltool sf                          # Show files in current directory
alltool hs <file> <hash_type>       # Calculate file hash
alltool run <script_path>           # Auto-detect and run scripts
```

### Disk Management
```bash
alltool format <disk> <type>        # Format disk (ntfs, ext4, vfat)
```

### Media & Entertainment
```bash
alltool sound <file|playlist.txt>   # Play audio files or playlists
alltool video <path>                # Play video files
alltool downloadvs <url>            # Download videos/audio from websites
```

### Network & Internet
```bash
alltool netspeed                    # Test internet speed
alltool sr <topic>                  # Search the web
alltool wea <city>                  # Get weather information
```

### System Control
```bash
alltool power pws                   # Power-saver mode
alltool power pwn                   # Balanced mode
alltool power pwp                   # Performance mode
alltool power pwst                  # Check power status
alltool power pwo                   # Shutdown system
alltool power pwr                   # Reboot system
alltool power pwl                   # Logout
alltool power pwsu                  # Suspend system
alltool power pwh                   # Hibernate system
alltool power pwlo                  # Lock screen
```

### System Information
```bash
alltool sif                         # Show detailed system information
alltool up                          # Check for system updates
alltool requirement                 # Check installed dependencies
```

### Security & Utilities
```bash
alltool psg <length> [options]      # Generate secure password
# Options: nose (no lowercase), nos (no uppercase), 
#          not (no digits), nol (no special characters)
```

### Help & Support
```bash
alltool help [language]             # Show help (en, fr, ar, de)
alltool refresh                     # Refresh alltool setup
```

## 🎯 Key Benefits

### 🚀 Efficiency
- **Single Command Interface**: Access all tools through one command
- **Auto-Detection**: Intelligent script and file type detection
- **Batch Operations**: Handle multiple files and operations efficiently

### 🛡️ Safety
- **Confirmation Prompts**: Safe operations with user confirmation
- **Error Handling**: Comprehensive error checking and reporting
- **Backup Awareness**: Operations that preserve data integrity

### 🌐 Compatibility
- **Multi-Distribution**: Works on Debian, Arch, Fedora, and openSUSE-based systems
- **Cross-Platform**: Supports multiple Linux distributions
- **Package Manager Integration**: Works with all major package managers

### 🔧 Developer-Friendly
- **Multi-Language Support**: Run scripts in 7+ programming languages
- **Auto-Compilation**: Automatic C/C++ compilation and execution
- **Development Tools**: Integrated development utilities

### 🎨 User Experience
- **Intuitive Commands**: Easy-to-remember command structure
- **Rich Output**: Emoji-enhanced status messages and progress indicators
- **Multi-Language Help**: Localized help system in 4 languages

## 🛠️ Installation & Setup

### Automatic Installation
```bash
python3 AllToolInstaller.py
```

### Manual Setup
1. Install dependencies using your package manager
2. Copy AllTools.py to ~/bin/alltool
3. Make it executable: `chmod +x ~/bin/alltool`
4. Add ~/bin to your PATH

### Dependencies
- **System Tools**: mpv, ffmpeg, speedtest-cli, yt-dlp, inxi, power-profiles-daemon
- **Programming**: Python 3, Node.js, Ruby, PHP, Java, GCC
- **Python Packages**: requests, beautifulsoup4
- **File System**: ntfs-3g, e2fsprogs, dosfstools

## 🎉 Use Cases

### 👨‍💻 Developers
- Run scripts in multiple languages
- Generate secure passwords
- Calculate file hashes for verification
- System information and diagnostics

### 🎵 Media Enthusiasts
- Play audio and video files
- Download content from websites
- Create and manage playlists
- Media format conversion

### 🔧 System Administrators
- System power management
- Disk formatting and management
- Network speed testing
- System updates and maintenance

### 🌐 General Users
- Weather information
- Web search capabilities
- File management
- System information

## 🚀 Getting Started

1. **Install AllTools**: Run the installer script
2. **Check Requirements**: `alltool requirement`
3. **Explore Commands**: `alltool help`
4. **Start Using**: Try `alltool sound <audio_file>` or `alltool wea <city>`

AllTools transforms your Linux terminal into a powerful, all-in-one utility suite that handles everything from basic file operations to advanced system management and media playback. It's designed to be intuitive, safe, and comprehensive - making Linux system management more accessible and efficient for users of all skill levels.
