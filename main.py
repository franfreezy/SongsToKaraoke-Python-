import yt_dlp

def stream_youtube_audio(url):
    ydl_opts = {
        'format': 'bestaudio/best',  # Download best available audio
        'noplaylist': True,          # Do not download playlists, only the single video
        'postprocessors': [{         # Convert the audio to mp3
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',  # Specify mp3 format
            'preferredquality': '192', # Set the audio quality (192 kbps)
        }],
        'outtmpl': '%(title)s.%(ext)s',  # Output template: Save as the title of the video
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)  # Set download to True
            print(f"Downloaded and converted: {info['title']}.mp3")
            return info['title'] + ".mp3"
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    youtube_url = "https://www.youtube.com/watch?v=MzsYibilgFU&ab_channel=LIVETUNESMEDIALTM-WORLD"  # Replace with actual YouTube video URL
    stream_youtube_audio(youtube_url)