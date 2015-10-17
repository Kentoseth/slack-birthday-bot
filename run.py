import json
from datetime import datetime, date
from slackclient import SlackClient

# The 2 lines below work to open the json file and read the json file
# This is where the bot is very bare, as you need to download the list of users on your team
json_file = open('file.json')
json_string = json_file.read()

# This is where the json data is being stored into a dictionary
jdata = json.loads(json_string)

#gets todays date
today = date.today()

#the next few lines are for Slack communication
token = "[TOKEN ID GOES HERE]" # found at https://api.slack.com/#auth)
sc = SlackClient(token)
chan = "#some-channel"

for value in jdata['members']:
	checker = datetime.strptime(value['birthday'], "%Y-%m-%d").date()

	if checker.month == today.month and checker.day == today.day:
		
		#rtm_connect is a command from the slack-client docs
		if sc.rtm_connect():

			#custom message for the birthday person
			message = "Happy Birthday @" + value['name'] + " :birthday: . I am birthday bot :-)"
			
			# The actual command to post the message, which is also printed out to the console
			# The print may be a good way to keep logs :)
			print sc.api_call("chat.postMessage", as_user="true:", channel=chan, text=message)
		
		else:
			print("Connection Failed, invalid token?")
	