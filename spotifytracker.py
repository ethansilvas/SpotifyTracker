import sys
import spotipy
import spotipy.util as util
import matplotlib

scope = 'user-library-read user-read-playback-state'

#get username from commandline
if len(sys.argv) > 1:
    username = sys.argv[1]
else:
    print ("Usage: %s username" % (sys.argv[0],))
    sys.exit()

#has users agree to allow app see/use functions from scope
token = util.prompt_for_user_token(username, scope)

#make sure that username is valid
if token:
    sp = spotipy.Spotify(auth=token)

    while True:
        newTrack = sp.current_user_playing_track()
        currentTrack = newTrack['item']['name']
        isPlaying = newTrack['is_playing']
        print(currentTrack)

        print("hi")
        if (isPlaying == False):
            print("no")

    results = sp.current_user_saved_tracks()
    for item in results['items']:
        track = item['track']
        print (track['name'] + ' - ' + track['artists'][0]['name'])
else:
    print ("Can't get token for", username)
