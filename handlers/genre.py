import json
import http.client as httplib
import spotipy

def genreseeds(event, context):
    print(event)
    data = json.loads(event['body'])
    token = data['accesstoken']

    sp = spotipy.Spotify(auth=token)

    results = sp.recommendation_genre_seeds()
    
    return {
        'statusCode': httplib.OK,
        'headers': {
            'Access-Control-Allow-Origin': "*",
            'Access-Control-Allow-Credentials' : True,
            'Content-Type': 'application/json'
        },
        'body': json.dumps({'genres': results})
    }