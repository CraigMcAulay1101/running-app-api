import json
import http.client as httplib
import spotipy

def addtracks(event, context):
    data = json.loads(event['body'])
    
    token = data['accesstoken']

    sp = spotipy.Spotify(auth=token)

    userdata = sp.current_user()

    userid = userdata['id']
    playlist_id = data['playlist_id']
    tracks = data['tracks']

    result = sp.user_playlist_add_tracks(userid, playlist_id, tracks, position=None)
    
    return {
        'statusCode': httplib.OK,
        'headers': {
            'Access-Control-Allow-Origin': "*",
            'Access-Control-Allow-Credentials' : True,
            'Content-Type': 'application/json'
        },
        'body': json.dumps({'result': result})
    }   