#   Libraries

import putio, os, time

#   Paths

def GetSettings():
    with open('Settings.txt') as f:
        lines = f.read().splitlines()
        return lines

# Upload magnet Link from File

def PutioUpload(path, folderid):
    print('uploading')
    for file in os.listdir(path):
        if file.endswith(".magnet"):
            print('uploading ' + file)
            with open(Settings[0] + file, 'r') as f:
                for line in f:
                    client.Transfer.add_url(line, folderid)

# Delete uploaded files

def TorrentFolderCleanup(path):
    files = os.listdir(path)
    count = 0
    for file in files:
        if file.endswith(".magnet") or file.endswith(".torrent"):
            count = count +1
            os.remove(os.path.join(path,file))
            
    if count > 0:
        print('Waiting 30sec for pending downloads to finalize')
        time.sleep(30)
       

def PutioDownload(path1, path2, folderid):

    TransferList = client.Transfer.list()
    transferlen = len(TransferList)
    files = client.File.list(folderid)
    print('files discovered for downloading', files)

    if transferlen != 0:
        os.chdir(path2)
        for file in files:
            print('Downloading:', file.name)
            client.File.download(file)
            client.File.delete(file)
            print('Download complete. Folder deleted on put.io')
        client.Transfer.clean()
        
        

Settings = GetSettings()

client = putio.Client(Settings[2]) # Instanciate Client Object

PutioUpload(Settings[0], Settings[3]) # Upload Magnet Files

TorrentFolderCleanup(Settings[0]) # Cleanup Uploaded File



PutioDownload(Settings[0], Settings[1], Settings[3]) #Download TV Files

    

