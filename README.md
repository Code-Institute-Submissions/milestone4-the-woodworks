# Milestone 4 - The Woodworks

**DISCLAIMER: This project is for educational purposes only, no materials/files are intended for any commercial use. In this document all sources will be credited.**

![AmiResponsive](https://ms4-the-woodworks.s3.eu-west-2.amazonaws.com/media/images/AmI.JPG)


- [Milestone 4 - The Woodworks](#milestone-4---the-woodworks)
    + [The journey of developing The Woodworks](#the-journey-of-developing-the-woodworks)
  * [UX](#ux)
    + [User stories](#user-stories)
    + [Model design](#model-design)
      - [Product](#product)
      - [Reviews](#reviews)
      - [Poll](#poll)
    + [Color scheme](#color-scheme)
    + [Naming scheme](#naming-scheme)
    + [Planned pages](#planned-pages)
  * [Features](#features)
    + [Existing Features](#existing-features)
      - [Consistent features across all pages](#consistent-features-across-all-pages)
      - [Store / Landing page](#store---landing-page)
      - [Cart](#cart)
      - [Checkout](#checkout)
      - [Checkout succes page](#checkout-succes-page)
      - [Login/registration/logout pages](#login-registration-logout-pages)
      - [Review page](#review-page)
      - [Poll/vote page](#poll-vote-page)
    + [Defensive design](#defensive-design)
    + [Features left to implement](#features-left-to-implement)
  * [Technologies used](#technologies-used)
    + [Framework & Extensions](#framework---extensions)
    + [Tools](#tools)
    + [APIs](#apis)
    + [Validators](#validators)
  * [Testing](#testing)
    + [Validators](#validators-1)
        * [HTML](#html)
        * [CSS](#css)
        * [Javascript](#javascript)
        * [Python](#python)
    + [User tests](#user-tests)
      - [Display, layout & responsiveness](#display--layout---responsiveness)
      - [Navigation header](#navigation-header)
      - [Authenication proces.](#authenication-proces)
      - [Store page](#store-page)
      - [Reviews page](#reviews-page)
      - [Vote page](#vote-page)
      - [Cart page](#cart-page)
      - [Checkout page](#checkout-page)
      - [Checkout Succes page.](#checkout-succes-page)
      - [General](#general)
    + [Bugs left to be solved.](#bugs-left-to-be-solved)
    + [Interesting bugs/issues solved](#interesting-bugs-issues-solved)
    + [External testers](#external-testers)
  * [Deployement](#deployement)
    + [Local deployement](#local-deployement)
  * [Credits](#credits)
  * [Acknowledgements](#acknowledgements)

<small><i><a href='http://ecotrust-canada.github.io/markdown-toc/'>Table of contents generated with markdown-toc</a></i></small>

# Milestone 4 - The Woodworks

**The deployed site can be found [here](https://codewouter-the-woodworks.herokuapp.com/)**

**NOTE: To use the creditcard payment functionality one should use 4242 4242 4242 4242 as a creditcard number.**

The milestone 4 project will be a website to showcase content I learned to develop in the last part of the Code Institute's Full stack developer bootcamp. It will be a Django based full stack website. Since I am on an extremely tight schedule I will build a minimal viable product first and expand on that if time permits. 

I chose to build a small e-commerce site for a dear friend of mine who will be starting a training in furniture woodworking and might be selling his creations in the future. The site I will build is a showcase to see how it might work.

As I have been working through the course material I experienced a big overload of information, so I needed to start building my project. In my past experience I found that worked a lot better than just working through the course material. Because of the sheer size of the possibities I will not be designing the whole site beforehand. General mockups and the look and feel can be designed early in the process, but all functionality and features will be chosen and developed as I go along.

### The journey of developing The Woodworks
I started development using very simple apps to push through the content fast so I could get the major roadblocks out of the way. I needed to be sure that I had the site working before complicating everything with styling, more products, etc. So with this in mind I build the apps and views (store, cart and add to cart functionality) necessary to get to the checkout page, then to the checkout itself and succesfull payment functionality using stripe. Orders were being entered into the database as well at this point. I also switched quite early to having my mediafiles being pulled from AWS S3 instead of local content, to be sure that was working as well. With all that finished I did an early deployement to heroku.

After that I went and build up the site for real, adding the review app, the poll app and all styling and true layout. Adding more items to be sold, some items for the poll and some sample reviews. Adding more styling and some Javascript to spice things up.

## UX

The following features need to be present at a minimum:

- The site needs to be clear and responsive.
- A landing page which will display purchaseable products
- A navbar including a shopping cart and a way to differentiate between a logged on/off user.
- A way to add products to the shopping cart.
- A login system using e-mail confirmation.
- Two additional apps not used in the Boutique Ado mini-project of the course material:
  1. A review page where each product can be reviewed.
  2. Either a contact form, or a page with a poll on what furniture product to develop next.
- A checkout page with fields for an address to send the product(s) to.
- A working payment system using Stripe and it's testing facilities.

### User stories

As a user that is not logged in:

- I want to view products on offer
- I want to look at reviews
- I want to look at the poll for the next product to be developed.
- I want to register for a new account
- I want login if I already have an account
- I want to add a product to my shopping cart
- I want to be able to see the contents of my shopping cart and adjust it if necessary.

As a user that is logged in:

- I want to add a review to a product
- I want to add a product to my shopping cart
- I want to see the contents of my shopping cart
- I want to checkout my purchases and pay for them
- I want to vote for the next product to be developed.

### Model design

#### Product
The products model will be several types of furniture, in the database design the model will have the following fields:

- product_id (primary key)
- name (string)
- description (string)
- price (integer)
- construction time (integer representing weeks)
- image (file)

#### Reviews
The review model will add reviews to products and use product_id as a foreign key.

- review_id (primary key)
- product_id (foreign key)
- review_text (string)

#### Poll
The poll model will contain a product type and votes cast per type. Time permitting it will be linked to a user account so a user can only vote once.

- product_type_id
- product_type (string)
- votes (integer)

A seperate model for the poll app was implemented during development will be present to keep track of who has voted. These are identified by their emaildres.

- Voters/voted (contains only emailadresses)

The database model can be viewed [here](https://github.com/codewouter/milestone4-the-woodworks/blob/master/mockups/ms4-db-model.pdf)

### Color scheme

Using https://coolors.co/ I picked a scheme that had a lot of green in it and some nice contrast giving it a bit of a 'nature' feel.

![Colorscheme image](https://ms4-the-woodworks.s3.eu-west-2.amazonaws.com/media/images/Colorpalette500x.png)

Colors from left to right:

- 606C38
- 283618
- FEFAE0
- DDA15E
- BC6C25

### Naming scheme

- HTML/CSS: using dashes, eg. toggle-info-button
- Javascript: camelcase, eg. toggleElementView
- Python: underscores. eg. view_reviews

### Planned pages

- Login/ registration page
    * Self explanetory. Will be provided by Django's allauth app. Some sytling might be necessary.

**Pages for the flow of shopping. Selecting, ordering, checkout, payment, confirmation.**

- Landing/store page
    * The landing is page will also be the store page. The site will contain the products that can be purchased. Here they can be added to the shopping cart. A maximum of 5 items each to keep users from ordering 100's of items. It will contain a button to go to the reviews section of the relevant product. Details of the product will be:
	    * picture of product
	    * name
	    * description (should be hidden on mobile, with an option to show it (button))
	    * price
	    * construction time

- Shopping cart page
    * This page will give an overview of the contents of the shopping cart, including total price and construtcion time. Here the user can adjust the cart's content and ultimately got to checkout. To go to checkout the user needs to be logged in.

- Checkout page
    * The checkout page will only show if the user is logged on. Here the user is shown a condensed view of the carts contents and the grand total to be payout. A form to fill out all the user's details, including payment details, is loaded. After that the user is given an option (button) to complete the order.

- Checkout succes page
    * A simple page to show that the order has followed through. If time permits it will show the order, payment and send an email for confirmation.

**Other pages**

- Review page
    * A page that will show reviews entered by users for a product. If logged in, the user can add reviews.

- Poll page
    * A poll will be shown here that asks to vote on the product to be developed next by the woodworks. If logged on the user can vote, if not, the user can view the results up to now.

Mockups of several of the pages can be viewed [here](https://github.com/codewouter/milestone4-the-woodworks/blob/master/mockups/the-woodworkds-mockups.pdf)

I have not made mockups of all pages as some were developed 'on the fly' during developement. As mentioned earlier, I went with exremely simplistic design to get all the way to a working deployed site. When that was finished I started polishing what was there and never felt I needed to build mockups first. The general design of the site was quite clear from the mockups I did make.

## Features

### Existing Features

#### Consistent features across all pages

- A navbar to navigate around the site. The links for Store, Vote and Cart are always present. When logged in there is a logout option. If not, links for register and login are present. The cart has a small addition showing the number of products in the cart if any are present. On the left the name of the shop is present and acts as a 'home' link. On small viewports all links will be replaced with a hamburger menu which will slide open to reveal all links.
- 
- A simple footer to indicate the bottom of the page, containing a copyright mark.

#### Store / Landing page
As per design these are one and the same. On the page all available products are shown through the use of cards. Each cards contains a picture, name of the item and a description in the cards main field. Here also is a button to go to the reviews for this project. On small viewports no description is shown, a button can be pressed to toggle between the description being shown or hidden. This has been implemented to not clutter the viewport too much. The footer of the card shows the following:

* The price 
* Construction time, 
* Number of items to be added to the cart
* Button to add to the cart 
* Maximum of items that can be added to the cart.

#### Cart
The cart page shows the content of the shopping cart. This has again been done with product cards. The content is condensed somewhat to give a clear overview. In the card the user can adjust the amount on order. At the bottom a summary containing total price and total construction time is shown. If the user agrees the checkout button can be pressed to go to the checkout screen. When the user is not logged on but trying to press the button, it will be disabled and a message show to ask the user to log on.

#### Checkout
The checkout page cannot be entered with being logged (typing the url will fail too). It shows an even more condensed view of the shopping cart's contents with the total price. The user is asked to fill out a form with the user's personal details and payment information. If all is valid, the user can use the button 'complete order' for secure checkout through Stripe's functionality.

#### Checkout succes page
A simple page showing a confirmation message that the order has been received. If time permits, this will be extended.

#### Login/registration/logout pages
These are directly implemented from allauth. All needed functionality is present and has been tested. Some styling and aligning has been done.

#### Review page
The review page will show the product with the reviews for that product (if any). If the user is logged on, the form to submit one's own review is displayed, else it is hidden. The reviews written are shown with the reviewer, review text and the date/time the review was submitted.

#### Poll/vote page
Here the user is able to see the results up to that moment of the votes on the question what should be developed next. A number of options is present with the number of votes for each option. A progressbar is present per product to show the relative number of votes. The bars fill up to the percentage of total votes the current option has. These are updates at every pageload. The total number of votes is shown too. The user can only vote once (tied to the user's emailadress). The buttons to vote are hidden when the user is not logged on, or has already voted. An appriorate message is shown to alert the user of this.

### Defensive design
Certain measure were taken to prevent users from making mistakes or malicious actions.

- General form validation
- Stripe has its own security system in place. I took nearly every part of code concerning stripe from the Boutique Ado project of the Code Institute.
- Several get_object_or_404 instances in the views.
- The checkout button is disabled when the user is not logged on.
- The checkout view has @login_required tagged.(so no access when typing the url of the checkout page in the addressbar)
- On the vote and review page, the relevant content to submit a vote or review are hidden when the user is not logged on.
- If a user enters empty values in the quantity boxes, the cart view in both functions will catch this and just return to the page.
- As a measure to prevent users from putting to0 many products in the cart, the user is only able to have a maximum of 5 items of each product in the cart. This has been implemented in several ways:
	+ Form validation only allows 1 to 5 in the quantity field on the store page and 0 to 5 on the cart page.
	+ In the addtocart view, no values except 1 to 5 are allowed (in case someone disables the form validation)
	+ In the adjustcart view, no vlaues except 0 to 5 are allowed. (in case someone disables the form validation)

### Features left to implement
Now that I know what Django is capable of there is so much more I would like to add. However most are beyond the scope and time allotted for this project.

Things that I would have liked very much to add but were left because of time constraints.

- Sorting of products lists etc.
- Smooth transistions hidden/show text on storepage.
- Change page titles (Headers needs work)
- Enlarged pictures when clicked on
- Webhook handling (the webhooks are received (tests from stripe succesful))
- Order overview on checkout succes page.
- Better footer placement, have it stable at the bottom of the viewport if small enough
- Order confirmation through email
- Seperate landing page.
- Superuser login to be able to add/remove products etc
- Persisting cart tied to account
- Timestap on orders
- Make address 2 field on checkout not required

## Technologies used
**Partly taken from https://raw.githubusercontent.com/maliahavlicek/ms4_challenger/master/README.md**


### Framework & Extensions

- [dj-database-url](https://pypi.org/project/dj-database-url/) - allows use of environment variable for database connections
- [bootstrap 4](https://getbootstrap.com/docs/4.0/getting-started/introduction/) - a mobile friendly CSS framework based on a responsive grid system.
- [django-forms-bootstrap](https://pypi.org/project/django-forms-bootstrap/) - allows further customization of bootstrap forms within Django framework
- [stripe](https://pypi.org/project/stripe/) - A python library to talk to Stripe's API
- [boto3](https://pypi.org/project/boto3/)-  allows Python to talk to AWS SDK so you can store data in S3 buckets 
- [django-storages](https://django-storages.readthedocs.io/en/latest/) a collection of custom storage backends with django to work with boto3 and AWS S3.
- [gunicorn](https://pypi.org/project/gunicorn/) - Python WSGI HTTP Server for UNIX so you can host your application
- [pillow](https://pillow.readthedocs.io/en/stable/) -Python Imaging Library to help store imagery into a database
- [psycopg2](https://www.psycopg.org/docs/) - PostgreSQL database adapter for the Python
- [pytz](https://pypi.org/project/pytz/) - world timezone calculations
- [allauth](https://django-allauth.readthedocs.io/en/latest/index.html) - Takes care of nearly all user authorization functionality.
- [Font Awesome](https://fontawesome.com/) - used for various icons.


### Tools

- [github](https://github.com/) - used for version control of project files and branching out to try different things without adversely affecting a functional set of code
- [balsamiq](https://balsamiq.com/) - used to create professional looking wire frames.
- [mardown table of contents generator](http://ecotrust-canada.github.io/markdown-toc/) - Used to generate the README table of contents.
- [heroku](https://www.heroku.com/) - runs the ms4  application in the cloud
- [pip](https://pip.pypa.io/en/stable/installing/) - used to install python extensions for this project
- [AmIresponsive](http://ami.responsivedesign.is/#) - Used to create Am I responsive picture.
- [Color Picker](https://coolors.co/) - Used to determine general colors used in the project.
- [Gitpod](https://www.gitpod.io/) - As main IDE

### APIs

- [AWS S3 Bucket](https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingBucket.html) - allows seamless uploading of user files to cloud storage using application credentials
- [stripe](https://stripe.com/) - payment platform to validate and accept credit card payments securely

### Validators

- [W3C Markup Validation Service](https://validator.w3.org/) - used to validate HTML and CSS code;
- [JSHint](https://jshint.com/) - used to validate JavaScript code;
- [PEP8 online](http://pep8online.com/) - validate Python code;

## Testing

### Validators

##### HTML
All pages were checked with W3C Markup Validation Service and no errors were found:

- Store: https://codewouter-the-woodworks.herokuapp.com/
- Signup: https://codewouter-the-woodworks.herokuapp.com/accounts/signup/
- Login: https://codewouter-the-woodworks.herokuapp.com/accounts/login/
- Vote: https://codewouter-the-woodworks.herokuapp.com/poll/
- Cart (empty & filled): https://codewouter-the-woodworks.herokuapp.com/cart/
- Reviews: https://codewouter-the-woodworks.herokuapp.com/reviews/7/
- Checkout: https://codewouter-the-woodworks.herokuapp.com/checkout/
- Checkout Success: https://codewouter-the-woodworks.herokuapp.com/checkout/checkout_success/

##### CSS
- The main.css file was checked using W3C Markup Validation Service.
- The CSS file validates as CSS level 3 + SVG. No errors found.

##### Javascript
All javascript files were validated using jshint.com. No critical errors found. Let and const variables are flagged as ES6 and some functions are called unused variables because they are called from outside the script file. After conferring with Tutor support they can be ignored.

##### Python
All python files in all apps were checked using PEP8Online and no errors were found except settings.py. Some lines are too long according to the validator, those have been commented on in the code. After conferring with Tutor support they can be ignored.

### User tests

#### Display, layout & responsiveness
All testing was done continuously during development using Chrome devtools settings set to:

* Laptop (1366 x 768)
* Ipad (stock)
* Galaxy S5 (stok)

And using these real devices:

* Fullscreen monitor (1920x1080)
* Samsung A7
* Samsung A5

No disfunctionality was found in final testing.

#### Navigation header

- The name of the company 'The Woodworks' can be clicked as a 'home' link.
- All links respond correctly.
- When the user is logged off, the logout link is not shown, login and register are shown.
- When the user is logged on, the login and register links are hidden and only the logout link is shown. 
- The links Store, Vote and Cart are always shown.
- When at least one item is in the cart, a small yellow dot shows the total number of items in the cart.
- On small viewports the links are hidden and put in a hamburger menu. All links are present in the menu, the same as described earlier. 

#### Authenication proces.

- The registration functionality was tested using multiple accounts
- The login functionality was tested using multiple accounts
- The logout functionality was tested using multiple accounts
- The password reset functionality was tested using multiple accounts

#### Store page

- On small viewports the description is hidden on pageload and the 'toggle info' button shows/hides the text.
- The reviews button responds well and loads the relevant page
- Quantity field can be filled manually or using arrows.
- The validation on the quantity field keeps the user from entering anything not in range 1-5. 
- Even when the validation is removed (through devtools for instance), illegal values are not accepted.

#### Reviews page

- Reviews are shown correctly.
- When not logged on the add review form is hidden and the text 'please login to add a review' is displayed with 'login' a link to the login page, which responds well.
- When logged on the review form is shown and responding correctly.
- If no reviews are present a message telling the user this appears.

#### Vote page

- When not logged on the vote buttons are hidden and the text 'please login to vote' is displayed with 'login' a link to the login page, which responds well.
- When the user is logged but has already votes, the vote buttons are hidden and the text 'You have already voted is shown'.
- When the user is logged on and has not voted, the vote buttons are shown and respond well. The site updates correctly with the vote added.
- The amount of votes per item are displayed correctly, the progress bars fill up correctly to the relevant percentage.

#### Cart page

- The cart page shows a message that the cart is empty with a button to return to the store, when no items are in the shopping cart.
- All items in the cart are displayed correctly.
- The total price and construction time is calculated and shown correctly.
- The checkout button is disabled when the user is nog logged on.
- When not logged on, clicking the checkout button will display a message asking the user to login. The login word in the text is clickable and takes the user to the login page.
- The quantity of each item shown can be adjusted. Illegal values cannot be entered through form validation (anything outside 0-5).
- Even when the validation is removed (through devtools for instance), illegal values are not accepted.  
- Setting the quantity to 0 and pressing the adjust button will remove the object from the cart.

#### Checkout page

- The contents of the cart is shown correctly.
- The total price is calculated and displayed correctly.
- The form validation of the checkout form prevents empty fields.
- The card form is working as intended by stripe (this has been fully imported from stripe)
- When not logged on, the site will move the user to the login page. This might be tested by diretly typing in the url in the address bar. (https://codewouter-the-woodworks.herokuapp.com/checkout/)
- A payment intent is created in Stripe, correctly using the total price as amount.
- If all fields are valid, pressing the 'complete order' button will succesfully:
	+ Proces the order so it's placed in the database and viewable through the admin part of the site.
	+ Proces the payment intent through Stripe's payment test functionality, the card is charged and the amount deducted. The webhook is received and processed and if succesful (which it always is) the checkout succes view and thus the page is loaded. See below for an example.
	+ Load the checkout succes page.


![payment-example](https://ms4-the-woodworks.s3.eu-west-2.amazonaws.com/media/images/payment-example-stripe.JPG)


#### Checkout Succes page.

- A message displays that the order has been processed succesfully and was paid for.
- The shopping cart is emptied.

#### General

- Using the back button on the browser will not lead to errors.

### Bugs left to be solved.

- The javascript function to render the progressbars on the poll page needs to be called when the page is rendered. Using ``` <body onload="myFunction()"> ``` would work but I do not know a way to pass the three arguments/variables needed at each iteration of the forloop creating the bars. In the end I chose to call the function through a small inline script. Which is of course not the best way to do this.

- In the javascript event listener ```document.getElementById('checkout-anchor').addEventListener("click", disableButton)``` the id is not always present (as intended). This will throw a console error when the cart page is loaded when the user is logged on. I cannot find a way (in time) to test the presence of the id before activating the eventlistener. In all if statements I found on the net, some form of getElementbyID is used. In the end I just catch the error and return nothing.

### Interesting bugs/issues solved

- When trying to disable the checkout button when the user was not logged on. I struggled to get this working. I couldn't understand how to call the function on pageload. In the end I made it too complex. Simply giving it an id based on whether the user is logged in, the disableButton function has a target id or not.

- When trying to pass the status whether someone had voted directly to the template it didn't work. After asking around it seemed I could only pass arguments to a template through the function that renders it (view\_poll). So I completely rebuild the view_poll function to check the status and pass it.

- A bug that took a -lot- of time was the following error
	- ```NoReverseMatch at /cart/, Reverse for 'adjust_cart' with arguments'(",)' not found ```. 
-  After being at it for the better part of a day, including a four hour session with tutor support (no critism there, love them), Chris himself stepped through slack and solved it in 5 minutes. The variable I was trying to pass should've been item.id instead of item.item_id. incredible how well Chris can read the code and spot mistakes. From the whole endeavour I really got to understand how the views, urls and templates work together and how arguments are passed.

### External testers

- My dear friend Jos (Jaws) who is part professinal tester who went through the site.
- On Slack I owe a debt of gratitude to Vlad opera, JoWings_Alumna, Aukje - byllsa, JimLynx and Igor for peer reviewing the project.

## Deployement

The following steps were taken to deploy the project to Heroku.

1. Login at Heroku

2. On Heroku create a new app **codewouter-the-woodworks**

3. In the Heroku App Dashboard, under the Resources tab, add Heroku Postgres (select the "Hobby Dev - Free" option).

4. In Gitpod use ```pip freeze > requirements``` to be sure eveything is added. At the time of deployement this was the contents of the requirements.txt file:

   ```
	asgiref==3.2.10
	boto3==1.14.60
	botocore==1.17.60
	dj-database-url==0.5.0
	Django==3.1
	django-allauth==0.42.0
	django-forms-bootstrap==3.1.0
	django-storages==1.10
	docutils==0.15.2
	gunicorn==20.0.4
	jmespath==0.10.0
	oauthlib==3.1.0
	Pillow==7.2.0
	psycopg2==2.8.6
	psycopg2-binary==2.8.6
	python3-openid==3.2.0
	pytz==2020.1
	requests-oauthlib==1.3.0
	s3transfer==0.3.3
	sqlparse==0.3.1
	stripe==2.53.0
   ```

5. The database had already been migrated at an earlier point from sqlite3 to Postgres. The proces used then was:

	1. From the CLI of gitpod install dj\_database\_url and psycopg2-binary (and use pip3  freeze > requirements.txt)
	2. In settings.py import dj\_database\_url
	3. In settings.py code this is in to have the postgres database selected when a DATABASE_URL is present in the environment variables. Which in Heroku is present and set to the correct url.
	
	```
	if 'DATABASE_URL' in os.environ:
    	DATABASES = {
        	'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
    	}
	else:
    	DATABASES = {
        	'default': {
           		'ENGINE': 'django.db.backends.sqlite3',
           	 	'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
       		 }
    	}
	```	
	3. Re-run the database migrations with `python3 manage.py migrate` which will build the Postgres database.
	4. And create a new superuser with `python3 manage.py createsuperuser
	5. Commit the changes. 

6. The DEBUG value is set dependent on the environment variable DEVELOPMENT. Heroku does not have this key, so it automatically reverts to false.
	```
	if 'DEVELOPMENT' in os.environ:
	    DEBUG = True
	else:
	    DEBUG = False
	```
7. In heroku add a DISABLE_COLLECTSTATIC Config Var and set its value to 1. So heroku wil not start collecting static files.
8. Static files (css/javascript/media) are all uploaded to a AWS Bucket and pulled from there. This was implemented very early in development as to be sure everything functioned correctly. To make heroku use these files and locations, some environmental variables needed to be said (see the overview of all heroku environmental variables)
9. Install gunicorn with `pip3 install gunicorn`and freeze it in the requirements file with ```pip freeze > requirements```
10. Create a Procfile in the main dir and enter within that `web: gunicorn the_woodworks.wsgi:application`
11. Within settings.py add the hostname to allowed host: `ALLOWED_HOSTS = ['codewouter-the-woodworks.herokuapp.com', 'localhost']`
12. Commit the changes and git push all to github.
13. Now everything was pushed to heroku using

	`
	heroku git:remote -a codewouter-the-woodwork
	`
	
	`
	git push heroku master
	`

15. Finally all environment variables from gitpod needed to be copied to heroku, resulting in this list:

    |           Key             |   
    |:-------------------------:|
    | STRIPE\_PUBLIC\_KEY       | 
    | STRIPE\_SECRET\_KEY       | 
    | STRIPE\_WH\_SECRET  	    |
    | SECRET\_KEY               |
    | AWS\_ACCESS\_KEY_ID       |
    | AWS\_SECRET\_ACCESS\_KEY  |
    | EMAIL\_HOST\_USER         |
    | EMAIL\_HOST\_PASS         |
    | DATABASE\_URL             |
    | DISABLE\_COLLECTSTATIC    |
    | USE_AWS					|

16. On the top right choose the 'more' button and choose 'restart all dynos'
17. Open app to see the deployed project.

### Local deployement
Unfortunately as I uploaded a lot of static media content to my AWS bucket and migrated very early to a Postgres database, it is not possible to have someone else create a local deployement without sending over static files.

## Credits

- Major inspiration and quite a bit of code was taken from Code Institute's Boutique Ado project by Chris. Where code was used fully or used partly has been written down in comments in the code.
- Inspiration for the design was taken from Rob Simon's Blindside Brewery project for the design aspect to find a simple yet fullfilling design in regards to making a minimal viable product. The repository is [here](https://github.com/RobSimons1/ms4-ecommerce).
- All product pictures and descriptions were taken from https://www.grainwoodfurniture.com/, except for:
	+ chair: https://wihardja.com.sg/
	+ sidetable: https://www.homesdirect365.co.uk/
- Favicon item is from https://www.freefavicon.com/freefavicons/objects/iconinfo/saw-152-27070.html
- The treebark footer image from https://www.freepik.com/free-photo/seamless-tree-bark-texture-design_6446472.htm
- The main body background texter from https://pngtree.com/freebackground/cracked-wooden-texture-background-wood-plane_1162081.html 
- Lastly, a lot of help to solve several bugs came from the Slack commuity and stack overflow


## Acknowledgements

I would to thank the following people:

+ First and foremost, my wife and children. For putting up with me, having to miss me and support me in all the past months!
+ Special shoutout to Igor Basuga (Igor_CI) who as a tutor, lead and just as a good friend, helped me with many a problem/bug, but also as a friend was very supportive.
+ Shoutout to Chris ckz8780 for an awesome example project but especially, coming to the rescue like a Django Superman when things got real tough.
+ The slack community as a whole, with extra consideration for JoWings, Vlad Oprea, Mr Bim, Anthony, Matthew, Jim Lynx, Aukje bylisa and Clint.
+ My dear friend Jaws (Jos), tester extraordinaire.
+ CI Tutor support
+ CI in general for putting up with my longwinded studentship. Especially thankful for the extensions I got to finish this up!
 

