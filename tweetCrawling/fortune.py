import tweepy

API_KEY = 'api_key'
API_SECRET = 'api_secret'
ACCESS_KEY = 'access_key'
ACCESS_SECRET = 'access_secret'

oAuth = tweepy.OAuthHandler(API_KEY, API_SECRET)
oAuth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth_handler= oAuth, api_root = '/1.1')

if __name__ == "__main__":
    # userID = 365546416 #@fortune_cookie2
    userID = 990433830 #@FortuneCookie_5
    user = api.get_user(userID)
    timeline = api.user_timeline(userID, count = 1000)

    for tweet in timeline:
        try:
            texts = tweet.text
            # print(texts)
            if '@' in texts:
                texts = texts.split(' ')[1:]
                str = ' '.join(texts)
                print(str)
                with open('fortune.txt', 'a') as f:
                    f.write(str + '\r\n')

        except AttributeError as e:
            print(e)

    # for friend in user.friends(count = 200):
    #     print(friend.id)
