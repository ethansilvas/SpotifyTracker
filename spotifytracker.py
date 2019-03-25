#imports for spotify api
import sys
import os
import time
import spotipy
import spotipy.util as util

#imports for graphing
import matplotlib
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

def main():
    #only need to access currently playing song
    scope = 'user-read-playback-state'

    #get username from commandline
    if len(sys.argv) > 1:
        username = sys.argv[1]
    else:
        print ("Usage: %s username" % (sys.argv[0],))
        sys.exit()

    #has users agree to allow script to see/use functions from scope
    token = util.prompt_for_user_token(username, scope)

    #make sure that username is valid
    if token:
        sp = spotipy.Spotify(auth=token)

        #create a dictionary to hold songs, the values will be the time listened
        songsPlayed = dict()

        #open songsplayed.txt to see if there is already a dictionary of songs
        try:
            f = open("songsplayed.txt", 'r')
            path = "./songsplayed.txt"

            #if songsplayed.txt has a dictionary in it, set songsPlayed to it
            if os.path.exists(path) and os.path.getsize(path) > 0:
                songsPlayed = eval(f.readline())
        except IOError:
            print("Can't open file.")

        print(songsPlayed)

        #loop and add songs to songsPlayed while spotify is open
        spotifyIsOpen = True;
        while spotifyIsOpen:
            newTrack = sp.current_user_playing_track()

            #add songs if newTrack is not empty (when app is open)
            if newTrack is not None:
                currentTrack = newTrack['item']['name']

                #loop while the current song is playing to keep time
                print(currentTrack)
                isPlaying = True;
                startTime = None
                while isPlaying:
                    copyOfNewTrack = sp.current_user_playing_track()

                    if copyOfNewTrack is not None:
                        isPlaying = copyOfNewTrack['is_playing']

                        #if a song is playing, start keeping time
                        if isPlaying:
                            #only set startTime if it hasn't been set
                            if startTime is None:
                                startTime = time.time()
                    else:
                        isPlaying = False

                #add/set the value for the key (song) to the elapsed time
                if startTime is not None:
                    timeListened = time.time() - startTime

                    if songsPlayed.get(currentTrack) is None:
                        songsPlayed[currentTrack] = timeListened
                    else:
                        songsPlayed[currentTrack] += timeListened
            else:
                #newTrack is empty, so spotify is not open
                print("Hello")
                spotifyIsOpen = False

        #if songs were added to the set, add them to songsplayed.txt
        if len(songsPlayed) is not 0:
            addSongsToFile(songsPlayed)
    else:
        print ("Can't get token for", username)

#function to update the dictionary of songs in songsplayed.txt
def addSongsToFile(songsPlayed):
    f = open("songsplayed.txt", "w+")
    f.write(str(songsPlayed))

if __name__== "__main__":
    main()
