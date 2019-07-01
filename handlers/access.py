import json
import http.client as httplib
import spotipy.oauth2 as oauth2

def getaccesstoken(event, context):
    data = json.loads(event['body'])

    if 'code' not in data:
        return {
            'statusCode': httplib.UNPROCESSABLE_ENTITY,
            'body': json.dumps({ 'error': 'Could not retrieve code' })
        }

    sp_oauth = oauth2.SpotifyOAuth(client_id=None, client_secret=None, redirect_uri=None)

    code = data['code']
    token_info = sp_oauth.get_access_token(code)
    access_token = token_info['access_token']

    if access_token:      
        return {
            'statusCode': httplib.OK,
            'body': json.dumps({'access_token': access_token })
        }
    else:
        return {
            'statusCode': httplib.UNPROCESSABLE_ENTITY,
            'body': json.dumps({ 'error': 'Could not process code' })
        }   