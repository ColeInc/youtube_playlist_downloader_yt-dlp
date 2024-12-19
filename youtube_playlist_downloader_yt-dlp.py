import yt_dlp
import os
import ssl
from typing import Optional

def download_playlist(playlist_url: str, output_dir: Optional[str] = None) -> None:
    """
    Download videos from a YouTube playlist as MP4 files.
    
    Args:
        playlist_url (str): URL of the YouTube playlist
        output_dir (str, optional): Directory to save the downloaded videos.
                                  If None, creates an 'OUT' directory in the current path.
    """
    # Set default output directory to "OUT" in current directory
    if output_dir is None:
        output_dir = os.path.join(os.getcwd(), 'OUT')
    
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    print(f"Using output directory: {output_dir}")
    
    # Configure yt-dlp options
    ydl_opts = {
        'format': 'best[ext=mp4]',  # Best quality MP4
        'outtmpl': os.path.join(output_dir, '%(title)s.%(ext)s'),  # Output template
        'ignoreerrors': True,  # Skip videos that can't be downloaded
        'extract_flat': 'in_playlist',  # Extract info about playlist items
        'quiet': False,  # Show progress
        'progress': True,  # Show progress bar
        'no_warnings': False,  # Show warnings
        'nocheckcertificate': True,  # Skip HTTPS certificate validation
        'postprocessors': [{
            'key': 'FFmpegVideoRemuxer',
            'preferedformat': 'mp4',
        }]
    }
    
    try:
        # Create unverified context for SSL
        ssl._create_default_https_context = ssl._create_unverified_context
        
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