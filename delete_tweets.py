import os
from time import sleep
import twitter

api = twitter.Api(
    consumer_key=os.environ["CONSUMER_KEY"],
    consumer_secret=os.environ["CONSUMER_SECRET"],
    access_token_key=os.environ["ACCESS_TOKEN_KEY"],
    access_token_secret=os.environ["ACCESS_TOKEN_SECRET"],
)

while True:
	try:
		statuses = api.GetUserTimeline(
		    screen_name=os.environ["SCREEN_NAME"], count=1000, trim_user=True
		)
	except Exception as e:
		print(e)
	else:

		for status in statuses[25:]:
		    api.DestroyStatus(status.id)

	sleep(3600)
