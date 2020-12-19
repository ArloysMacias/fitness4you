#Fitness4You: An E-commerce site
This e-commerce site is was created as a fourth Mile stone project with Code Institute.
It is a web-based store where users can view and purchase fitness and nutritional supplements as a part of their fitness routine. They can search and filter the offered products dynamically Users can interact with the site as a guest, including purchasing or users can create a profile, log in and interact with the site through his or her own account. This also allows the user to keep track of his or her information and purchase history.

##Demo

##Planning Fitness4You
The planning done prior to developing the project can be found in the document below:

************Have this at all as a seperate readme or just incorporate vision statement with the UX?


##UX
The project's target audience is adults who are interested in enhancing their fitness routines or seeking dietary supplements and looking for a simple place where their are able to purchase this without hassle. The rating system on Fitness4You helps customers choose the best products to purchase and the login gives the customer his or her own private place to store the information and history.

###Vision Statement
The e-commerce site presents a wide variety of nutritional supplements for users to easily search and view. Additionally, users can filter products by price and rating to customize their shopping experience. Selected products can be added to the cart and purchased via credit card with out the need to log in. For users who are returning customers and would like to save their information and purchase history there is the option of creating an account and log in.

Feature list:

Product display:
* Products are displayed with a clickable image
* Products information shown:
  * Name
  * Category
  * Brand
  * Price
  * Rating
  * Description

Users can search for products by:
* Name
* Category
* Price
* Rating

Site functionalities:
* Account
  * Users can create an account
  * Users can log in to the site after creating an account
  * Users can log out of the site
  * Users can edit their information once logged in to the site
  * Users can save view their purchase history once logged in to the site.
  
* Shopping cart:
  * Users can add varying quantities of products to the shopping cart
  * Users can delete products from the shopping cart
  * Users can view products in the shopping cart
  
* Check out:
  * Users can pay for the products via credit card and a secure payment option
  
General:
* Users can add to shopping cart and make a purchase with out creating an account
  

###User Stories
As a customer visiting Fitness4You, I want to:
* Understand what the site offers as soon as I enter the Home page.

* Find the site easy and logical to navigate, with buttons and information as I click through the site.

* Be able to search the products I am interested in without hassle.

* Be able to filter products based on price or rating.

* Be able to use the site on my mobile device, for example when I am waiting for the bus.

* Have the option to purchase through a secure payment system.

* Have the option to create an account and login where I can safely store my information and purchases, as well as see my purchase history.

* Be able to review and edit my cart before committing to purchase.

###Design and Colors

The Home page layout is simple and easy to use to give the used the best experience, with key features and services easily accessible. 
The color scheme for this product is dark to create a feeling of danger and excitement with inspiration taken from other similar sites or sites for users interested in sports where nutritional supplements are common. To break up the black, reds and greens where used on key features and buttons to highlight as well as adding to the overall design choice.

###Wireframes


##Features
###Existing Features
####Navbar
Each page on the site has the navbar accessible on the very top of the page. In mobile devices it turns into a hamburger menu in the top left corner of the page.

The following options are presented on the navbar when the user is not logged in:
* Home
* Merchandise (Dropdown)
* Account (Dropdown)
* Shopping cart (with number indication items inside)

The following options are presented on the navbar when the user is logged in:
* Home
* Merchandise (Dropdown)
* Account (Dropdown)
* User name
* Shopping cart (with number indication items inside)

####Home Page
Created with the intent on drawing the interest of the user with bold colors and intriguing images. 

* Buttons that makes it easy for the user to create an account, as it directs him or her to the Login/Register page
* A section showing some of the products available for purchase, with clickable links taking the user to the specific product page
* Footer with contact information to the owner of the site

####Product List
* Product details

Displayed in the product cards are information about each product such as name, brand, price, rating and description. Each product also displays an image which is clickable for an enlarged view.

* Buttons

Each product card has a 'view' button and a 'add-to-cart' button attach to it. Clicking the 'view' button will redirect the user to the specific product page and the 'add-to-cart' button will place the product in the cart, showing a success message when completed.

####Product Page
* Product details

As opposed to the Product list, the Product page displays information about a specific product in a larger view such as name, brand, price, rating and description. Each product also displays an image which is clickable for an enlarged view.

* Buttons

An 'add-to-cart' button will place the product in the cart, showing a success message when completed and a 'continue shopping' button will take the user back to the Product List.

####Register Page
This template is from django's inbuilt allauth.

* Form

The register page allows new users to be added to the database. This consists of a registration form where the user enters the information needed in order to successfully register as a user on the page. When the user clicks '***********' a new user is added into the database.

####Login Page

* Form

When the user click the 'login' button they are redirected to the login page where they have to input user name and password in order to successfully log in. If an incorrect user name or password is entered the page is refreshed, the user is informed and asked to submit again. After successful login the user is redirected to ********* page.

####Logout Page

When the user click on the 'logout' link they are redirected to a confirmation page where the user is asked to confirm if they want to complete the log out. Once logged out the user will be redirected to the ********* page.

####Admin Page


####Cart Page

The Cart page displays the shopping cart with the items the user had added previously. It shows the product quantity, individual price, total price and product description. It also allows the user to change the quantity of individual products as well as deleting a product from the cart. If the quantity of an item is reduced to zero it will automatically be removed from the cart. Buttons to continue shopping or to proceed to checkout are displayed. If the user visits their cart but hasn't added any products, they will be informed that their cart is empty and no checkout button will be visible.

####Checkout Page

The checkout page contains the forms used to insert the user's personal details and to insert payment details. At the bottom of the page is the 'Submit payment' button which will initiate interaction with Stripe API.

####Checkout Successful Page

If checkout is successful the user will be redirected to the *Checkout Successful Page' where they will be informed that the payment went through and a confirmation email has been sent to the email provided in the previous form. The user will also see a "receipt" or a complete list showing the order they just placed.

###Features Left to Implement
Without time constraints it would be ideal to add and implement the following features:

* A choice of different training options and classes, both in groups and with a PT
* The option for users to leave product reviews
*  

## Technologies

The following technologies were used in the development of the application:

##Database Schema

##Site Configuration

##Testing

##Code Validation

## Deployment

##Credits
A million thanks to the best wife EVER!!!!