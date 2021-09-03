SECRET_KEY = 'django-insecure-ylrongqys7l$0=a&i+0llkdt0hkfyho-efe#@=*6&gsydb6+mo'

DATABASES = {
    'default': {
        'ENGINE': 'mysql.connector.django',
        'NAME': 'music_library_database',
        'USER': 'root',
        'PASSWORD': 'password_123',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'OPTIONS': {
            'autocommit': True
        }
    }
}
