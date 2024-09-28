import subprocess
import yt_dlp

def stream_and_trim_video(url, start_time, end_time, output_name):
    # Get the best video and audio stream URLs without downloading
    ydl_opts = {
        'format': 'best',
        'noplaylist': True,
        'quiet': True,  # Suppress output from yt-dlp
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)  # Get info without downloading
            video_url = info['url']                       # Get the video stream URL

            # Use ffmpeg to trim the video from start_time to end_time
            start = convert_to_ffmpeg_time(start_time)
            end = convert_to_ffmpeg_time(end_time)

            trimmed_output = f"{output_name}.mp4"
            trim_video(video_url, start, end, trimmed_output)

            print(f"Trimmed video part saved as: {trimmed_output}")
            return trimmed_output

    except Exception as e:
        print(f"An error occurred: {e}")

def convert_to_ffmpeg_time(time_str):
    """ Converts time in 'HH:MM:SS' format to ffmpeg-readable format """
    if time_str.count(':') == 1:
        return f"00:{time_str}"  # Add '00:' in front if time is in MM:SS
    return time_str

def trim_video(input_url, start_time, end_time, output_file):
    """ Use ffmpeg to stream and trim the video from input_url """
    try:
        command = [
            'ffmpeg',
            '-y',  # Overwrite the file without asking
            '-i', input_url,  # Input stream URL
            '-ss', start_time,  # Start time
            '-to', end_time,  # End time
            '-c', 'copy',  # Copy video without re-encoding
            output_file  # Output file
        ]
        subprocess.run(command, check=True)
    except Exception as e:
        print(f"Error trimming video: {e}")

if __name__ == "__main__":
    youtube_url = "https://www.youtube.com/watch?v=R0DMtkfl7ww&ab_channel=FuneralonlineService" 
    start_time = "07:53:45"  # Start at 2 minutes and 30 seconds (HH:MM:SS)
    end_time = "07:56:46"  # End at 5 minutes (HH:MM:SS)
    output_name = "trimmed_part"  # Name of the output trimmed video

    stream_and_trim_video(youtube_url, start_time, end_time, output_name)

    