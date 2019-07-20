import json
import http.client as httplib
import spotipy
import spotipy.util as util

def createmix(event, context):
    data = json.loads(event['body'])

    kwargs = {}
    
    token = data['accesstoken']
    genre = data['genres']
    kwargs['target_tempo'] = data['bpm']
    
    sp = spotipy.Spotify(auth=token)

    results = sp.recommendations(
        seed_artists=None,
        seed_genres=[genre],
        seed_tracks=None,
        limit=20,
        country=None,
        **kwargs    
    )
    
    return {
        'statusCode': httplib.OK,
        'body': json.dumps({'tracks': results['tracks']})
    }