# SonnarPutio
Uploads Magnet Files from Sonnar to Put.io and Downloads TV Shows

Run Setup.py first and Complete GUI setup

	Select or Create a Torrent Folder - Example: C:\Torrent
		
	Select or Create a Watch Folder - 	Example: C:\Watch
		
	Type or Paste Your Put.io Token Key
	
	Type or Paste Folder ID of folder where TV files are stored on Put.io
	
	Results are stored in Settings.txt in Torrent Folder
		Example: C:\Torrent\Settings.txt
	
	
Go into Sonarr and Configure Download Client as Blackhole Diretcory
	Name:					Torrent
	Enable:					Yes
	Torrent Folder			Example: C:\Torrent\
							Choose the same folder as you did during Setup
							
	Watch Folder			Example: C:\Watch\
							Choose the same folder as you did during Setup	
							
	Save Magnet Files:		Yes

	Read Only				No
	
	
Go into Sonarr and Create a Connection
	
	Connection Type Custom Script
	
	Name:					Putio-Upload
	On Grab:				Yes
	On Download:			No
	Filter Series Tags:		
	Path:					Example: C:\Python27\python.exe
	Arguments:				Example: C:\Torrent\SonnarPutio.py
	

You may also want to create a scheduled task to run SonnarPutio.py for more frequent downloads
