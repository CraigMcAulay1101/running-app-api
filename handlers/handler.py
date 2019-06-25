import json
import http.client as httplib
import spotipy.util as util

def lambda_handler(event, context):
    username = 'craig1101'
    scope = 'user-library-read'
    redirecturl = util.prompt_for_user_token(username, scope)
    
    return {
        'statusCode': httplib.OK,
        'body': json.dumps({'return_url': redirecturl})
    }