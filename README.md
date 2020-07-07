# Neverlost Thrift

The site is desgined as an online thrift store, with all the curiousity and mish mash of goods as its feature. Its goal is to allow people to  browse as much as buy, sifting through the hodgepode of once-off re-usable goods that re for sale. I wanted to create a site which is based more on playfulness and discovery than raw economic gain, allowing people to just enjoy looking. I have deliberately created a system similar to pintrest, instagram, or other social networks to add that element of playfulness.

Link to deployed project [here](https://neverlost-thrift.herokuapp.com/).

## UX

### Home Page

#### First Impression
##### Initial Viewing
The home page is desgined as a feed, with infinite scrolling, much like many social networks. A page preloader with a slow fade is placed covering content on all pages, the z-index has been placed under the navbar and menu button, so they persists from one page to the next. Toasts pop up above the overlay so notification are still clearly seen, even while waiting for images to load.
The main splash image highlights monthly Stock Drops, each featuring different types of goods, with a short description. The style is reminiscent of a vintage / antique aesthetic, calling people to just take a look at the wares of various types.
The style is busy, reminiscent of Instagram's 9-square grid on desktop and personal feed on desktop. Images are all automatically cropped 1:1 to call back to this theme. 


#### Navigation
##### Navbar
The navbaar has layers, a persistent search bar is available, as is the cart, profile and user profile button, keeping the interactivity available. The logo is big, bold and ever-present as a form of self-advertising. The authourisation functions switch depending one whether or not the user is logged in. Signup, login, profile and logout are always highlighted no matter the page. The like and cart button are animated to catch the eye and keep things playful. The other menus are standard e-commerce menus. I've tried to make the like and cart more prominent than these, as I think positive user engagement is gained more through simplicity than deep menus.
The mobile and side nav have been placed to the right for ease of use with one hand.

##### Ajax Forms
I'm utillising ajax form submissions to smooth out the user experience while browsing the site. Items can be cleaning added to the cart, removed, liked, and unliked all in a few simple clicks. The popover menus update in realtime with the submissions, so you can easily access your most recently liked items, the cart or checkout. The buttons are animated and switch icons depending on context, such as whether an item has numerous stock or is a unique item.
The icons are all SVG based from Bootsrap icons, styled within the file, sized by and stored within the object element so they can be cached by the browser. 


#### Feed
##### Sorting
The store items on the main page are decided by a number of fields I have placed on their model. Firstly they are shown by popularity, a number which is the sum of likes they have received and quantity sold, and secondly by stock. This way the most popular items that still have the most stock are pushed to the top to generate sales, whereas items out of stock are listed last in the feed. They are still viewable to maintain the theme of browsing goods, see what's there, playing with the products rather than solely shopping.
Infinite Scroll is used to avoid pagination and create the social media-like feed, keeping the browsing endless.

##### Product Box
Each item has a box complete with varying degrees of info. As a thrift store usuall has all kinds of stock, of varying shapes, sizes, types and number, I have attempted to dynamically highlight this where possible. Items can be marked as a "sole item", essentially unique, "low stock" for items that re not unique, but are running out, and "sold" when stock hits zero. Other information such as size, where applicable is displayed, item names are truncated to maintain the aesthetic, if somebody likes the image the idea is that they will click from curiosity.
The boxes have a series of tags below them which can be clicked to bring up items of a similar "aesthitic", much like socia network tags. If you want to shop for vintage, that's, there, maybe the color yellow? You can click on that. Originally I wanted users to be able to enter some of their own tags, but that feature was cut due to deadlines and will be revisited later.


### Profile Page

#### Settings
##### Billing & Shipping
The main feature of the settings page is to be able to save SHipping and Billing settings seperately, and have them applied seperately. On preparing an order form all fields will be propopulated with the neccessary info. Likewise, all information will be saved to your account if you so choose at payment during the checkout.

##### Email & Password
DJango-allauth has been used for the majority of settings regarding verifivation and security. Most functions work with a redirect to the user's previous oage for a smoother experience However, I found django-allauth to be quite inflexible and obtuse. I would likely not choose it agin.


### Search, About, Contact

#### Search
The search page returns weighted results utilising PostgreSQL database unique features in django. It searches text, weighting tags as more important and the other sections less important before returning the results. The search uses the same page and view as the home page, just altered to suit the search 

#### Contact
A simple contact form that send emails to the recipients with a thank you email as well. All emails are stored in the database for reference. I was going to make them viewable via the an administrator site section, but I had to cut those features. Will be added at a later date.

### Fonts, Colours

#### Fonts & Colors
The font choices are clean simple and bold, as are the colors. I wanted the look to bright, bubbly, fun, slightly mismatched and a little bit cheesy, just like a really good thrift store.

##### Main Palette
![Main pallette](https://user-images.githubusercontent.com/44118951/86847565-cf1e5180-c0ac-11ea-867a-bf63a3ed1723.png)

##### Bootstrap SASS
For this project I have utilised Bootstrap 4.5 source files to ovveride their class defaults to my liking, making customisation much more easy. I can now re-them the entire site with a single switch in the code, which is fantastic. I applied the above pallete to defaults for use in toasts, messages, error warnings, etc. Other details, such as shadows, sharp edged boxes by default, etc. have all been taken advantage of. Despite thinking this would minimise the amount of Bootsrap features I don't use, I ended up utilising the majority of them nonetheless.

### User Stories
As a user interested in browsing, I expect to see lots of different items that could interest me.

As a user interested in clothing, I expect to be find unique items.

As a user interested in antiques, I expect to look through to find some goods.

### Wireframes
Wireframe: https://drive.google.com/open?id=1qIyntbCbm1Q0vOoC849uHAyfC5QICYAL

## Features

### Features implemented
- General
    - App structure
        - All templates and static files are held in the base directory and then in respective app folders, rather than within the app folders. I thik this maintains clearer, more cosistent directory structure during development. Though it may be conter-productive with regard to modularity.
        - SASS has been utilised for greater customisation of [Bootstrap4](https://getbootstrap.com/)
        - The SASS auto-compiles a css file when the app runs, so only source files are to be edited and css files are never commited.
    - Security
        - All sensitive information is stored in environment variables and hasn't been commited.
        - [django-allauth](https://django-allauth.readthedocs.io/en/latest/index.html) is utilised for security purposes.
        - Decorators and mixins are utilised to prevent access to forbidden pages.
        - DetailViews will often redirect a user to their own version of that view to prevent access to other's orders.
        - Stripe is active on all pages so their own fraud protection is active.


- Products
    - Items are marked as unique by default and their stock will be set to 1.
    - Items that are not unique have stock set to a default of 50
    - when these' items stock drops below 10 they will be marked as "low stock"
    - Users can not purchase more stock than is available, it will be set to the maximum stock availabe.
    - Items with 0 stock will be automatically set to "sold" and have their add to cart buttons removed.
    - Products remain viewable and likable after being sold.
    - products can be saved to userprofiles
    - The items saved by users will be saved in reverse chronological order by utlising a "through" model table on the ManytoMany field.
    - Products have a "popularity" field that updates on likes, and stock changes.
    - Products are sorted by both popularity and stock quantity
    - Product images are automatically resized before being uploaded to save space and maintain the aesthetic
    - Delivery is €9 and is free above €60.
    - Likes and carting is all ajax for smoothness
    - Popovers update in realtime with adds to carts and likes

- Users
    - AnonymousUsers can go through the entire purchase process without signing up
    - Confirmation sent to email address on purchase.
    - The ability to view that order will remain in their session if the anonymous user wishes to return to the page.
    - That order also cannot be viewed by anyone else without the session cookie.
    - Anonymous users can like items, have them saved in their session
    - If they choose to join or login during that session, the likes in their session will be transferred to their user profile and saved. 
    - Users can save shipping and billing information seperately
    - The information can be saved during checkout both together
    - If the info is the same, you only have to enter it once, just leave the box ticked
    - authroisation is handled by allauth, email verification, password changes, etc.
    - Can use the "Remember me" function to stay logged in
    - Can change password securely

- Search
    - Search has been implemented using Postgres database features
    - Tags are weighted more than other text
    - Traditional search works as well, however I find the Postgres database to be a bit either too inclsive or exclusive, A wider array of items would help sove the issue.
    - Tags allow eople ro search by idea
    - Stockdrop images have a similar image resizing process
    - Stockdrops show monthly sales based on a theme, creating more unique collections
    - categories offer a more traditional browsing feature
    - Tags allow people to search the items by idea rather than the traditional means.

- Testing
    - From the outset I have set up TravisCi and written tests for my functions.
    - For the vast majority of the project I have only pushed to master after testing has been completed.
    - Coverage was utilised throughout testing
    - TravisCI automatically pushed to Heroku on passing
    - Unfortunately testing fell away as the deadline came up, but I mainr=tained those I had written.
    - environment variables have never been written in the app, let alone committed
    - the procfile utilises gunicorn for initialisation
    - I created custom crispy fields templates and allauth templates.

- Utility
    - Infinite Scroll has been applied to all feeds.
    - Preloader placed over content but under menus
    - Nav and menus placed on the right for one-handed use
    - Nav options change depending on location and authentication.
    - Messages pop up for user feedback
    - email has been applied and is functional


### To Explore / Do

- Content 
    - More comprehensive sizing application
    - More items
    - Custom user walls, like pintrest
    - Better search function
    - Users can enter tags too
    - Number of likes are shown for items

- Users
    - More interaction between users
    - A board where the can ake requests or comment
    - A public profile page with liked items, bought items if desired, etc.
    - A follow system

- General
    - an admin section with superuser abilities
    - data graphs with tracking item sales, popularity, effect
    - Swaggger testing
    - Database charts for mapping connections


## Technologies Used
- Languages
    - [Python](https://www.python.org/)
        * Using Flask and other plugins to develop the app
    - [HTML](w3.org/standards/webdesign/htmlcss)
        * Page markup
    - [CSS](w3.org/standards/webdesign/htmlcss)
        * Styling
    - [Javascript](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
        * Running functions to initalize components
    - [JQuery](https://jquery.com/)
        * Animations and click functions

- Framework
    - [Bootstrap4](https://getbootstrap.com/)
        * Used for basic styles and outline

- Resources
    - [Bootstrap Icons](https://icons.getbootstrap.com/)
        * Used for icons
    - [Google Fonts](https://fonts.google.com)
        * Font Styles
    - [Waypoints](http://imakewebthings.com/waypoints/)
        * Used for infinite scroll on feed pages -->

- Packages
    - Please see requirements.txt
    <!-- - [django](https://www.djangoproject.com/)
        * The main app technology for project
    - [django-crispy-forms](https://django-crispy-forms.readthedocs.io/en/latest/)
        * Form parsing and formatting
    - [django-sass-processor](https://github.com/jrief/django-sass-processor)
    - [django-compressor](https://django-compressor.readthedocs.io/en/stable/)
        * Both used for compiling and deploying SASS css files
    - [whitenoise](http://whitenoise.evans.io/en/stable/)
        * Used to deploy static files during production
    - [dj-database-url](https://github.com/jacobian/dj-database-url)
        * Used to parse databse URLs
    - [coverage](https://coverage.readthedocs.io/en/coverage-5.1/)
        * Used for testing
    - [gunicorn](https://gunicorn.org/)
        * Server deployment on heroku -->

## Testing & Troubleshooting
- Validation
    - All forms have validation and will not submit without the proper information.
    - Links checked with [W3C Link Checker](https://validator.w3.org/checklink)
    - HTML has been validated with [W3C HTML5 Validator](https://validator.w3.org/)
    - CSS has been validated with [W3C CSS Validator](https://jigsaw.w3.org/css-validator/) and auto-prefixed with [CSS Autoprefixer](https://autoprefixer.github.io/). There is a validation issue with margin-block-end but it is a valid value in all popular browser.
    - Each javascript file was tested on the site for errors and fucntionality using the console and with [JSHint](https://jshint.com/)
    - gitignore file has been included to prevent system file commits
    - requirements.txt updated

- Testing
    - [Travis CI](https://travis-ci.com/) is utilised for testing on each branch. If the master branch is tested and passes, the app is automatically deployed to [Heroku](https://www.heroku.com/). THis maintains a functional production app at all times.
    - [Coverage](https://coverage.readthedocs.io/en/coverage-5.1/) has been utilised throughout the project to ensure all code is tested thoroughly.
    - A secondary, persistent, PostgreSQL test database has been utilised on [Heroku](https://www.heroku.com/). This way the test database functions more similarly to the production database, with items being added and persisting. THis allows for more accurate testing and test views which function on a real database. Testing must be run with this command to maintain the database's persistence
    ```
    python manage.py test --keepdb
    ```
    - There is a console log notification that states whether debug mode is off or on.
    - The views have been thoroughly manually tested and refined over time, utilising  python features to create documents in the database in a useful, flexible structure.
    - The documents in the database have been examined and structured in a manner so that the information is well defined, checking how the views effect documents.
    - I have tested the site and its layout on multiple android devices, different sizes, on multiple browsers. I was unable to test on iOS. Mainly developed and tested using chrome developer mode. It is fully responsive with a clean layout on each device.
    - Each feature was developed and tested in its own branch before being pushed to master.
    - Some tests were performed on views and were tested manually throuroughly. For example, every possible combination on search was tested.
    - Each time a feature was added all the functions were tested to see if there was an impact.


    ## Deployment
    0. Github 
    1. Fork the repo on github.
    0. Push the repo to a PaaS, such as Heroku.
    0. Set the environment variables, ensure debug is False.
    0. Deploy and your good to go.

    ## Credits

    ### Content
    Photos are from unsplash
    Any code utilised from another programmer is documented and credited within the code. However, much of the stripe webhook details have been taken from the codinstitute lessons utilised and changed for my needs.
