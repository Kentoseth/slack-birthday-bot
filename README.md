# slack-birthday-bot

A Slack bot (written in Python) that sends out birthday messages to people in your channels/team.

This project is self-contained, so if you follow the instructions, it should work out-of-the-box for you.

----------

This tool has a dependency on the Slack Python-client.

The client can be installed using:

```
pip install slackclient
```

More info can be found here: [link](https://github.com/slackhq/python-slackclient)

----------

##Using the program itself

In order to make this program work, you need to make 1 file-edit and do a couple of other manual things (with some these tasks capable of being automated).

###Adding your Slack token

In the `run.py` file, on this line:

```
token = "[TOKEN ID GOES HERE]" # found at https://api.slack.com/#auth)  
```

You need to get your specific token and add it so that you get something like: `token = "dasdafe1214r51"`

###Fetching user data(possible to automate)

In the `run.py` file, there is a line: 

```
json_file = open('file.json')
```

What this is, is the JSON representation of your team-members, as available from the Slack API. Making 1 single GET request should fetch the list for you. My needs were small, therefore I did not need to update the list frequently (and frankly did not want to make too many API calls to Slack anyway)

If you need to keep the list updated frequently, you can probably add it to the CRON job I specify below.

###Running the bot

Running a bot means that the bot needs to be 'alive' for at least 2-60 minutes a day(depending on how big your Slack team-list is) to post birthday messages.

What I suggest (as the simplest way) is to run the Python file as a CRON job once a day.

You can run it on your local machine or on a server.

You can also add the 'GET' request as another CRON job, making sure to save the output as `file.json` in the same directory as the `run.py` file.

> (Possible)Q: Do I need to run the the file multiple times a day to update each person on their birthday(in case there is more than 1 person sharing a birthday)?

> A: No, running the script once will send each person in your Slack team a birthday message (on the same day)

----------