import youtube_dl

# Define the YouTube video URL and options for audio extraction
video_url = 'https://www.youtube.com/watch?v=901QKLEkW1o'
ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}

# Download and extract audio from the video
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    info_dict = ydl.extract_info(video_url, download=False)
    audio_file = ydl.prepare_filename(info_dict)
    ydl.process_info(info_dict)
