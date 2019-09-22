import json
import http.client as httplib
import spotipy
import spotipy.util as util

def createplaylist(event, context):
    data = json.loads(event['body'])
    
    token = data['accesstoken']

    sp = spotipy.Spotify(auth=token)

    userdata = sp.current_user()

    userid = userdata['id']
    playlistname = data['name']

    result = sp.user_playlist_create(userid, playlistname, public=True)
    
    return {
        'statusCode': httplib.OK,
        'headers': {
            'Access-Control-Allow-Origin': "*",
            'Access-Control-Allow-Credentials' : True,
            'Content-Type': 'application/json'
        },
        'body': json.dumps({'playlist_id': result['id']})
    }   