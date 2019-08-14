import os
import time
import twitter

api = twitter.Api(
    consumer_key=os.environ["CONSUMER_KEY"],
    consumer_secret=os.environ["CONSUMER_SECRET"],
    access_token_key=os.environ["ACCESS_TOKEN_KEY"],
    access_token_secret=os.environ["ACCESS_TOKEN_SECRET"],
)

user_id = api.GetUser(screen_name=os.environ["SCREEN_NAME"]).id_str


def bot():
    for tweet in api.GetStreamFilter(follow=[user_id]):
        statuses = api.GetUserTimeline(user_id=user_id, count=1000, trim_user=True)

        for status in statuses[5:]:
            api.DestroyStatus(status.id)
            print(status)


while True:
    try:
        bot()
    except Exception as e:
        print(e)
        time.sleep(5)
