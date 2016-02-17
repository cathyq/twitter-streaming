from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import sys
import signal


#consumer key, consumer secret, access token, access secret.
ckey="Auc1c0rIYsqWDQeZ02eN0hX9Q"
csecret="amOy7BHD8UDJNQdHwKk93EXvtwUpSFvzoi4ZRstjvdPssdzPB2"
atoken="153439125-Jgqf3PjXO2d9K6DZEkXGvz5rInIXhNgtUwGD9Ym9"
asecret="OEkNZYQFFmicsQgJ3a5dvPTV416jcwQQkl0vOjGbSTGh6"

class StdOutListener(StreamListener):

    def on_data(self, data):
        print(data)
        return(True)

    def on_error(self, status):
        print status

if __name__ == '__main__':
	# Twitter Streaming API authetification and connection
    l = StdOutListener()
    auth = OAuthHandler(ckey, csecret)
    auth.set_access_token(atoken, asecret)
    stream = Stream(auth, l)

    signal.alarm(30*60)
    # filter Twitter Streams to capture data by the keywords
    stream.filter(track=[sys.argv[1]])






		