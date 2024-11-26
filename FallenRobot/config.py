class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    API_ID = 9303922
    API_HASH = "a17677495aa9ae010b897c2d65146282"

    CASH_API_KEY = "OS6K0SO7XEPZJ0RO"  # Get this value for currency converter from https://www.alphavantage.co/support/#api-key

    DATABASE_URL = ""  # A sql database url from elephantsql.com

    EVENT_LOGS = ()  # Event logs channel to note down important bot level events

    MONGO_DB_URI = "mongodb+srv://sukoon:sukoon@cluster0.fldi6.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"  # Get ths value from cloud.mongodb.com

    # Telegraph link of the image which will be shown at start command.
    START_IMG = "https://te.legra.ph/file/40eb1ed850cdea274693e.jpg"

    SUPPORT_CHAT = "https://t.me/+vzWrtTRKQLRlNDdl"  # Your Telegram support group chat username where your users will go and bother you

    TOKEN = "7904499484:AAEnk5hkCWtAQwvlnH-W6p6M0bYnC5wIgxs"  # Get bot token from @BotFather on Telegram

    TIME_API_KEY = "UH4ASHLF9J0K"  # Get this value from https://timezonedb.com/api

    OWNER_ID = 5174925609 # User id of your telegram account (Must be integer)

    # Optional fields
    BL_CHATS = []  # List of groups that you want blacklisted.
    DRAGONS = []  # User id of sudo users
    DEV_USERS = []  # User id of dev users
    DEMONS = []  # User id of support users
    TIGERS = []  # User id of tiger users
    WOLVES = []  # User id of whitelist users

    ALLOW_CHATS = True
    ALLOW_EXCL = True
    DEL_CMDS = True
    INFOPIC = True
    LOAD = []
    NO_LOAD = []
    STRICT_GBAN = True
    TEMP_DOWNLOAD_DIRECTORY = "./"
    WORKERS = 8


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
