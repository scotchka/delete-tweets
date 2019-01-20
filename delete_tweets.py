import os
import twitter

api = twitter.Api(
    consumer_key=os.environ["CONSUMER_KEY"],
    consumer_secret=os.environ["CONSUMER_SECRET"],
    access_token_key=os.environ["ACCESS_TOKEN_KEY"],
    access_token_secret=os.environ["ACCESS_TOKEN_SECRET"],
)

statuses = api.GetUserTimeline(
    screen_name=os.environ["SCREEN_NAME"], count=1000, trim_user=True
)

for status in statuses[25:]:
    api.DestroyStatus(status.id)
