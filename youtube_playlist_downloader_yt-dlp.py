import yt_dlp
import os
import ssl
from typing import Optional


def download_playlist(playlist_url: str, output_dir: Optional[str] = None) -> None:
    """
    Download videos from a YouTube playlist as MP4 files in 1080p quality.
    
    Args:
        playlist_url (str): URL of the YouTube playlist.
        output_dir (str, optional): Directory to save the downloaded videos.
                                    If None, creates an 'OUT' directory in the current path.
    """
    # Set default output directory to "OUT" in current directory
    if output_dir is None:
        output_dir = os.path.join(os.getcwd(), 'OUT')
    
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    print(f"Using output directory: {output_dir}")
    
    # Path to cookies.txt in the current directory
    cookies_file = os.path.join(os.getcwd(), 'cookies.txt')
    
    # Configure yt-dlp options
    ydl_opts = {
        # Try to get the best 1080p video with audio; fall back to best available
        'format': 'bestvideo[height=1080]+bestaudio/best',
        'outtmpl': os.path.join(output_dir, '%(title)s.%(ext)s'),  # Output template
        'ignoreerrors': True,  # Skip videos that can't be downloaded
        'nocheckcertificate': True,  # Skip HTTPS certificate validation
        'merge_output_format': 'mp4',
        'postprocessors': [{
            'key': 'FFmpegVideoRemuxer',
            'preferedformat': 'mp4',
        }],
        'noplaylist': False,  # Enable playlist downloading
        'yes_playlist': True,  # Confirm that we want the full playlist
    }
    
    # Add cookies file if it exists
    if os.path.exists(cookies_file):
        ydl_opts['cookiefile'] = cookies_file
        print(f"Using cookies from: {cookies_file}")
    else:
        print(f"Warning: Cookies file {cookies_file} not found. Continuing without cookies.")
    
    try:
        # Create unverified context for SSL
        ssl._create_default_https_context = ssl._create_unverified_context
        
        # Clean up the playlist URL to ensure we're getting the playlist
        if 'playlist?list=' not in playlist_url and 'list=' in playlist_url:
            # Convert video URL with playlist to proper playlist URL
            playlist_id = playlist_url.split('list=')[1].split('&')[0]
            playlist_url = f'https://www.youtube.com/playlist?list={playlist_id}'
            print(f"Converted URL to playlist URL: {playlist_url}")
        
        # Create yt-dlp object with our options
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            # Download the playlist
            print(f"Starting download of playlist: {playlist_url}")
            ydl.download([playlist_url])
            print(f"\nDownload complete! Videos saved to: {output_dir}")
            
    except Exception as e:
        print(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    # Example usage
    playlist_url = input("Enter the YouTube playlist URL: ")
    output_dir = "OUT/"
    
    if not output_dir:
        output_dir = None
    
    download_playlist(playlist_url, output_dir)
