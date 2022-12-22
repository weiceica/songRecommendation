import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy.util as spo

if __name__ == "__main__":
    username = "weiceica"
    user_id = "b2714d0ebea740edb51613c004bbfa6c"
    user_secret = "2b7bd29633944b19a52becd985b8ccfe"
    uri = 'http://localhost:7777/callback'
    scope = "user-library-read"

    token = spo.prompt_for_user_token(username=username,
                                      scope=scope,
                                      client_id=user_id,
                                      client_secret=user_secret,
                                      redirect_uri=uri)
    print(token)
    

