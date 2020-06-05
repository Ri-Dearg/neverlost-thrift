# Neverlost Thrift

<!-- The site is desgined as a text-base story sharing platform based around the coronavirus epidemic. Its goal is to allow people to post, share and search experiences and opinions on the site. The inspiration came from the various ways people have begun to use social networking during the epidemic, in manners not sen before. I wanted to create a site which is based more on thoughtful exploration rather than instant gratification, such as Instagram or Facebook, but still allow for personalisation. Certain design choices which would be out of line with similar systems were made deliberately and will be explained. -->

Link to deployed project [here](https://neverlost-thrift.herokuapp.com/).

## UX

<!-- ### Home Page

#### First Impression
##### Initial Viewing
The home page is desgined as a feed, with infinite scrolling, much like many social networks. A page preloader with a slow fade is placed covering content on all pages, the z-index has been placed under the navbar and mneu button, so they persists from one page to the next.
A different random quote on the topic of sharing is pulled from a hand-picked selection will be displayed as the Home page central graphic. I previously had a chart with information on the virus, but the further I developed the site, the less it was in theme. So, I chose a random quote, which I hope will help set the tone by having visitors reflect before reacting.
The style is simplicistic, minimalist and clean to create clear focus rather than busy distration.
On the very first load of each session, an alert will pop out from the floating menu to alert the user of its presence.
Many actions will pop up a flashed color coded messeage for confirmation and user feedback.

#### Navigation
##### Navbar
The navbaar is simple and clean. Kepping in theme with the idea of text, no imagery has been used for the logo. The authourisation functions switch depending one whether or not the user is logged in. Signup, login, profile and logout are always highlighted no matter the page. This is to encourage interaction with these functions in particular, as well as create preference for, and push users towards, the colorful, eye-catching floating menu button, where the key site functions are, while simultaneously diminishing the importance of the basic navbar items.
The mobile and side nav have been placed to the right for ease of use with one hand, favouring the right-handed majority.

##### Floating Fixed Menu
I'm utillising this menu as the main point of interaction and navigation for the site. All pages on the site can be accessed through this menu and some features are exclusive to it. On desktop it opens on hover, on mobile with a tap, positioned bottom-right for the same reaason as before. It hovers above the preloader to maintain importance to the same degree of the nav.
It uses a bright and colorful palette to catch the eye. The menu items are tooltipped and color coordinated for clarity. The green button also changes on context between signup/login/profile/home. Each button opens a modal except the button for the aformentioned green button.
All forms in the modals have helper text and validation where necessary for user feedback. The signup login form uses tabs to offer both options. The Post a story option allows people to preview a color by holding down on it before posting.

#### Feed
##### Story Section
Under this there is a "Featured" story section that is displayed first, followed by an non-featured story section. Feature stories are automatically set at 21 likes, but for the purpose of this project I have manually set some for display purposes.
The stories in each section are ordered reverse chronologically, most recent first. The story list from the database will pull 100 stories maximum, featured and non-featured inclusive.
Infinite Scroll is used to avoid pagination and create the social media-like feed. The scroll has a loading icon for feedback, gives an alert when the content has ended and when there are connection issues.

##### Story Cards
Each story has a card as a basic design, with a user-selected color from a set palette, allowing for personalisation but maintaining a coherent style. Each card is has its content truncated at 180px to maintain a consistent size and give a preview of the story. The story can then be opened to full height.
Each card displays basic info about the writer and allows the main content to have stylised text formatting.
If logged in, a like button will be present, which uses ajax to perform form submission in the background. On click the icon will change and deliver a short recognition sound. Likes are only displayed after a user clicks the like button, and only temporarily. This is a deliberate choice to deliver a familiar system but diminish its importance. The reason being to like something if it interests you, and not solely because it is popular. While it is possible to like and unlike something to see the number, it requires extra effort that will likely dissuade the average user.
Tags are always on display so the viewer can get an idea of the theme. Each one is a link to a search page on that tag. The search uses a text index and does not filter posts by tag. This was a choice as to also include content which may have the keywords but not list the tag, however the tags carry a higher importance weight in the index, so they will always be prioritised. A specific per-tag search was tried but I preferred the weighted text search.

### Profile Page

#### User Feed
##### Edit Menu
The profile page is made of two tabs. A user story feed and a user settings section. The user story feed has functions the same as the main feed but with two main differences. Firstly, all stories are filtered to only user-created stories. Secondly, each story has an edit button instead of a like button.
The edit button opens has a differerent color to differentiate it from the main menu and will sit just to the right of the main menu button on small screens, displaying a menu perpendicular to the main meu, to not have menu tooltips clip.
It has two color-coordinated options, edit and delete. Both pull up modals, the edit story being pre-filled with the story info.

#### User Settings
##### Layout
The layout is standard with the rest of the site with buttons sitting on the right. Sections have dividers for clarity and the delete buttons are centered for clarity.
User can opt to input basic data that will prefill their for data when posting a story, if any info is saved, a button to delete the info is shown.
All forms have helper text. The delete options have modals that require password input to confirm the decision.

### Search, About, Contact

#### Search
The searchpage returns results either sorted by tectscore if text was entered, or within the range requested in the search form. The page is essentially the homepage, with all features bt with filtered results.

#### About
A simple page explaining the site.

#### Contact
Another simple form field that uses flask-mail for email.

### Fonts, Colours

#### Fonts
THe font choices were based on the idea of reading a book, sp a styles fitting the theme were picked. However, when writing a story, users may choose their own fonts in the story content.

#### Colours

##### Main Palette
![Main Palette](https://user-images.githubusercontent.com/44118951/81061325-7081ff00-8ed4-11ea-94d9-5e01ace77669.png)

##### Story Cards
![Story Card 1](https://user-images.githubusercontent.com/44118951/81062707-c2c41f80-8ed6-11ea-86b0-355dd042702c.png)
![Story Card 2](https://user-images.githubusercontent.com/44118951/81062698-c061c580-8ed6-11ea-843c-78bd4eb94521.png)


Colors were chosen from the Materialize CSS palette for ease of use with classes in dynamic content. I mainly targeted bright, bubbly colors to give life to what is essentially a slow, patient content. 
THe main background color anf the nav color are utilised to give a sense of clam.
The main menu button colors are used to represent certain ideas throughout the entire site, so you'll find them reused in forms and menus. The cards have a set palette of colors to choose from. I chose a subset that was a balance between impact, boldness and readability. The colors allow each person to give a bit more character to their story card. The colors are kept simple and clean and the use of dark tones is avoided, reserved for text. Shadows are used appropriately to give a sense of depth.

### User Stories
As a user interested in reading stories, I expect to see a many different perspectives..

As a user interested in writing, I expect to be able to share my stories.

### Wireframes
Wireframe: https://drive.google.com/open?id=1qIyntbCbm1Q0vOoC849uHAyfC5QICYAL -->

## Features

### Features implemented
- General
    - App structure
        - All templates and static files are held in the base directory and then in respective app folders, rather than within the app folders. I thik this maintains clearer , more cosistent directory structure.
        - SASS has been utilised for greater customisation of [Bootstrap4](https://getbootstrap.com/)
        - The SASS auto-compiles a css file when the app runs, so only source files are to be edited and css files are never commited.
    - Security
        - All sensitive information is stored in environment variables and hasn't been commited.

<!-- - Content
    - Story Creation
        - Edit text using a custom-built CKEditor for font styles, colors, sizes and other features
        - Post anonymously without logging in, but cannot like stories
        - Choose from a range of colors for the post
        - Text limit of 40,000 characters
        - Card colors can be previewed on the select dropdown by hover, or holding on mobile
    - Story Display
        - Featured stories displayed above others after passing a set number of likes
        - Stories are ordered chronologically by a millisecond timestamp, and converted to a readable date
        - Stories auto size height, that can be truncated with long stories
        - Trucated text that can be expanded and closed
        - Like stories asynchronously, with sound and notification for the action
        - Simple card format, all evenly sized for uniformity when scrolling
        - I give everything one like as a thanks for posting
    - Search
        - Form requires data which is then used to search through stories
        - Add tags, which are linked to search facility
        - Tags are weighted heavier in the search index and mixed with content for a full text search
        - Date and age ranges for search
        - All search field are optional, mix any details
        - Country and language search filter the results
        - The database makes use of arrays, integers, booleans and embedded documents to fully utilise the search abilities.

- Users
    - Authentication
        - flask-login manages users
        - A USer Class was created for a blueprint
        - Users can securely create an account with a hashed password
        - Patterns are required for both usernames and passwords
        - User can signup using only a username and password. I recently used typing.com and was refreshed to find they required no email. I decided to follow suit.
        - Can use the "Remember me" function to stay logged in
        - Can change password securely
        - Can delete all users stories while keeping the account
        - Can delete account while leaving posted stories, user information is stripped from the story
    - Content
        - Registered users can like stories
        - Ragistered users have their stories saved to their account
        - Users can edit or delete any created stories
        - Users can fill in autofill info to use when posting a story
        - Users can delete their autofill info


        - The app has been designed as a module, utilising an __init__.py file for configuration of the app
        - The site utilises blueprints that are imported into the main app creation, one for the majority of views, and the other for views requiring secure authourisation
        - Extensions.py has been utilised, along with blueprint, to avoid circular imports
        - config.py has been created for environment variable storage
        - models.py has been utilised to create a User Class for flask-login.
        - The other details follow standard practice for a flask app
        - a gitgnore file is included
        - environment variables have never been written in the app, let alone committed
        - the procfile utilises gunicorn for initialisation
        - The distribution includes a custom-built CKEditor API with a particular set of plugins.
    - Utility
        - Infinite Scroll has been applied to all feeds.
        - Preloader placed over content but under menus
        - Nav and menus placed on the right for one-handed use
        - Menus utilise tooltips for clarity        
        - Nav options change depending on location and authentication.
        - Flashed messages pop up for user feedback
        - flask-mail is used for the contact page
    - Colors
        - Site is color co-ordinated for cheerfullness.
        - Buttons and themes are color co-ordinated to give for clearer, more uniform recognition of function
    - Other 
        - Random quote on site index
        - Utilises Material Design to give a sense of depth
        - Flashed messages have styled categories
        - Clean, minimal and colorful -->

### To Explore / Do

<!-- - Content 
    - Share button for each card
    - Tag-specific more restricted search
    - More quotes for index

- Users
    - Email entry for password recovery using flask-mail
    - A tab that displays like stories
    - A friend / follow system
    - edit and like buttons for users on their own cards on all pages

- General
    - Change to Bootstrap / Foundation CSS
    - Implement alternative tagging system - Materialize Chips is buggy
    - Work on mobile font-size formatting (I don't currently have access to enough phones for this)
    - More testing on views and debugging 
    - Italian language site
    - Optimize Edit Modal creation on user page. Right now the page is bloated and I can definitely optimize it. -->

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
    <!-- - [Material Design Icons](https://material.io/resources/icons/?style=baseline)
        * Used for icons
    - [Google Fonts](https://fonts.google.com)
        * Font Styles
    - [Infinite Scroll](https://infinite-scroll.com/)
        * Used for infinite scroll on feed pages -->

- Packages
    - [django](https://www.djangoproject.com/)
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
        * Server deployment on heroku

## Testing & Troubleshooting
- Validation
    <!-- - All forms have validation and will not submit without the proper information.
    - Links checked with [W3C Link Checker](https://validator.w3.org/checklink)
    - HTML has been validated with [W3C HTML5 Validator](https://validator.w3.org/)
    - CSS has been validated with [W3C CSS Validator](https://jigsaw.w3.org/css-validator/) and auto-prefixed with [CSS Autoprefixer](https://autoprefixer.github.io/). There is a validation issue with margin-block-end but it is a valid value in all popular browser.
    - Each javascript file was tested on the site for errors and fucntionality using the console and with [JSHint](https://jshint.com/) -->
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
    <!-- - The views have been thoroughly manually tested and refined over time, utilising  python features to create documents in the database in a useful, flexible structure.
    - The documents in the database have been examined and structured in a manner so that the information is well defined, checking how the views effect documents.
    - The text index has been tested to include all string info, and excludes common text word searches.
    - Indexes for times, dates and ages have been included, ensuring that in search both full days are included.
    - Booleans are well utilised for automatic featuring, the function has been tested to fire.
    - On append re-initialising functions are fire by Infinite Scroll in order to ensure all features work correctly.
    - Initialising features have been grouped into two functions, based on whether they are required for all appended stories, or only stories on the profile page that require editing functions. If a new function needs to be created, it can easily be slipped into one of the two grouped functions, and it will easily function correctly on all pages.
    - I have tested the site and its layout on multiple android devices, different sizes, on multiple browsers. I was unable to test on iOS. Mainly developed and tested using chrome developer mode. It is fully responsive with a clean layout on each device.
    - Each feature was developed and tested in its own branch before being pushed to master.
    - Some tests were performed on views and were tested manually throuroughly. For example, every possible combination on search was tested.
    - I regret that, due to the amount of troubleshooting I had to do with the CSS, I was unable to fully utilise pythons's unittest framework. I made some simple views, but the CSS troubleshooting slowed down my app development to the point where I had to move forward with features to make the deadline. More testing is necessary in this area.
    - Each time a feature was added all the functions were tested to see if there was an impact.
    - The python module structure has been tested and implemented, adding config.py, setup.py and some tests.

    <!-- - Troubleshooting
    - Throughout devlopment I found my largest issues were caused by difficulties with Materialize CSS components. I sincerely regret using it, as I spent a lot of time debugging the CSS instead of developing features or creating test views. Bootstrap and Foundation are both more complex and therefore more flexible, perhaps more study is rewuired to utilise them well, but that suits me. The simplicity of Materialize may suit some developers, but I found it to be a hinderance.
    - The tags feature in Materialize "Chips" was something I implemented early on as the tag system, only to find out that when I began testing using real devices as opposed to developer mode, that it had fairly unfixalke bugs on android. To enter a tag, you must use the "Enter" key, however on android, within a form, the enter button becomes a "Tab" button. I edited the Materialize.js to allow using spaces, including keys for space on android, but it still would not register. This has been a known issue since 2018 In the end I found a workaround by implementing the Chips outside of the form, pulling the data from the tags and reinserting it as a list, key by key, into the form. This was just one of many issues I found and still have with the Materialize CSS.
    - Many of the components are inflexible, functioning well while used singly but buggy and requiring a lot of specific code editing when used in conjunction with one another
    - Tabs within a modal, for example, didn't have the active tab selected properly so I had to reinitiate it with specific settings.
    - Tooltips weren't fixed on the page for the action buttons, scrolling upwards on mobile devices, I simply had to create my own.
    - Z-indexes have a bizzare order, placing less relevant components under or over others, seemingly randomly. The action buttons themselves had z-indexes above the Nav, as well as modals, so scrolling on the user page left buttons clipping, I had to edit z-indexes.
    - Bullet points removed by default in styles
    - Some form components recognise "required" attribute, other do not, validation only functions on some of fields, requiring custom code. The list goes on.
    - Documentation was missing, ouright incorrect, or messy in many parts. There were classes that didn not function as described, and examples that weren't connected to the information.
    - Troubleshooting database issues was relatively easy. As this is my first project utilising the database, a little bit of study in the dcumentation to learn syntax was usually enough.
    - I came accross issues with cirular imports when writing the app, and found that the best solution was to scale the app up a little from a single app.py, to a module. This allowed me to avoid circular imports, keep the the app information organised and make the app nicely distributable.
    - I began trying out creating an app-factory but found it was overkill for my purposes.

    <!-- ## Deployment
    <!-- There are a number of methods for deployment
    <!-- 1. Setup.py
    1. A setup.py file has been created for easy deployment.
    0. At a python terminal you can run "python setup.py sdist" to create a source distributable
    0. This can then be unpacked, and the module be installed by running python "setup.py install" from its directory.
    0. This will install the package for modification.
    0. This will allow you to run the program locally, if you wish
    0. To deploy the app online you will have to utilise a PaaS, such as Heroku, or an alternative.
    0. Ensure debug is set to False, and take a look at the config.py to see which environment variables will need to be set.
    0. Set the config variables as you need in you chosen PaaS.
    0. Ensure all packages from requirements.txt are installed.
    0. Push the files to the PaaS and deploy.

    <!-- 0. Github
    1. Fork the repo on github.
    0. Push the repo to a PaaS, such as Heroku.
    0. Set the environment variables, ensure debug is False.
    0. Deploy and your good to go.

    <!-- ## Credits

    <!-- ### Content
    <!-- Stories provided by actual people.
    <!-- Any code utilised from another programmer is documented and credited within the code.
    <!-- Infinite Scroll is utilised under its Open Source license for personal projects.
    <!-- ### Media
    <!-- - Sound:
    - Title: Blop
        Uploaded: 03.27.13
        License: Attribution 3.0
        Recorded by Mark DiAngelo
    - Title: Pop Cork
        Uploaded: 06.09.09
        License: Attribution 3.0
        Recorded by Mike Koenig -->