# fitness4you

####Error:
Files in the media folder do not load properly

####Solution:
Include the following line of code in the setting.py file

...
...
...
...
'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',
            ],

‘django.template.context_processors.media’, in your settings.py


####Error:

AttributeError at /admin/login/
'ellipsis' object has no attribute 'rsplit'
Request Method:	GET
Request URL:	http://127.0.0.1:8000/admin/login/?next=/admin/
Django Version:	3.0.1
Exception Type:	AttributeError
Exception Value:	
'ellipsis' object has no attribute 'rsplit'
Exception Location:	/Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/site-packages/django/utils/module_loading.py in import_string, line 13
Python Executable:	/usr/local/bin/python3.8
Python Version:	3.8.5
Python Path:	
['/Users/arloys.rojas/Code_Institute_Projects/fitness4you',
 '/Users/arloys.rojas/Code_Institute_Projects/fitness4you',
 '/Users/arloys.rojas/Library/Application '
 'Support/IntelliJIdea2019.3/python/helpers/pycharm_display',
 '/Library/Frameworks/Python.framework/Versions/3.8/lib/python38.zip',
 '/Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8',
 '/Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/lib-dynload',
 '/Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/site-packages',
 '/Users/arloys.rojas/Library/Application '
 'Support/IntelliJIdea2019.3/python/helpers/pycharm_matplotlib_backend']
Server time:	Tue, 17 Nov 2020 00:48:55 +0000


####Solution:
remove the 3 points in the following line of code

AUTHENTICATION_BACKENDS = [
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
    ...
]

####Data Base:
![Data Base](https://github.com/ArloysMacias/fitness4you/blob/master/media/DataBaseDiagram/DataBase.png)

