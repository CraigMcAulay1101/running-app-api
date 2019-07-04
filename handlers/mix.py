import json
import http.client as httplib
import spotipy
import spotipy.util as util

def createmix(event, context):
    data = json.loads(event['body'])
    
    token = data['accesstoken']
    genres = data['genres']

    sp = spotipy.Spotify(auth=token)

    results = sp.recommendations(
        seed_artists=None,
        seed_genres=genres,
        seed_tracks=None,
        limit=20,
        country=None,
        tempo=data['bpm']    
    )
    return {
        'statusCode': httplib.OK,
        'body': json.dumps({'return_url': results})
    }