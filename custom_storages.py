from django.conf import settings
# from storages.backends.s3boto3 import S3Boto3Storage
from storages.backends.azure_storage import AzureStorage


# class StaticStorage(S3Boto3Storage):
#     location = settings.STATICFILES_LOCATION
#
# class MediaStorage(S3Boto3Storage):
#     location = settings.MEDIAFILES_LOCATION

class PublicAzureStorage(AzureStorage):
    account_name = 'fpvsiteuser'
    account_key = '+R8UWrbaOgwBXv21viakRtw7QYOurasUEKMJTVtdbyhp0+ZtzbtGvrIxKrA6Wmgb7ktg29AO8HriqeTSrNqm+g=='
    azure_container = 'fpvsitecontainer'
    expiration_secs = None