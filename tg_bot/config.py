if not __name__.endswith("sample_config"):
    import sys
    print("The README is there to be read. Extend this sample config to a config file, don't just rename and change "
          "values here. Doing that WILL backfire on you.\nBot quitting.", file=sys.stderr)
    quit(1)


# Create a new config.py file in same dir and import, then extend this class.
class Config(object):
    LOGGER = True

    # REQUIRED
    API_KEY = "6222408835:AAGxtk0YfVlGzB96Cwrpv22Qs2FRGwkqAYo"
    OWNER_ID = "5147282548"  # If you dont know, run the bot and do /id in your private chat with it
    OWNER_USERNAME = "https://t.me/Andreas035"

    # RECOMMENDED
    SQLALCHEMY_DATABASE_URI = 'sqldbtype://username:pw@hostname:port/db_name'  # needed for any database modules
    MESSAGE_DUMP = None  # needed to make sure 'save from' messages persist
    LOAD = []
    NO_LOAD = ['translation', 'rss']
    WEBHOOK = False
    URL = None

class Production(Config):
    LOGGER = False


class Development(Config):
    LOGGER = True
class Config(object):
    LOGGER = True

    
