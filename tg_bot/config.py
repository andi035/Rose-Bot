class Config(object):
    LOGGER = True

    # REQUIRED
    API_KEY = "6222408835:AAGxtk0YfVlGzB96Cwrpv22Qs2FRGwkqAYo"
    OWNER_ID = "5147282548"  # If you dont know, run the bot and do /id in your private chat with it
    OWNER_USERNAME = "https://t.me/Andreas035"


class Production(Config):
    LOGGER = False


class Development(Config):
    LOGGER = True
