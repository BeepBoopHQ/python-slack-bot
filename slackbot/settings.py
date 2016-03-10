import os
import sys

DEBUG = False

PLUGINS = [
    'slackbot.plugins',
]


try:
    # Raises a KeyError if SLACK_TOKEN environment variable is missing
    API_TOKEN = os.environ['SLACK_TOKEN']
except:
    # Alternatively, place slack token in the source code
    # API_TOKEN = '###token###'
    print 'SLACK_TOKEN missing'
    sys.exit(1)

'''
If you use Slack Web API to send messages (with send_webapi() or reply_webapi()),
you can customize the bot logo by providing Icon or Emoji.
If you use Slack RTM API to send messages (with send() or reply()),
the used icon comes from bot settings and Icon or Emoji has no effect.
'''
# BOT_ICON = 'http://lorempixel.com/64/64/abstract/7/'
# BOT_EMOJI = ':godmode:'

for key in os.environ:
    if key[:9] == 'SLACKBOT_':
        name = key[9:]
        globals()[name] = os.environ[key]

try:
    from slackbot_settings import *
except ImportError:
    try:
        from local_settings import *
    except ImportError:
        pass
