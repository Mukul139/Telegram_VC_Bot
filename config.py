HEROKU = True  # NOTE Make it false if you're not deploying on heroku.

# NOTE these values are for heroku & Docker.
if HEROKU:
    from os import environ

    from dotenv import load_dotenv

    load_dotenv()  # take environment variables from .env.
    API_ID = int(environ["API_ID"])
    API_HASH = environ["API_HASH"]
    SESSION_STRING = environ[
        "BQCxf1d08fnKjBHj2f6pln7Zwlcjr5KOGpRVQei2XJFkvONPMO3ufdUHQoQXQCQwRcP9mteqLSqLcNVrqlJ-IYsCKvEPlmgGnBNeXjVWfuwWKgwXXpAx7JGxhPvr4uA4HZqd7YZjd3Rwksc1Q9T7OmStyHDlYH--T9ubVilX1_N5qtaPOVrxqCFPa6gc0CFEIguswJShx2CPDprrHohMil8f1oznpcqazzHHFYjdit-u99GrLU_CZc12TgyZi9VbjkXqgBBiDmFfHmUw7ohcyMDxOUy0NTKQh8GbqJK2YTuGoP3Zp3PNjwb2hmX5AodE-dJ0tpgHoYxaS2tShte-iW4lRMZJ4QE"
    ]  # Check Readme for session
    ARQ_API_KEY = environ["ARQ_API_KEY"]
    CHAT_ID = int(environ["CHAT_ID"])
    DEFAULT_SERVICE = environ.get("DEFAULT_SERVICE") or "youtube"
    BITRATE = int(environ["BITRATE"])

# NOTE Fill this if you are not deploying on heroku.
if not HEROKU:
    API_ID = 14371
    API_HASH = "e46b6c854d2bf58a0"
    ARQ_API_KEY = "Get this from @ARQRobot"
    CHAT_ID = -100546355432
    DEFAULT_SERVICE = "saavn"  # Must be one of "youtube"/"saavn"
    BITRATE = 512 # Must be 512/320

# don't make changes below this line
ARQ_API = "https://arq.hamker.in"
