[![Build Status](https://travis-ci.com/Ri-Dearg/neverlost-thrift.svg?branch=master)](https://travis-ci.com/github/Ri-Dearg/neverlost-thrift) [![Coverage Status](https://coveralls.io/repos/github/Ri-Dearg/neverlost-thrift/badge.svg)](https://coveralls.io/github/Ri-Dearg/neverlost-thrift) ![Code Style](https://img.shields.io/badge/code%20style-pep8-green.svg) 
<div align="center">
  <img src="https://user-images.githubusercontent.com/44118951/90537734-f5401280-e17d-11ea-8846-850cfc1129d8.png" alt="Neverlost Thrift">
</div>

![HomePage](https://user-images.githubusercontent.com/44118951/90686385-8ccf5f00-e26b-11ea-824b-4481f236c2d8.png)

[Neverlost](https://neverlost-thrift.herokuapp.com/) is designed as an online thrift store, with the same curiosity and mish-mash of goods found in a thrift store as its feature. Its goal is to allow people to browse as much as buy, sifting through the hodgepodge of once-off, unique, re-usable goods that are for sale. I wanted to create a site which is based more on playfulness and discovery than raw economic gain, allowing people to just enjoy looking. As it is a thrift store it has been designed with varying items, sizes, and non-conforming stock in mind. I have deliberately created a system similar to Pinterest, Instagram, or other social networks to add that element of playfulness.

## Table of Contents
1. <details open>
    <summary><a href="#ux">UX</a></summary>

    <ul>
    <li><details>
    <summary><a href="#goals">Goals</a></summary>

    - [Visitor Goals](#visitor-goals)
    - [Business Goals](#business-goals)
    - [User Stories](#user-stories)
    </details></li>

    <li><details>
    <summary><a href="#visual-design">Visual Design</a></summary>

    - [Wireframes](#wireframes)
    - [Fonts](#fonts)
    - [Icons](#icons)
    - [Colors](#colors)
    - [Images](#images)
    - [Styling](#styling)
    </details></li>

    <li><details>
    <summary><a href="#seamless-design">Seamless Design</a></summary>

    - [Preloader](#preloader)
    - [AJAX](#ajax)
    - [Toasts](#toasts)
    - [Infinite Scroll](#infinite-scroll)
    </details></li>
    </ul>
</details>

2. <details open>
    <summary><a href="#features">Features</a></summary>

    <ul>
    <li><details>
    <summary><a href="#page-elements">Page Elements</a></summary>

    - [All Pages](#all-pages)
    - [Product List Page](#product-list-page)
    - [Product Detail Page](#product-detail-page)
    - [Account Pages](#account-pages)
    - [Likes Pages](#likes-pages)
    - [Cart Pages](#cart-pages)
    - [Checkout Pages](#checkout-pages)
    - [Contact Pages](#contact-pages)
    </details></li>

    <li><details>
    <summary><a href="#additional-features">Additional Features</a></summary>

    - [General](#general)
    - [Products](#products)
    - [Users](#users)
    - [Search Features](#search-features)
    </details></li>

    <li><details>
    <summary><a href="#features-not-yet-implemented">Features Not Yet Implemented</a></summary>

    - [Basic](#basic)
    - [Content](#content)
    - [User Features](#user-features)
    </details></li>
    </ul>
</details>

3. <details open>
    <summary><a href="#information-architecture">Information Architecture</a></summary>

    <ul>
    <li><details>
    <summary><a href="#database-structure">Database Structure</a></summary>

    - [Details](#details)
    - [Diagram](#diagram)
    </details></li>    

    <li><details>
    <summary><a href="#data-models">Data Models</a></summary>

    - [Checkout App](#checkout-app)
    - [Contact App](#contact-app)
    - [Products App](#products-app)
    - [Users App](#users-app)
    </details></li>
    </ul>
</details>

4. <details open>
    <summary><a href="#technologies-used">Technologies Used</a></summary>

    - [Languages](#languages)
    - [Frameworks](#frameworks)
    - [Libraries](#libraries)
    - [Packages](#packages)
    - [Platforms](#platforms)
    - [Other Tools](#other-tools)
</details>

5. <details open>
    <summary><a href="#testing">Testing</a></summary>

    <ul>
    <li><details>
    <summary><a href="#automated-testing">Automated Testing</a></summary>

    - [Validation](#validation)
    - [Python Testing](#python-testing)
    - [Coverage](#coverage)
    - [Travis CI](#travis-ci)
    - [Coveralls](#coveralls)
    </details></li>

    <li><details>
    <summary><a href="#manual-testing">Manual Testing</a></summary>

    - [General Testing](#general-testing)
    - [Mobile Testing](#mobile-testing)
    - [Desktop Testing](#desktop-testing)
    </details></li>

    <li><details>
    <summary><a href="#bugs">Bugs</a></summary>

    - [Known Bugs](#known-bugs)
    - [Fixed Bugs](#fixed-bugs)
    </details></li>
    </ul>
</details>

6. <details open>
    <summary><a href="#deployment">Deployment</a></summary>

    <ul>
    <li><details>
    <summary><a href="#local-deployment">Local Deployment</a></summary>

    - [Local Preparation](#local-preparation)
    - [Local Instructions](#local-instructions)
    </details></li>

    <li><details>
    <summary><a href="#heroku-deployment">Heroku Deployment</a></summary>

    - [Heroku Preparation](#heroku-preparation)
    - [Heroku Instructions](#heroku-instructions)
    </details></li>
    </ul>
</details>

7. <details open>
    <summary><a href="#credit-and-contact">Credit and Contact</a></summary>

    - [Images](#local-preparation)
    - [Code](#local-instructions)
    - [Contact](#contact)
</details>

----

# UX
## Goals
### Visitor Goals
The target audience for Neverlost Thrift are:
- People who want unique clothes and items.
- People who are interested in vintage or upcycled products.
- People that want to browse through cute items and different aesthetics.
- Collectors of particular types of goods.
- Shoppers that don't know what they want, but want to explore.

User goals are:
- Find that unique something to add to my wardrobe.
- Create an online collection of a certain aesthetic I can share.
- See what's new and exciting every month.
- Navigate the store and sections easily through different kinds of goods.
- Make a secure purchase.

Neverlost Thrift fills these needs by:
- Creating a system similar to social feeds with likes, infinite scroll, tags, square and stylish images, etc. This creates the aspect of playfulness and familiarity with something other than a store.
- New, unique stock of a certain type is added every month, giving more reasons to return and browse.
- The site follows standard design conventions of a shop with regard to menus, checkout, categories, etc, while also highlighting the more unique aspects. This allows the user to navigate easily while noticing that which sets it apart.
- Searching and product pages include similar items, categories and are organised by popularity, so the customer sees the most engaging goods first.

### Business Goals
The Business Goals of Neverlost Thrift are:
- Create an interesting place to shop, as well as play.
- Maintain site traffic through non-shopping engagement.
- Keep the site interesting with new different stock incoming monthly.
- Have customers feel they are purchasing through a trustworthy source.
- Have the most engaging content front and centre to maintain engagement and increase sales.

### User Stories
1. As a user interested in browsing, I expect to see lots of different items that could interest me.
0. As a user interested in clothing, I expect to find unique items.
0. As a user interested in antiques, I expect to look through to find rare goods.
0. As a collector, I expect to find a collection of unique goods from the same category.
0. I expect to be able to use likes and tags to categorise and save items.
0. As a user shopping online, I expect to see menus and navigation that follow precedents set by other shopping sites.
0. As a user used to modern shopping sites, I expect the buttons to be ajax page changing to be fluid.
0. As a user looking through the items, I expect clear labels as to what kind of item it is and the stock of the said item.
0. As a user adding items to the cart, I expect to not be interrupted when clicking add.
0. As a user with items in the cart, I expect my totals to be accurate and updated.
0. As a user who wants to make a purchase, I expect to feel the site is trustworthy and to have a straightforward purchasing flow.
0. As a user who has made a purchase, I expect to receive a confirmation by email.
0. As a user who has made a payment, I expect the order to be confirmed, even if I am interrupted.
0. As a repeat purchaser, I expect to have my information saved for reuse.
0. As a user who has made purchases, I expect to be able to view my order history.
0. As a user who may want to return, I would like to be able to make an account securely.
0. As a user who has made an account, I expect to be able to change or update my information.


## Visual Design
### Wireframes
Wireframe: https://drive.google.com/drive/folders/1WHexlk5WcbX0tRLvL6d_u-NFCN9x0JS2?usp=sharing

### Fonts
<div align="center">
  <img src="https://user-images.githubusercontent.com/44118951/90979996-e6c87100-e558-11ea-8314-6b3acb4fd297.png" alt="Fonts">
</div>

- The primary font, [Montserrat](https://fonts.google.com/specimen/Montserrat) was chosen because it was similar to the secondary font used for the brand. It is sans-serif, so it is clear, clean and simple. It was chosen to not contrast or draw the eye, but instead to remain rather mute, keeping the eyes more focused on the products and images.
- The secondary font, [Lexand Deca](https://fonts.google.com/specimen/Lexend+Deca) was chosen because it is Monospace, is a very clean font, which looks great bold and in uppercase. The spacing equal spacing allowed for easy use in based on character length. It was perfect for a strong brand logo as well as use for headings.

### Icons
<div align="center">
  <img src="https://user-images.githubusercontent.com/44118951/90980094-8685ff00-e559-11ea-97af-756fae60a3dc.png" alt="Icons">
</div>

- Icons are taken from the new Bootstrap Icon library and so are SVG files, allowing for great styling flexibility and caching.
- Icons are utilised in the navbar for Account, Likes and Cart for consistency with other sites, a search icon is used on smaller screens. Matching icons are used on the product boxes and pages for clarity.
- If an item is added to cart or liked, the icons are swapped out on the fly after a successful ajax response to indicate the change.
- The same icons are utilised with different styles within an object tag applied to allow for better caching and faster icon swapping.

### Colors
<div align="center">
  <img src="https://user-images.githubusercontent.com/44118951/90965219-8688ef00-e4c6-11ea-9105-bc0fa68b9c2a.png" alt="Color Pallette">
</div>

- I wanted the site to look bright, bubbly, fun, slightly mismatched and a little bit cheesy, just like a really good thrift store.
- It's in the mixture and clashing of the colors that they come together to create an overall theme and unity.
- The colors chosen are clean, simple and bold, similar to the fonts.

### Images
<div align="center">
  <img src="https://user-images.githubusercontent.com/44118951/90981869-a6babb80-e563-11ea-9a04-3d432d84cca8.png" alt="Images">
</div>

- The site has a heavy focus on image use, utilising stylised images instead of standard product images to focus on an aesthetic use.
- All images are resized and converted upon upload before being saved for optimisation. 
- This creates uniformity between the images' style for the product display and also reduces the file size for better loading speed. High-quality images that are several MB will be reduced to ~ 50kb.
- A maximum of nine images are loaded at a single time, so at most, they will total ~ 450kb
- Images are all responsive. The image display grid is 3x3 on medium-sized screens and up, following Instagram's profile view conventions.
- On smaller screens, it is one image after another, in the style if Instagram's feed.
- Images have a small tag if there's more information to convey, such as low stock, a unique item or if it's sold out.

### Styling
- For this project I have utilised Bootstrap 4.5 source files to override their class defaults to my liking, making customisation much easier. The entire site can be restyled with a single switch in the code.
- The above palette has been applied to defaults for use in toasts, messages, error warnings.
- Using the SASS, shadows and sharp-edged boxes have been applied by default, taking advantage of the features.
- Responsive text sizing has also been enabled using SASS.
- Rounded edges have been utilised where a bit more friendliness and fun is necessary, such as the tags below the products.
- Fading animations are utilised for smoothness in certain transitions, such as the icons in the Navbar.


## Seamless Design
### Preloader
- A simple, style-consistent, preloader is used when loading pages, as the site is image-heavy.
- The Preloader is placed under the Navbar, so access to likes, account options, cart, categories, etc. will always be available to the user for a better navigation experience. It also maintains the brand logo appearance front and centre.
- The use of the preloader under the Navbar gives the impression of a persistent webpage despite loading new pages.
- The same preloader design is used when making payments to block of the page.

### AJAX
- AJAX only views use a simple decorator from the [django-ajax](https://github.com/yceruto/django-ajax) package to transfer data in JSON format.
- AJAX forms are used throughout the site, as this is a basic modern expectation of users when browsing a site, and a necessity when there are many buttons on the page, otherwise there would be serious flow and UX issues. It means all features can be used with a few simple clicks!
- Add to Cart and Like buttons utilise AJAX to encourage easy interaction.
- On success, the form will swap out icons to confirm the buttons have been clicked, changing the icon and/or color depending on the context, such as whether an item has numerous stock or is a unique item.
- Fires a Bootstrap Toast notification.
- It will also fire off a view to update and refresh the relevant like or cart "include" template. The total will be updated and the most recent liked items will be shown in real-time without the need for a page refresh.
- Removing items on the cart page will also update the cart total without page refreshing

### Toasts
<div align="center">
  <img src="https://user-images.githubusercontent.com/44118951/92019714-59a2ca80-ed57-11ea-8bfc-9c09f6115c12.png" alt="Toasts">
</div>

- Bootstrap Toasts are used to notify users of their actions on the page.
- A toast will show with a response to the user action, it may be a success message, an info message or an error message.
- This gives users immediate feedback, for instance, if a user has added all available stock of an item, the message will change from "X added to cart." to "X has run out of stock!"
- Toasts have a higher z-index than the preloader so they can be seen even while a page is loading.
- They are fired both by the Django messages function, as well as the AJAX forms.

### Infinite Scroll
- Infinite Scroll has been implemented to the site using [waypoints](https://github.com/imakewebthings/waypoints).
- Infinite Scroll is applied to product pages to create a social media-like feed.
- Allows the user to browse the entire stock, and like items or add to cart whenever they see something they like.
- The same preloader icon is used for loading new items.
- Django's paginator automatically provides the page list and queryset for the next set of items.

----

# Features
## Page Elements
### All Pages
#### Navbar
<div align="center">
  <img src="https://user-images.githubusercontent.com/44118951/90983901-e4264580-e571-11ea-969a-2691fab45c57.png" alt="Medium Header"><br>
  <img src="https://user-images.githubusercontent.com/44118951/90983900-e1c3eb80-e571-11ea-9b2e-63367348af77.png" alt="Small Header">
</div>

- The Navbar is the single persistent item across the site, as a footer has been foregone in favour of the infinite scroll.
- The Logo is always highlighted, central and bold, on all screen sizes, as a form of self-advertising.
- The three icons and the search bar are always present as they are key features of the site, however, positions change depending on screen size. The search bar moves down into the green section next to the collapsable menu on a smaller screen and the icons spread out. The heart shifts position to the centre under the logo and flashes pink when an item is liked, drawing attention towards the logo.
- Authorisation functions switch depending on whether or not the user is logged in. Signup, login, profile and logout are always highlighted no matter the page.
- The like and cart buttons are animated to catch the eye and keep things playful. 
- The cart button will highlight the number of items in the cart with a little badge.
- The section menus are standard e-commerce menus. Stockdrops are utilised as a separate category.
- Categories and StockDrop menu options are dynamically added and sorted based on the models in the database.
- The correct section menu is dynamically set as active and highlighted in the Navbar depending on the current page.
- I've tried to make the like, cart and tags more prominent than the section menus, as I think positive user engagement is gained more through simplicity than deep menus.
- The search bar is always available and performs a Postgres text search that gives more weight to tags.
- The mobile nav button has been placed to the right for ease of use with one hand.

### Product List Page
#### StockDrop Carousel
<div align="center">
  <img src="https://user-images.githubusercontent.com/44118951/90984657-a677eb80-e576-11ea-9cde-db27388571c1.png" alt="Stockdrop Carousel"><br>
</div>

- Used as a splash image that highlights the most recent collections.
- Stockdrops are a model and so images, phrases, links, dates, etc. are all dynamically generated.
- Most recently added Stockdrop is automatically set to the active image.
- Uploaded images, like products, are automatically resized appropriately.
- Displays only on the home page, search queries will remove it from the page.


#### Product Box
<div align="center">
  <img src="https://user-images.githubusercontent.com/44118951/91299975-c855b600-e7a2-11ea-933b-faf304c4f86b.png" alt="Product Box"><br>
</div>

- Used as the main item in the feed, as a 3x3 grid on larger screens, singly on smaller screens.
- Ordered by popularity, an integer that is the sum of likes they have received and quantity sold, and secondly by stock. This way the most popular items that still have the most stock are pushed to the top to generate sales, whereas items out of stock are listed last in the feed.
- Out of stock products are still viewable to maintain the theme of browsing goods, see what's there, playing with the products rather than solely shopping.
- Utilises small info banners to communicate item details. Items can be marked as a "sole item", essentially unique, "low stock" for items that re not unique, but are running out, and "sold" when the stock hits zero.
- Information changes depending on item details. If the item has a size it will be displayed, if the item is sold the add to cart button disappears, etc. As a thrift store usually has all kinds of stock, of varying shapes, sizes, types and number, I have attempted to dynamically highlight this where possible.
- Has two ajax form buttons for adding to cart or liking.
- item names are truncated to maintain the aesthetic, if somebody likes the image the idea is that they will click from curiosity.
- Tags at the bottom can be clicked to search for items with that tag, to bring up items of a similar "aesthetic", much like social network tags.

#### Search
- The Product List page also functions as the search query page.
- Runs a Postgres text-based search on all products, with weighted results. Tags carry one grade more importance than other text.
- Searches automatically remove the Stockdrop image and display the search term instead.
- Displays the same grid with filtered results.
- If there are no results, it gives the option to return to the main shop page and it displays a side-scrolling box with products.

#### StockDrop and Category
- Utilise the same layout and similar features as the Product List Page, with results filtered to the respective model.
- I will look into optimising the templates and views by integrating these pages into the same view and template as the Page List.

### Product Detail Page
#### Product Detail Box
<div align="center">
  <img src="https://user-images.githubusercontent.com/44118951/91301917-f4266b00-e7a5-11ea-8374-4f804d0b7b5c.png" alt="Product Detail"><br>
</div>

- Displays information similar to the product box but adds a description section, with larger text and buttons.
- Information will change dynamically, if there is more than one item in stock, there will be a quantity box, the size will or won't display, etc.
- Cannot add more than the current stock of the item to the basket.

#### Related Items Bar
<div align="center">
  <img src="https://user-images.githubusercontent.com/44118951/91303564-80d22880-e7a8-11ea-8474-187ab22f5ac4.png" alt="Product Detail"><br>
</div>

- Highlights up to nine other popular products in the same category as the chosen product.
- Utilises the same Product Box template with all the same features.
- Side-scrolling in line with many other sites' "Related items" sections.
- Is also used on other pages which may result as empty, such as empty search results, 404 pages, etc.

### Account Pages
#### Singup and Login
<div align="center">
  <img src="https://user-images.githubusercontent.com/44118951/91305151-e58e8280-e7aa-11ea-8455-214e0b86b602.png" alt="Product Box"><br>
</div>

- [django-allauth](https://github.com/pennersr/django-allauth) is used for account verification functions.
- Some aspects of django-allauth have been customised to suit the site, such as page redirections, etc.
- Both the Signup/Login pages give access to the other form in as a tab in case the incorrect option was selected.
- Many forms and templates have been customised for the site.

#### Settings Page
- All django-allauth functions are available, changing the email, adding email, changing password, etc
- Utilising these functions will redirect to the user's account page with a toast notification instead of the usual django-allauth redirect for smoother user experience.
- Trying to access another user's page will result in your own page being displayed as the view checks for the current logged in user and utilises that for the page context.
- Able to save Shipping and Billing details separately, so when making an order the fields will automatically be filled in.

### Likes Pages
#### Likes
- A list in reverse chronological order of all liked items.
- Page follows the same layout as other product feed pages.
- Can be used without logging in and the items will be saved to the session storage.
- If logged in, the items will be saved directly to the user account. 
- Any items that are stored in the session will be transferred to the user account upon login or account creation.
- if the user gets to the page without liked items it gives an option to head back to the main page. 

#### Likes Popover Notification
<div align="center">
  <img src="https://user-images.githubusercontent.com/44118951/92010500-29a0fa80-ed4a-11ea-8efb-f5ad77b86328.png" alt="Like Popover"><br>
</div>

- The popover in the navbar will update when a product is liked.
- displays only the recent likes so it doesn't become a long list. 
- is persistent on all pages. 
- Icon pulses as confirmation rather than opening to remain unobtrusive. 

### Cart Pages
#### Cart 
- Shows a list of items that have been added to the cart. 
- Information varies depending on product characteristics like quantity or size.
- Quantity can be altered, but cannot be increased above max stock. 
- Items can be removed without page reloading, they will fade out and a notification will fire.
- The total will also refresh when quantity is updated or an item is removed.
- If the page is empty, a button leading to the home page is shown.

#### Cart Popover
<div align="center">
  <img src="https://user-images.githubusercontent.com/44118951/92010878-9c11da80-ed4a-11ea-800d-867e624e7190.png" alt="Cart Popover"><br>
</div>

- Similar to the like popover but will update when a product is added.
- Icon pulses and has a badge showing the number of items in the cart.
- Can go straight to the checkout.

### Checkout Pages
#### Payment Page
- Displays an order summary with options for shipping, billing and card details utilising Stripe.
- The Shipping and Billing details can be entered separately if necessary. 
- If the box is ticked that they are the same, the view automatically inserts and sorts necessary form information.
- Billing and Shipping information can be saved to the profile if the save infobox is ticked.
- Payment buttons deactivate upon sending the form to not double send and the preloader blocks other buttons. 
- A Webhook will create the order if payment completes and the order hasn't been created.
- Email is sent on order confirmation.

#### Order Detail
- A simple page displaying order information. 
- A confirmed order automatically redirects to this page after creation.
- This page will redirect if it is accessed by an account that hasn't made the order. 
- If an account that is not logged in makes an order, a token which allows the user to view only their order is stored in the session. 

#### Order List
- A simple page with orders listed in reverse chronological order. 
- Displays an image and a few key order details. 

### Contact Pages
- A simple contact form that sends emails to the recipients with a thank you email as well.
- All emails are stored in the database for reference.


## Additional Features
### General
- App structure
    - All templates and static files are held in the base directory and then in respective app folders, rather than within the app folders. I think this maintains a clearer, more consistent directory structure during development. Though it may be counter-productive in terms of modularity.
    - SASS has been utilised for greater customisation of [Bootstrap4](https://getbootstrap.com/)
    - The SASS auto-compiles a CSS file when the app runs, so only source files are to be edited and CSS files are never committed.
- Security
    - All sensitive information is stored in environment variables and hasn't been committed.
    - [django-allauth](https://django-allauth.readthedocs.io/en/latest/index.html) is utilised for security purposes.
    - Decorators and mixins are utilised to prevent access to forbidden pages.
    - DetailViews will often redirect a user to their own version of that view to prevent access to other's orders.
    - Stripe is active on all pages so their fraud protection is active.

### Products
- Stock
    - Items are marked as unique by default and their stock will be set to 1.
    - Items that are not unique have stock set to a default of 50.
    - when these' items stock drops below 10 they will be marked as "low stock".
    - Users can not purchase more stock than is available, it will be set to the maximum stock available.
    - Items with 0 stock will be automatically set to "sold" and have their add to cart buttons removed.
    - Products remain viewable and likeable after being sold.

- Management
    - Products can be saved to user profiles by liking.
    - The items saved by users will be saved in reverse chronological order by utilising a "through" model table on the ManytoMany field.
    - Products have a "popularity" field that updates on likes, and stock changes.
    - Products are sorted by both popularity and stock quantity.
    - Delivery is €9 and is free above €60.

### Users
- Anonymous Users
    - Anonymous Users can go through the entire purchase process without signing up.
    - Confirmation sent to the email address on purchase.
    - The ability to view that order will remain in their session if the anonymous user wishes to return to the page.
    - That order also cannot be viewed by anyone else without the session cookie.
    - If they choose to join or login during that session, the likes in their session will be transferred to their user profile and saved.
- Accounts
    - [django-allauth](https://django-allauth.readthedocs.io/en/latest/index.html) features are utilised for accounts.
    - Accounts must be email verified.
    - Can use the "Remember me" function to stay logged in.
    - Can change password securely.
    - Can add multiple email addresses.

### Search Features
- Details
    - Search has been implemented using Postgres database features.
    - Utilises a full-text search on select model fields.
    - Product tags are weighted more than other text to maintain their importance.
- Tags
    - Tags allow people to search by idea, concept, aesthetic, etc.
    - More similar to a social networking site.
    - A familiar concept used for quickly accessing similar items more abstractly.


## Features Not Yet Implemented
### Basic
- An admin section with superuser abilities within the site.
- Data graphs with tracking item sales, popularity, etc.
- Implement Swagger API.
- Database charts for mapping connections.
- Preloader fades in on click, before another page loads, giving a more complete sense of seamless loading.

### Content 
- More comprehensive product size features.
- More products.
- Custom sharable user walls, like Pinterest.
- A more well-defined search function, as I find the search to be either too inclusive or exclusive.
- Tags can be entered by users as well.
- The number of likes is shown for items.
- Newsletter Signup
- Sharing to Social Networks

### User Features
- More interaction between users, such as the ability to follow/friend.
- A board where they can make requests for particular items or comment.
- A public profile page with liked items, bought items if desired, etc.
- Login using social accounts.

----

# Information Architecture
## Database Structure
### Details
- I have utilised a **Postgres** database throughout the entire project development.
- I chose this instead of the standard **sqlite3** database given with a Django installation to utilise more advanced Database features available within Django. In particular, weighted text search, and array fields in the DB.
- The project is directly connected to the deployed database on Heroku during development as this was necessary to utilise a Postgres database on Gitpod while using the Code Institute Dockerfile.

### Diagram
- The diagram shows a layout of the tables created by my models in the database.
- The diagram below omits the tables created by default, except the user table, as well as the tables created by [django-allauth](https://django-allauth.readthedocs.io/en/latest/index.html).
<div align="center">
  <img src="https://user-images.githubusercontent.com/44118951/91736967-c3cc3b80-ebae-11ea-8905-661c3a1e9f8c.png" alt="Database Diagram"><br>
</div>


## Data models
**Note:** 
- I am omitting all default tables created by [django](https://www.djangoproject.com/) as well as [django-allauth](https://django-allauth.readthedocs.io/en/latest/index.html) from this section. Please refer to their documentation (refrenced [here](#technologies-used)) for more information on their data models.
- Some models use a CustomPhoneNumberField class which inherits the PhoneNumberField class from [django-phonenumber-field](https://github.com/stefanfoulis/django-phonenumber-field). It simply removes the strict number verification in the class.
- The CountryField is utilised from [django-countries](https://github.com/SmileyChris/django-countries).

### Checkout App
#### Order Model
**Notes:**
- Utilises the OrderLineItem model for total fields.

| Column Name | Validation | Field Type |
 --- | --- | ---
order_number | max_length=32, null=False, editable=False | CharField
email | max_length=254, null=False, blank=False | CharField
billing_full_name | max_length=50, null=False, blank=False | CharField
billing_phone_number | null=False, blank=False | CustomPhoneNumberField
billing_postcode | max_length=20, default='', blank=True | CharField
billing_town_or_city | max_length=40, null=False, blank=False | CharField
billing_street_address_1 | max_length=80, null=False, blank=False | CharField
billing_street_address_2 | max_length=80, null=False, blank=False | CharField
billing_county | max_length=80, default='', blank=True | CharField
billing_country | blank_label='Country *', null=False, blank=False | CountryField
shipping_full_name | max_length=50, null=False, blank=False | CharField
shipping_phone_number | null=False, blank=False | CustomPhoneNumberField
shipping_postcode | max_length=20, default='', blank=True | CharField
shipping_street_address_1 | max_length=80, null=False, blank=False | CharField
shipping_street_address_2 | max_length=80, null=False, blank=False | CharField
shipping_town_or_city | max_length=40, null=False, blank=False | CharField
shipping_county | max_length=80, default='', blank=True | CharField
shipping_country | blank_label='Country *', null=False, blank=False | CountryField
date | auto_now_add=True, editable=False | DateTimeField
delivery_cost | max_digits=6, decimal_places=2, null=False, default=0 | DecimalField
order_total | max_digits=10, decimal_places=2, null=False, default=0 | DecimalField
grand_total | max_digits=10, decimal_places=2, null=False, default=0 | DecimalField
user_profile_id | on_delete=models.SET_NULL, null=True, blank=True, related_name='orders' | ForeignKey to UserProfile
original_cart | null=False, blank=False | TextField
stripe_pid | max_length=254, null=False, blank=False | CharField

#### OrderLineItem Model
**Notes:**
- Is created after an Order is created as it relies on the Order to work.

| Column Name | Validation | Field Type |
 --- | --- | ---
quantity | null=False, blank=False, default=0 | IntegerField
lineitem_total | max_digits=6, decimal_places=2, editable=False, null=False, blank=False | DecimalField
order_id | on_delete=models.CASCADE, null=False, blank=False, related_name='lineitems' | ForeignKey to Order
product_id | on_delete=models.CASCADE, null=False, blank=False | ForeignKey to Product

### Contact App
#### Email Model
| Column Name | Validation | Field Type |
 --- | --- | ---
email | blank=False, null=False | EmailField
name | max_length=60, blank=False, null=False | CharField
subject | max_length=254, blank=False, null=False | CharField
message |  | TextField
date | default=timezone.now | DateTimeField

### Products App
#### Category Model
| Column Name | Validation | Field Type |
 --- | --- | ---
name | max_length=254 | CharField
friendly_name | max_length=254, default='' | CharField

#### Product Model
| Column Name | Validation | Field Type |
 --- | --- | ---
name | max_length=254, default='' | 
description |  | TextField
price | max_digits=6, decimal_places=2 | DecimalField
image | default='default.png', upload_to='product_images' | ImageField
date_added | default=timezone.now | DateTimeField
admin_tags | max_length=40), size=8 | ArrayField
is_unique | default=True, blank=False, null=False | BooleanField
stock | default=1, blank=False, null=False | SmallIntegerField
size | max_length=2, default='', blank=True | CharField
popularity | default=0, blank=False, null=False, editable=False | IntegerField
times_purchased | default=0, blank=False, null=False, editable=False | IntegerField
category_id | 'Category', null=True, blank=True, related_name='products' on_delete=models.SET_NULL, | ForeignKey to Category
stock_drop_id | 'StockDrop', null=True, blank=True, on_delete=models.SET_NULL, related_name='products' | ForeignKey to Stockdrop

#### Stockdrop Model
| Column Name | Validation | Field Type |
 --- | --- | ---
name | max_length=30, null=False | CharField
description | max_length=200, null=False | CharField
image | upload_to='stock_drop' | ImageField
date_added | default=timezone.now | DateTimeField
display | default=True | BooleanField

### Users App
#### Userprofile Model
| Column Name | Validation | Field Type |
 --- | --- | ---
billing_full_name | max_length=50, default='', blank=True | CharField
billing_phone_number | default='', blank=True | CustomPhoneNumberField
billing_postcode | max_length=20, default='', blank=True | CharField
billing_town_or_city | max_length=40, default='', blank=True | CharField
billing_street_address_1 | max_length=80, default='', blank=True | CharField
billing_street_address_2 | max_length=80, default='', blank=True | CharField
billing_county | max_length=80, default='', blank=True | CharField
billing_country | blank_label='Country', default='', blank=True | CountryField
shipping_full_name | max_length=50, default='', blank=True | CharField
shipping_phone_number | default='', blank=True | CustomPhoneNumberField
shipping_postcode | max_length=20, default='', blank=True | CharField
shipping_street_address_1 | max_length=80, default='', blank=True | CharField
shipping_street_address_2 | max_length=80, default='', blank=True | CharField
shipping_town_or_city | max_length=40, default='', blank=True | CharField
shipping_county | max_length=80, default='', blank=True | CharField
shipping_country | blank_label='Country', default='', blank=True | CountryField
user | on_delete=models.CASCADE | ForeignKey to User
liked_products | blank=True, related_name='users', through='Liked' | ManyToManyField to Product

#### Liked Model
| Column Name | Validation | Field Type |
 --- | --- | ---
product_id | on_delete=models.CASCADE | ForeignKey to Product
userprofile_id | on_delete=models.CASCADE | ForeignKey to Userprofile
datetime_added | auto_now_add=True | DateTimeField

----

# Technologies Used
## Languages
- [Python](https://www.python.org/)
    * Using Django and other plugins to develop the app.
- [HTML](w3.org/standards/webdesign/htmlcss)
    * Page markup.
- [CSS](w3.org/standards/webdesign/htmlcss)
    * Styling.
- [SASS](https://sass-lang.com/)
    * Used to customise Bootstrap and CSS styles.
- [Javascript](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
    * Running functions for interactive components, AJAX, etc.


## Frameworks
- [Django](https://www.djangoproject.com/)
    * The main web framework technology for the project.
- [Bootstrap4](https://getbootstrap.com/)
    * Used for basic styles and outline.


## Libraries
- [JQuery](https://jquery.com/)
    * Animations and click functions.
- [Google Fonts](https://fonts.google.com)
    * Font Styles.
- [Bootstrap Icons](https://icons.getbootstrap.com/)
    * Used for icons.
- [Waypoints](http://imakewebthings.com/waypoints/)
    * Used for infinite scroll on feed pages.
- [Stripe](https://stripe.com/)
    * Used for processing payments securely.


## Packages
- [boto3](https://github.com/boto/boto3)
    * Used for configuration and Management of AWS
- [coverage](https://github.com/nedbat/coveragepy)
    * Measures lines of code tested.
- [dj-database-url](https://github.com/jacobian/dj-database-url)
    * Parses databse URLs for django.
- [django-allauth](https://github.com/pennersr/django-allauth)
    * Parses databse URLs for django.
- [django-compressor](https://github.com/django-compressor/django-compressor)
    * Django-sass-processor uses this for offline compiling.
- [django-countries](https://github.com/SmileyChris/django-countries)
    * Provides form and model fields for country selection.
- [django-crispy-forms](https://github.com/django-crispy-forms/django-crispy-forms)
    * Form parsing, styling and formatting.
- [django-phonenumber-field](https://github.com/stefanfoulis/django-phonenumber-field)
    * Provides model and form fields for inputting phone numbers in a set format.
- [django-sass-processor](https://github.com/jrief/django-sass-processor)
    * Processes the SASS files into CSS files when app is run.
- [django-storages](https://github.com/jschneier/django-storages)
    * Creates custom storages for use with AWS.
- [djangoajax](http://yceruto.github.io/django-ajax/)
    * Provides a decorator that sends a view response in JSON format.
- [gunicorn](https://gunicorn.org/)
    * Server deployment on heroku.
- [pillow](https://github.com/python-pillow/Pillow)
    * Provides tools for image manipulation.
- [psycopg2](https://github.com/psycopg/psycopg2)
    * Adapter for use with a Postrgres Database.
- [whitenoise](http://whitenoise.evans.io/en/stable/)
    * Used to deploy static files locally during production.


## Platforms
- [Amazon Web Services](https://aws.amazon.com/)
    * S3 Bucket used for static file hosting
- [Coveralls](https://coveralls.io/)
    * Tracks code coverage statistics.
- [Github](https://github.com/)
    * Storing code remotely.
- [Gitpod](https://gitpod.io/)
    * IDE for project development.
- [Heroku](https://www.heroku.com/)
    * Platform for production deployement.
- [Travis CI](https://travis-ci.org/)
    * For CI testing and automatic deployment.


## Other Tools
- [Balsamiq](https://balsamiq.com/)
    * To create wireframes.
- [Croppola](https://croppola.com/)
    * Quick image cropping tool.
- [DBeaver](https://dbeaver.io/)
    * Generate Diagrams for the database.
- [Mockup Generator](https://techsini.com/multi-mockup/index.php)
    * For device mockup images.

----

# Testing
## Automated Testing
### Validation
- HTML has been validated with [W3C HTML5 Validator](https://validator.w3.org/).
- CSS has been validated with [W3C CSS Validator](https://jigsaw.w3.org/css-validator/) and auto-prefixed with [CSS Autoprefixer](https://autoprefixer.github.io/).
- Links checked with [W3C Link Checker](https://validator.w3.org/checklink).
- Each javascript file was tested on the site for errors and functionality using the console and with [JSHint](https://jshint.com/).
- Python has been validated using the [Microsoft Python Linter](https://code.visualstudio.com/docs/python/linting)

### Python Testing
**Notes:**
- Tests have been written for views from the outset and maintained throughout the project development.
- Tests are maintained within separate folders in each app.
- After the initial development, merges to master have been committed solely from the testing branch after testing has completed, ensuring less chance for error.
- A secondary, persistent, PostgreSQL test database has been utilised on [Heroku](https://www.heroku.com/). This way the test database functions more similarly to the production database, with items being added and persisting. This allows for more accurate testing and test views which function on a real Postgres database. Testing must be run with the option `--keepdb` to maintain the database's persistence.

#### Running Tests
1. Activate the virtual environment with the [deployed](#deployement) code.
2. Input the following code into the terminal:
    ```
    python manage.py test --keepdb
    ```
3. Test specific apps with:
    ```
    python manage.py test <app name> --keepdb
    ```
4. Results will be shown in the terminal.

### Coverage
**Notes:**
- [Coverage](https://github.com/nedbat/coveragepy) has been used throughout the project to ensure the majority of my code has been tested.
- I test the majority of code I have written, while excluding code that derives from Django or other packages (specifically [django-allauth](https://github.com/pennersr/django-allauth)) utilised in this app. Additionally, I do not test the webhook files utilising [Stripe](https://stripe.com/) webhooks, but test similar code I have written as faking the webhooks seems to necessitate utilising the Stripe dashboard manually. In the future, I will attempt to write code for this.

#### Running Coverage 
1. Activate the virtual enviroment with the [deployed](#deployement) code.
2. Input the following code into the terminal:
    ```
    coverage html
    ```
3. Or, to test all code I have personally written for the app excluding the webhooks, write:
    ```
    coverage run --source=. --omit=custom_storages.py,checkout/webhook*,config/*,manage.py,users/adapter.py manage.py test --keepdb
    ```
4. Open `index.html` in the newly created `htmlcov` folder.

### Travis CI
- [Travis CI](https://travis-ci.org/) was utilised from the beginning of the project to maintain [build testing history](https://travis-ci.com/github/Ri-Dearg/neverlost-thrift).
- Travis will automatically deploy the master branch of the project to Heroku if the build passes.
- Travis will also run coverage and pass the result to [Coveralls](https://coveralls.io/) on testing success.

### Coveralls
- Testing history can be found [here](https://coveralls.io/github/Ri-Dearg/neverlost-thrift)
- [Coveralls](https://coveralls.io/) was recently implemented to maintain build coverage history.
- Coverage info is generated utilising:
    ```
    coverage run --source=. --omit=custom_storages.py,checkout/webhook*,config/*,manage.py,users/adapter.py manage.py test --keepdb 
    ```

## Manual Testing
### General Testing
- Each feature was developed and tested in its own branch before being pushed to master.
- Each time a feature was added, all the functions were tested to see if there was an impact.
- The views have been thoroughly manually tested and refined over time, utilising python features to create documents in the database in a useful, flexible structure.
- The site was sent to friends for feedback and testing.
- There is a console log notification that states whether debug mode is off or on.
- All forms have validation and will not submit without the proper information.
- .gitignore file has been included to prevent system file commits.

### Mobile Testing
- I tested the site personally on my Android device, going through the entire process, checking buttons, functions, checking out, etc.
- The site was sent to friends and relatives for them to follow the same process. They have tested on their devices, including iOS.
- Chrome was utilised to inspect the site in mobile format, going through the pages and functions.

### Desktop Testing
- The site was developed on a Chromebook and, as such, the majority of testing occurred on Chrome.
- The site was tested by friends and relatives on numerous desktop devices.
- The site was marginally tested on other browsers, such as Firefox and Edge.
- Internet Explorer was not tested and the site was not developed with it in mind as support for the browser is gradually being dropped.


## Bugs
### Known Bugs
- A user reported that the "Orders" button does not function in the desktop view. I have been entirely unable to replicate this bug on several browsers and devices.
- Heroku does not compile the SASS from the [django-sass-processor](https://github.com/jrief/django-sass-processor) automatically, meaning CSS is missing. I resolved this by creating a post_compile file with the code:
```
cd "$1" || exit 1
python manage.py compilescss --traceback
python manage.py collectstatic --noinput --traceback
``` 
However, the project seems to always run `collectstatic` no matter what the settings are on Heroku or Django using this method. This results in a large number of PUT requests for AWS. It seems there is no clear workaround but I would like to find one. I may look into utilising [Collectfast](https://github.com/antonagestam/collectfast).

### Fixed Bugs
- Occasionally the Product Box icons would display incorrectly when buttons are clicked incredibly quickly. Fixed by utilising the `object` HTML tag for caching.
- I was unable to utilise Django Postgres specific features for my DB or run tests on it. Fixed by utilising two Postgres servers on Heroku as default databases.
- Icons in the navbar would jump position during their fade-out animations. Fixed by setting bootstrap `col` to a fixed grid number rather than `auto`.
- Debug mode was on during production. Fixed by removing `DEBUG=False` from config vars.
- Allauth consistently redirected users to unused allauth pages and templates. Fixed by creating a custom Adapter and Custom forms for more customised redirections.
- Different Users could view other user's orders. Fixed by setting the user context to the request's user. The same issue occurred with User Profiles with the same fix.
- Users could buy more stock than is available. Fixed by setting max item quantity to stock on adding a product or purchasing a product.
- After Liking and Adding to cart had been set to use AJAX, the popovers wouldn't update. Fixed by creating views which refresh the context and re-render the templates and are re-loaded by Javascript after success.
- The total on the cart page would not refresh on deleting the item or changing the quantity. Fixed by the same method above.
- The `PhoneNumberField` in forms had validation that was too strict and caused errors during checkout. Fixed by creating a custom validator.
- The `PhoneNumberField` was not processed correctly in orders. Found out it separates into two separate fields before concatenating. Added manual concatenation.
- If an anonymous user liked products before logging in or creating an account the items would be lost on logging in. Fixed by transferring the session items to the new account on login with a signal.
- Toasts were positioned under the preloader. Fixed by changing the z-index.

----

# Deployment
## Local Deployment
### Local Preparation
**Requirements:**
- An IDE of your choice, such as [Visual Studio Code](https://code.visualstudio.com/)
- [Python 3](https://www.python.org/downloads/release/python-385/)
- [pip](https://github.com/pypa/pip)
- [Git](https://git-scm.com/)
- A Postgres database set up.
- A free account with [Stripe](https://stripe.com/).
- You may use a free account at [Amazon Web Services](https://aws.amazon.com/) for static file hosting.
- Alternatively, the project comes with [whitenoise](http://whitenoise.evans.io/en/stable/) installed for static file hosting in production directly from Django.
- You will have to set up a connection with an email server, or write the following code in `settings.py` to see the emails in the terminal:
    ```
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
    ```

### Local Instructions
1. Download a copy of the project repository [here](https://github.com/Ri-Dearg/neverlost-thrift/archive/master.zip) and extract the zip file to your base folder. Or you can clone the repository with:
    ```
    git clone https://github.com/Ri-Dearg/neverlost-thrift
    ```
2. Open your IDE and choose the base directory.
3. I recommend running the program Python's virtual environment with:
    ```
    python3 -m .venv venv
    ```
    - Setting up a virtual environment can differ from system to system, please see [python documentation](https://docs.python.org/3/library/venv.html) for more info. The site can also be run without setting up a virtual environment.
4. Run the virtual environment.
    ```
    .venv\Scripts\activate
    ```
5. Install project requirements with:
    ```
    pip3 -r requirements.txt.
    ```
6. Set up the necessary environment variables in your IDE.
    Personally, I created an env.py and then imported it into settings.py. The project is set up to look for this file so it may be useful for you to do the same, however, do not include this in commits or for production.
    The necessary variables are as follows:
    ```
    'SECRET_KEY', <key>
    'DATABASE_URL', <key>
    'HEROKU_POSTGRESQL_CRIMSON_URL', <key>
    'STRIPE_PUBLIC_KEY', <key>
    'STRIPE_SECRET_KEY', <key>
    'STRIPE_WH_SECRET', <key>
    'AWS_ACCESS_KEY_ID', <key>
    'AWS_SECRET_ACCESS_KEY', <key>
    'AWS_STORAGE_BUCKET_NAME', <key>
    ```
    - Certain variables may not be necessary based on your setup, but the `settings.py` file will need to be modified accordingly.
    - Make sure your server is in the `ALLOWED_HOSTS` setting in `settings.py`
    - The `HEROKU_POSTGRESQL_CRIMSON_URL` is used as the testing database.
    - the AWS variables can be removed and changed in favour of Whitenoise with some alterations in `settings.py`.
    - The variables `DEBUG` and `DEVELOPMENT` can be added if in development.
7. Run the migrate command to create the data tables.
    ```
    python manage.py migrate
    ```
8. Create a superuser with username and password:
    ```
    python manage.py createsuperuser
    ```
9. Run the local server:
    ```
    python manage.py runserver
    ```
10. The site should now run and be accessible. Login to the admin area and create some models to see the site features.

## Heroku Deployment
### Heroku Preparation
- It is possible to copy or clone the repository to directly deploy it to Heroku without any changes, only adding environment variables. If you wish to customise the repo please check the details below.
**Requirements:**
- A `requirements.txt` file created with `pip freeze > requirements.txt`.
- A `Procfile` with the command `web: gunicorn config.wsgi:application`.
- Adjust `ALLOWED_HOSTS` in `settings.py` to your deployment hostname.
- A folder `bin` in the base directory with a `post_compile` file inside. This is necessary to run the CSS compiling. The file must contain the following text:
```
#!/usr/bin/env bash

cd "$1" || exit 1
python manage.py compilescss --traceback
python manage.py collectstatic --noinput --traceback
```
- A free account with [Stripe](https://stripe.com/).
- You may use a free account at [Amazon Web Services](https://aws.amazon.com/) for static file hosting.
- Alternatively, the project comes with [whitenoise](http://whitenoise.evans.io/en/stable/) installed for static file hosting in production directly from Django.

### Heroku Instructions
1. Copy or clone the repository.
2. `git add`, `git commit` and `git push` to a GitHub repository.
3. Create an app on [Heroku](https://www.heroku.com/), selecting a name and region.
4. Click on 'Deploy' in the menu, and select the Github repository from the menu. Confirm that you are linking the correct repository. Do not yet deploy it.
5. Go to the 'Settings' section and click on 'Reveal Config Vars'.
6. Input the same environment variables as listed in step 6. of [Local Instruction](#local-instructions).
7. Continue on to follow steps 7 and 8 in your IDE. You can also create add product models, etc during this step if you wish. Repeat step 7.
8. Return to the 'Deploy' section and manually deploy the repository.
9. Click the 'View App' button and everything should be up and running!


## Credit and Contact
### Images
Images were all taken from Unsplash and do not require the photographer's credit. However, all images utilised throughout the project can be found in [this collection](https://unsplash.com/collections/10623069/neverlost-thrift) where their credit can be seen.

### Code
- Any code utilised from another programmer is documented and credited within the code.
- Much of the stripe webhook details have been taken from the [Code Institute](https://codeinstitute.net/) lessons, utilised and changed for my needs.

### Contact
Please feel free to contact me at `sheridan.rp@gmail.com`
