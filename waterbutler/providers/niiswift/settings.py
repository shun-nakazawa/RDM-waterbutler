from waterbutler import settings

config = settings.child('NIISWIFT_PROVIDER_CONFIG')


TEMP_URL_SECS = int(config.get('TEMP_URL_SECS', 100))
