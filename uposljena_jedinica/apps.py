from django.apps import AppConfig


class UposljenaJedinicaConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'  # Sets default field type for auto-incrementing primary keys
    name = 'uposljena_jedinica'  # The name of the app, matching the folder name