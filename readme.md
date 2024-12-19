# Youtube Playlist Mass Downloader: 
Simply paste the URL of a given youtube playlist, and it will download the respective videos locally offline.

# To run:
- python3 -m venv venv
- source venv/bin/activate

If you get permission errors on Linux/Mac, you might need to run:
- chmod 700 ~/Library/Application\ Support/Google/Chrome 

## Cookies.txt
You can access private playlists by providing your YouTube cookies to yt-dlp. Here's how to do it:

First, you'll need to get your YouTube cookies. The easiest way is to:

Install the "Cookie-Editor" extension for your browser (available for Chrome/Firefox)
Go to YouTube and log in
Click the Cookie-Editor extension icon
Click "Export" -> "Export as Netscape HTTP Cookie File"
Save this as "cookies.txt" in your script directory