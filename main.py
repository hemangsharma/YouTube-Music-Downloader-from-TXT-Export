#!/usr/bin/env python3
import os
import csv
import yt_dlp
from rich import print
from rich.prompt import Prompt

def parse_songs_from_txt(txt_path):
    """Try multiple encodings to parse a tab-delimited TXT; return list of (name, artist)."""
    encodings = ['utf-8', 'utf-16', 'latin1']
    last_error = None

    for enc in encodings:
        try:
            with open(txt_path, 'r', encoding=enc) as f:
                reader = csv.DictReader(f, delimiter='\t')
                songs = []
                for row in reader:
                    name   = row.get('Name', '').strip()
                    artist = row.get('Artist', '').strip()
                    if name:  # require at least a song name
                        songs.append((name, artist))
                return songs
        except UnicodeDecodeError as e:
            last_error = e
            continue

    # if we get here, none of the encodings worked
    raise UnicodeDecodeError(
        f"Unable to decode '{txt_path}' with tried encodings: {encodings}"
    ) from last_error

def download_song_from_youtube(query, download_path):
    """Search & download the song from YouTube as an mp3 (bestaudio)."""
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': os.path.join(download_path, '%(title)s.%(ext)s'),
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'quiet': True,
        'noplaylist': True,
        'default_search': 'ytsearch1',
        'no_warnings': True
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            print(f"[cyan]↓[/cyan] [bold]Downloading[/bold]: {query}")
            ydl.download([query])
        except Exception as e:
            print(f"[red]✗ Failed:[/] {query} → {e}")


def main():
    print("[bold green]YouTube Music Downloader from TXT Export[/bold green]\n")

    txt_path = Prompt.ask("[green]Path to your tab‑delimited TXT file[/]")
    download_path = Prompt.ask("[green]Where to save MP3 files[/]")

    # ensure output folder exists
    os.makedirs(download_path, exist_ok=True)

    # parse
    try:
        songs = parse_songs_from_txt(txt_path)
    except Exception as e:
        print(f"[red]Error parsing file:[/] {e}")
        return

    total = len(songs)
    print(f"\n[bold yellow]Found {total} songs. Starting downloads...[/bold yellow]\n")

    # download each
    for idx, (name, artist) in enumerate(songs, start=1):
        query = f"{name} {artist}".strip()
        print(f"[bold]{idx}/{total}[/bold]: {query}")
        download_song_from_youtube(query, download_path)

    print("\n[bold green]All done![/bold green]")

if __name__ == '__main__':
    main()
