# YouTube Music Downloader from TXT Export

A simple CLI tool that reads a tab‑delimited TXT export (e.g. from Apple Music), parses **all** listed tracks, and downloads each song’s audio from YouTube as a high‑quality MP3.


## Requirements

- **Python 3.7+**  
- [`yt-dlp`](https://github.com/yt-dlp/yt-dlp)  
- [`rich`](https://github.com/Textualize/rich)  
- **ffmpeg** must be installed and available on your system `PATH`

```bash
pip install yt-dlp rich
```

### Installing ffmpeg:
#### macOS: 
```bash
brew install ffmpeg
```
#### Ubuntu: 
```bash
sudo apt install ffmpeg
```
#### Windows: 
```bash
download from https://ffmpeg.org/download.html
```

## Usage
Save the script as download_music.py.

Run it:

```bash
python download_music.py
```

When prompted:

Path to your tab‑delimited TXT file
e.g. ``` /Users/you/MusicExport/Top25MostPlayed.txt```

Where to save MP3 files
e.g. ```/Users/you/MusicDownloads```

The script will:

Try reading your TXT with UTF‑8, UTF‑16, then Latin‑1.

Parse out every row’s Name and Artist.

Search YouTube (ytsearch1) for each “Name Artist” query.

Download the best audio and convert it to 192 kbps MP3.

You’ll see a progress list like:

```
1/25: Song Title Artist Name
↓ Downloading: Song Title Artist Name
...
All done!
```

## Input Format
Your .txt must be tab-delimited and include at least these columns in the header row:
Name
Artist
Additional columns are ignored.

## Troubleshooting
### UnicodeDecodeError
If you still see encoding errors, ensure your export really is plain TXT (not XLS/X) and in one of the supported encodings (UTF‑8/16, Latin‑1).

### ffmpeg not found
Make sure ffmpeg is installed and on your PATH. Running ffmpeg -version should print its version info.

### Download failures
Sometimes YouTube search may return an unrelated result. You can rerun just that query or adjust the search terms manually.

## Disclaimer
This tool is for personal use only. Ensure you comply with YouTube’s Terms of Service and your local copyright laws when downloading audio.
