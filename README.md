# SonnarPutio
Uploads Magnet Files from Sonnar to Put.io and Downloads TV Shows

How it works:

* As a torrent blackhole, sonarr will dump magnet files in your torrent folder. 
* This script will upload those magnet files to put.io, starting their transfers.
* They'll be put into a put.io folder you designate.
* When this script sees new episodes in that put.io folder it downloads them to your local Watch folder. It then **deletes** those files from your put.io folder.
* Sonarr then sees the local and newly downloaded episodes and moves them to their correct location.


## Setup

```sh
pip install -r requirements
```

Create a Torrent Folder. Example: C:\Torrent	

Create a Watch Folder - 	Example: C:\Watch

Get a token key. Open https://api.put.io/v2/oauth2/authenticate?client_id=28&response_type=oob , confirm and save the token key.

Create a Settings.txt file with these four values each on their own line:
 - torrent folder path
 - watch folder path
 - Your Put.io Token Key. 
 - Put.io Folder ID of where you want the files to download to
 
... for example:

```txt
C:\Torrent
C:\Watch
O7TZ6CZ5Z4KHNNAWDKUW
1063423147
```

	
Go into Sonarr and Add a new Download Client. Select "Torrent blackhole" as the type.


	Name:					putio_torrent_watch (or whatever you want)
	Enable:					Yes

	Torrent Folder			Example: C:\Torrent\
							Choose the same folder as you did during Setup
							
	Watch Folder			Example: C:\Watch\
							Choose the same folder as you did during Setup	
							
	Save Magnet Files:		Yes

	Read Only				No
	

Move these .py files and Settings.txt into the Torrent folder

Run `python SonnarPutio.py` manually to verify it works.

Go into Sonarr and Create a Connection (it'll call this script after certain events). Select "Custom Script".
	
	Name:					Putio-Upload
	On Grab, On Import:		Yes
	On Upgrade:             Yes
	On *:					No
	
	Path:					Example: C:\Torrent\SonnarPutio.py
	

You may also want to create a scheduled task (outside of Sonarr) to run SonnarPutio.py for more frequent downloads.
