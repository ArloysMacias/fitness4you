#Fitness4You: An E-commerce site planning

##UX
The project's target audience is adults who are interested in enhancing their fitness routines or seeking dietary supplements and looking for a simple place where their are able to purchase this without hassle. The rating system on Fitness4You helps customers choose the best products to purchase and the login gives the customer his or her own private place to store the information and history.

###Vision Statement
The e-commerce site presents a wide variety of nutritional supplements for users to easily search and view. Additionally, users can filter products by price and rating to customize their shopping experience. Selected products can be added to the cart and purchased via credit card without the need to log in. For users who are returning customers and would like to save their information and purchase history there is the option of creating an account and log in. Registration also comes with the added benefit of getting access to exclusive products.

####Feature list:

#####Product display:
* Products are displayed with a clickable image showing the description
* Products information shown:
  * Name
  * Category
  * Brand
  * Price
  * Rating
  * Description

#####Users can filter for products by:
* Name
* Category
* Price
* Rating

#####Site functionalities:
* Account
  * Users can create an account
  * Users can log in to the site after creating an account
  * Users can log out of the site
  * Users can edit their information once logged in to the site
  * Users can save and view their purchase history once logged in to the site.
  
* Shopping cart:
  * Users can add varying quantities of products to the shopping cart
  * Users can delete products from the shopping cart
  * Users can view products in the shopping cart
  
* Check out:
  * Users can pay for the products via credit card and a secure payment option
  
#####General:
* Users can add to shopping cart and make a purchase without creating an account
  

###User Stories
As a customer visiting Fitness4You, I want to:
* Understand what the site offers as soon as I enter the Home page.

* Find the site easy and logical to navigate, with buttons and information as I click through the site.

* Be able to search the products I am interested in without hassle.

* Be able to filter products based on price, rating, brand and category.

* Be able to use the site on my mobile device, for example when I am waiting for the bus.

* Have the option to purchase through a secure payment system.

* Have the option to create an account and login where I can safely store my information and purchases, as well as see my purchase history.

* Be able to review and edit my cart before committing to purchase.

###Design and Colors

The Home page layout is simple and easy to use to give the used the best experience, with key features and services easily accessible. 
The color scheme for this product is dark to create a feeling of danger and excitement with inspiration taken from other similar sites or sites for users interested in sports where nutritional supplements are common. To break up the black, reds and greens where used on key features and buttons to highlight as well as adding to the overall design choice.

###Wireframes














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

| No | Name                                                            | Description                                                                                                                                                                                                                                                           | Solutions                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|----|-----------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1  | Loading files                                                   | Files in the media folder do not load properly                                                                                                                                                                                                                        | I included the following line of code in the setting.py file   ...  ...  ...   ...  'django.contrib.messages.context_processors.messages',  'django.template.context_processors.media', ],  ‘django.template.context_processors.media’,  in your settings.py  ... ... ...                                                                                                                                                                                                                                                                                                                     |
| 2  | I can't login to the admin section                              |                                                                                                                                                                                                                                                                       | I deleted the 3 points in the following line of code       space             ... ... ... ... AUTHENTICATION_BACKENDS = [ # Needed to login by username in Django admin, regardless of   allauth  'django.contrib.auth.backends.ModelBackend', # `allauth` specific authentication methods, such as login by e-mail 'allauth.account.auth_backends.AuthenticationBackend', ... ... ... ]                                                                                                                                                                                                       |
| 3  | Link in materializecss checkboxes                               | I couldn't figure out how to capture the event (onchange or onclick) in a materializecss checkbox and send the url to the view                                                                                                                                        | I changed the element and decided to develop the filters with a collapsible and with radio buttons                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| 4  | Webhook not working                                             | When doing the webhook, because I am using intellij idea (and I am working locally) I am not able to obtain the address of the webhook to pass it to stripe                                                                                                           | I look for a tool that allows me to expose a my local development server to the Internet https://www.pubnub.com/learn/glossary/what-is-ngrok/ ngrok https://ngrok.com/  1. The setting.py allowed the address provided by Ngrok: ALLOWED_HOSTS = ['2a0d946fed40.ngrok.io'] 2. Copy the address in Stripe / Webhooks / Webhooks Data: http://2a0d946fed40.ngrok.io/checkout/wh/ 3. Write the Stripe WebHooks key for the local development environment: STRIPE_WH_SECRET = 'xxxxxxxxxxxxxxxxxxxxxxxxxxx'.  (Should not be in environment STRIPE_WH_SECRET = os.getenv('STRIPE_WH_SECRET', '')) |
| 5  | Pagination and drop-down from materialize cancel each other out | When I enter this jquery version: <script src="https://ajax.googleapis.com/ajax/libs/jquery/2.2.2/jquery.min.js"></script> The pagination works but the drop-down from materialize does not work.   When I delete it the drop-down works but the pagination does not. | In jQuery 3 size() was deprecated and completely removed The norm is to use length property instead. So I changed the function size to length in children.length from :http://cdn.rawgit.com/pinzon1992/materialize_table_pagination/f9a8478f/js/pagination.js                                                                                                                                                                                                                                                                                                                                |

#### Model:

![Data Base](https://github.com/ArloysMacias/fitness4you/blob/master/media/DataBaseDiagram/DataBase.png)

