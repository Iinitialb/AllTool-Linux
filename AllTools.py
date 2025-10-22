#!/usr/bin/env python3
import sys
import subprocess
import os

def main():
    if len(sys.argv) < 2:
        print("Usage: alltool <command> [args]")
        print("Available commands: create, format, refresh, help, netspeed, sound, video, downloadvs, requirement")
        return

    command = sys.argv[1]

    if command == "create":
        if len(sys.argv) < 3:
            print("Usage: alltool create <filename>")
            return
        filepath = sys.argv[2]
        folder = os.path.dirname(filepath)
        if folder and not os.path.exists(folder):
            os.makedirs(folder)
        subprocess.run(["touch", filepath])

    elif command == "format":
        if len(sys.argv) < 4:
            print("Usage: alltool format <disk> <type>")
            return
        disk = sys.argv[2]
        fs_type = sys.argv[3].lower()

        formatters = {
            "ntfs": "mkfs.ntfs",
            "ext4": "mkfs.ext4",
            "vfat": "mkfs.vfat"
        }

        if fs_type not in formatters:
            print(f"Unsupported format type: {fs_type}")
            print(f"Supported types: {', '.join(formatters.keys())}")
            return

        print(f"⚠️ Warning: Make sure '{disk}' is a valid device like /dev/sdb1")
        confirm = input(f"Are you sure you want to format {disk} as {fs_type}? This will erase all data! (yes/no): ")
        if confirm.lower() != "yes":
            print("Aborted.")
            return

        print(f"Formatting {disk} as {fs_type}...")
        subprocess.run(["sudo", formatters[fs_type], disk])
    elif command == "refresh":
        print("🔄 Refreshing alltool setup...")

        # Make script executable
        script_path = os.path.expanduser("~/bin/AllTools.py")
        subprocess.run(["chmod", "+x", script_path])

        # Detect shell config file
        shell = os.environ.get("SHELL", "")
        if "zsh" in shell:
            config_file = os.path.expanduser("~/.zshrc")
        elif "bash" in shell:
            config_file = os.path.expanduser("~/.bashrc")
        else:
            config_file = os.path.expanduser("~/.profile")

        # Check if PATH is already set
        path_line = 'export PATH="$HOME/bin:$PATH"'
        already_set = False
        if os.path.exists(config_file):
            with open(config_file, "r") as f:
                for line in f:
                    if path_line in line:
                        already_set = True
                        break

        # Append if missing
        if not already_set:
            with open(config_file, "a") as f:
                f.write(f"\n# Added by alltool\n{path_line}\n")
            print(f"✅ PATH updated in {config_file}")
        else:
            print(f"ℹ️ PATH already set in {config_file}")

        print("Please run: source ~/.zshrc or restart your terminal to apply changes.")
        print("Refresh complete.")


    elif command == "help":
        lang = sys.argv[2] if len(sys.argv) > 2 else "en"

        help_texts = {
            "en": """
Usage: alltool <command> [args]
Available commands:
  create <filename>         Create a file, auto-create folders if needed
  format <disk> <type>      Format disk (types: ntfs, ext4, vfat)
  refresh                   Refresh permissions and show PATH setup
  help [lang]               Show help in en, fr, ar, de
  sound <file|playlist.txt> Play audio file or playlist (wav, mp3, ogg, flac, aac, m4a)
  downloadvs <url>          Download video or audio from supported websites using yt-dlp
  requirement               Check if alltool dependencies are installed
""",
            "fr": """
Utilisation : alltool <commande> [arguments]
Commandes disponibles :
  create <fichier>          Crée un fichier, crée les dossiers si nécessaire
  format <disque> <type>    Formate le disque (types : ntfs, ext4, vfat)
  refresh                   Actualise les permissions et affiche le PATH
  help [langue]             Affiche l'aide en en, fr, ar, de
  sound <fichier|playlist.txt> Joue un fichier audio ou une playlist (wav, mp3, ogg, flac, aac, m4a)
  downloadvs <url>          Télécharge une vidéo ou un audio depuis les sites pris en charge via yt-dlp
  requirement               Vérifie si les dépendances de alltool sont installées
""",
            "ar": """
الاستخدام: alltool <الأمر> [المعطيات]
الأوامر المتاحة:
  create <اسم الملف>        إنشاء ملف، وإنشاء المجلدات تلقائيًا إذا لزم الأمر
  format <القرص> <النوع>     تهيئة القرص (الأنواع: ntfs، ext4، vfat)
  refresh                    تحديث الصلاحيات وعرض إعداد PATH
  help [اللغة]               عرض المساعدة باللغات: en، fr، ar، de
  sound <ملف|playlist.txt>     تشغيل ملف صوتي أو قائمة تشغيل (wav، mp3، ogg، flac، aac، m4a)
  downloadvs <الرابط>          تحميل فيديو أو صوت من المواقع المدعومة باستخدام yt-dlp
  requirement               التحقق من تثبيت متطلبات alltool
""",
            "de": """
Verwendung: alltool <Befehl> [Argumente]
Verfügbare Befehle:
  create <Dateiname>        Datei erstellen, Ordner bei Bedarf automatisch
  format <Datenträger> <Typ> Datenträger formatieren (Typen: ntfs, ext4, vfat)
  refresh                   Berechtigungen aktualisieren und PATH anzeigen
  help [Sprache]            Hilfe anzeigen in en, fr, ar, de
  sound <Datei|playlist.txt>   Audio oder Playlist abspielen (wav, mp3, ogg, flac, aac, m4a)
  downloadvs <url>          Video oder Audio von unterstützten Seiten mit yt-dlp herunterladen
  requirement               Prüft, ob alle Abhängigkeiten installiert sind
"""
        }

        print(help_texts.get(lang, help_texts["en"]))
    elif command == "sound":
        if len(sys.argv) < 3:
            print("Usage: alltool sound <path_to_audio_file_or_playlist.txt>")
            return
        input_path = os.path.expanduser(sys.argv[2])

        if not os.path.exists(input_path):
            print(f"❌ Error: File '{input_path}' does not exist.")
            return

        supported_formats = [".wav", ".mp3", ".ogg", ".flac", ".aac", ".m4a"]

        # Check if it's a playlist
        if input_path.lower().endswith(".txt"):
            print(f"📃 Playing playlist: {input_path}")
            with open(input_path, "r") as f:
                for line in f:
                    audio_file = os.path.expanduser(line.strip())
                    if not os.path.exists(audio_file):
                        print(f"⚠️ Skipping missing file: {audio_file}")
                        continue
                    if not any(audio_file.lower().endswith(ext) for ext in supported_formats):
                        print(f"⚠️ Skipping unsupported format: {audio_file}")
                        continue
                    print(f"🔊 Playing: {audio_file}")
                    subprocess.run(["mpv", "--really-quiet", audio_file])
        else:
            if not any(input_path.lower().endswith(ext) for ext in supported_formats):
                print("❌ Error: Unsupported file format. Supported formats: wav, mp3, ogg, flac, aac, m4a")
                return
            print(f"🔊 Playing sound: {input_path}")
            subprocess.run(["mpv", "--really-quiet", input_path])
    elif command == "netspeed":
        print("Measuring network speed...")
        subprocess.run(["speedtest-cli"])
    elif command == "requirement":
        print("🔍 Checking system requirements for alltool...")

        requirements = {
            "mpv": "Sound playback (multi-format)",
            "speedtest-cli": "Network speed test",
            "mkfs.ntfs": "Format NTFS disks",
            "mkfs.ext4": "Format EXT4 disks",
            "mkfs.vfat": "Format VFAT disks",
            "touch": "Create files",
            "ffmpeg": "Video processing and conversion",
            "ffplay": "Video playback",
            "yt-dlp": "Download videos and audio from websites"
        }

        for tool, desc in requirements.items():
            result = subprocess.run(["which", tool], stdout=subprocess.DEVNULL)
            status = "✅ Installed" if result.returncode == 0 else "❌ Missing"
            print(f"{tool:<12} {status} — {desc}")
    elif command == "video":
        if len(sys.argv) < 3:
            print("Usage: alltool video <path_to_video>")
            return
        video_path = os.path.expanduser(sys.argv[2])
        if not os.path.exists(video_path):
            print(f"❌ Error: File '{video_path}' does not exist.")
            return
        print(f"🎬 Playing video: {video_path}")
        subprocess.run(["ffplay", "-autoexit", video_path])
    elif command == "downloadvs":
        if len(sys.argv) < 3:
            print("Usage: alltool downloadvs <video_or_audio_url>")
            return
        url = sys.argv[2]

        # Check if yt-dlp is installed
        result = subprocess.run(["which", "yt-dlp"], stdout=subprocess.DEVNULL)
        if result.returncode != 0:
            print("❌ yt-dlp is not installed. Please install it with: sudo pacman -S yt-dlp")
            return

        print(f"⬇️ Downloading from: {url}")
        subprocess.run(["yt-dlp", url])
    else:
        print(f"Unknown command: {command}")

if __name__ == "__main__":
    main()