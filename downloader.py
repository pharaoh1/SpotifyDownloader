from library.internal import *
from library.spotify import LoadTrack, LoadAlbum
from library.youtube import SearchSong, DownloadVideo
import re

class Downloader:
    def __init__(self, dumpFile):
        self.dumpFilePath = dumpFile

        self.readFile()

    def readFile(self):
        console.info('opening file =={0}=='.format(self.dumpFilePath))
        file = open(self.dumpFilePath, 'r').read()
        saveDir = self.dumpFilePath.replace('.txt', '')

        for line in file.split('\n'):
            if (line.startswith('http')):
                trackId = re.match('http(s|)://open.spotify.com/track/(.*)', line)
                if (trackId):
                    trackId = trackId.group(2)
                    track = LoadTrack(trackId)

                    console.success('Found track in dump file: =={0}== by =={1}==, starting youtube search'.format(track.metadata.name, track.metadata.artist))
                    youtubeVideo = SearchSong(track)
                    if (youtubeVideo.metadata):
                    	DownloadVideo(track, youtubeVideo, saveDir)
                    print('')


a = Downloader('library/Mirror Master.txt')