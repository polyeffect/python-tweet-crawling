import tweepy

API_KEY = 'uFKPfqWUOCxAR1zhvtOCxgfuQ'
API_SECRET = 'uhJdWRE8rm4gFJDsfIQL9EndsAyppMIc2DLHmILdOkROoem6b2'
ACCESS_KEY = '1429214635-iqWhUIQ8fL5RRgm50CIVteX6iIUQvMCxHA49rxV'
ACCESS_SECRET = 'eERw0vcSCCt5W9ktAmVr9uaynMCmPTgEofmpisZ0pW7AO'

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
