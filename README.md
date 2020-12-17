# fitness4you

###Imported

####[Materialize (0.100.2)](http://archives.materializecss.com/0.100.2/)
Materialize is a modern responsive CSS framework based on Material Design by Google.

####[Bootstrap](https://getbootstrap.com/)
Bootstrap is a free and open-source CSS framework directed at responsive, mobile-first front-end web development. It contains CSS- and (optionally) JavaScript-based design templates for typography, forms, buttons, navigation, and other interface components.

####[noUislider](https://refreshless.com/nouislider/)
NoUiSlider is a lightweight range slider with multi-touch support and a ton of features. It supports non-linear ranges, requires no external dependencies, has keyboard support, and it works great in responsive designs

####[Wnumb](https://refreshless.com/wnumb/)
WNumb is a formatting library with a dead-simple interface. It has two methods: to and from. Licensed MIT, so free for personal and commercial use.

####[Django-Crispy-Forms](https://django-crispy-forms.readthedocs.io/en/latest/index.html)django-crispy-forms)
Is a pluggable Django app that helps to write DRY forms by providing additional capability to configure and control the rendered HTML.

####[Gunicorn](https://en.wikipedia.org/wiki/Gunicorn) 
Green Unicorn is a Python Web Server Gateway Interface (WSGI) HTTP server. It is a pre-fork worker model, ported from Ruby's Unicorn project.he Gunicorn server is broadly compatible with a number of web frameworks, simply implemented, light on server resources and fairly fast.

####[Pillow](https://en.wikipedia.org/wiki/Python_Imaging_Library)
Python Imaging Library (abbreviated as PIL) (in newer versions known as Pillow) is a free and open-source additional library for the Python programming language that adds support for opening, manipulating, and saving many different image file formats

####[Requests](https://www.django-rest-framework.org/api-guide/requests/)
REST framework's Request class extends the standard HttpRequest, adding support for REST framework's flexible request parsing and request authentication.

####[Stripe](https://stripe.com/es-se)
Payment processing software and application programming interfaces (APIs) for e-commerce websites and mobile applications.

####[Django-filter](https://django-filter.readthedocs.io/en/stable/)
Django-filter is a generic, reusable application to alleviate writing some of the more mundane bits of view code. Specifically, it allows users to filter down a queryset based on a model’s fields, displaying the form to let them do this.


###Main problems and their solutions

| No | Name                               | Description                                                                                                                                                 | Solutions                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|----|------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1  | Loading files                      | Files in the media folder do not load properly                                                                                                              | I included the following line of code in the setting.py file   ...  ...  ...   ...  'django.contrib.messages.context_processors.messages',  'django.template.context_processors.media', ],  ‘django.template.context_processors.media’,  in your settings.py  ... ... ...                                                                                                                                                                                                                                                                                                                     |
| 2  | I can't login to the admin section |                                                                                                                                                             | I deleted the 3 points in the following line of code       space             ... ... ... ... AUTHENTICATION_BACKENDS = [ # Needed to login by username in Django admin, regardless of   allauth  'django.contrib.auth.backends.ModelBackend', # `allauth` specific authentication methods, such as login by e-mail 'allauth.account.auth_backends.AuthenticationBackend', ... ... ... ]                                                                                                                                                                                                       |
| 3  | Link in materializecss checkboxes  | I couldn't figure out how to capture the event (onchange or onclick) in a materializecss checkbox and send the url to the view                              | I changed the element and decided to develop the filters with a collapsible and with radio buttons                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| 4  | Webhook not working                | When I was developing the webhooks, because I was working locally (Using Intellij IDEA) I was not able to obtain the address of the webhook to pass it to stripe | I look for a tool that allows me to expose a my local development server to the Internet https://www.pubnub.com/learn/glossary/what-is-ngrok/ ngrok https://ngrok.com/  1. The setting.py allowed the address provided by Ngrok: ALLOWED_HOSTS = ['2a0d946fed40.ngrok.io'] 2. Copy the address in Stripe / Webhooks / Webhooks Data: http://2a0d946fed40.ngrok.io/checkout/wh/ 3. Write the Stripe WebHooks key for the local development environment: STRIPE_WH_SECRET = 'xxxxxxxxxxxxxxxxxxxxxxxxxxx'.  (Should not be in environment STRIPE_WH_SECRET = os.getenv('STRIPE_WH_SECRET', '')) |


#### Model:

![Data Base](https://github.com/ArloysMacias/fitness4you/blob/master/media/DataBaseDiagram/DataBase.png)

