README.md
![Planr Base Mockup](static/images/am_I_responsive.png)


[View deployed site here](http://plant-base-project.herokuapp.com/home)

## Introduction
The last 18 months have seen many of us confined to our homes for extended periods of time, and increasingly our homes are in urban settings with little or no green outside space. These are some of the reasons attributed to a recent surge in interest in houseplants. There are numerous benefits to keeping houseplants: they are relatively inexpensive; they allow us to connect with nature, they satisfy our primal urges to care and nurture, and in the uncertain times created by the global pandemic, they offer a sense of calm reassurance to many people. Best of all, you can talk to them  (and of course, they don’t answer you back!)

So what are the downsides I hear you cry, it can’t all be blissful green-fingered-fun? Well, caring for houseplants can be tricky. I have certainly presided over the decline of one (or two!?) in my time, but thankfully with a bit of basic guidance and species specific knowledge, anybody can successfully grow a healthy houseplant.

Plant Base is an interactive web application that gives users access to a wealth of information on caring for houseplants. Users will be able to access recipe style cards or ‘tip-sheets’, which contain useful information on caring for a variety of houseplants. Users will be able to search for specific plants. They will be encouraged to create an account so that they can build their own personal collections, where they will also be able to upload and edit their own tip sheets to be shared with other users.

## User Experience

Here I will address the aims and goals of the application from both the perspectives of the user and of the owner. I will also address how user experience is key to the design of the application.

### User stories

##### As a new user I want 

* To quickly understand the purpose of the site and the benefits it can offer me
* To be shown relevant content that is visually pleasing
* To be able to browse through the sites content without needing to create an account
* To be able to view individual plant sheets
* To be able to search for specific plants
* To be signposted to any associated social media accounts
* To be able to access useful links and other applicable resources
* To be able to register as a new user quickly and easily

##### As a registered user I also want

* To be able to login in to my account quickly and easily
* To be able to upload my own care sheets for others to use, and for this process to be straightforward and quick.
* To be able to edit my own care sheets quickly and easily
* To be given guidance on how and what to input on when creating a sheet
* To be able to delete my own care sheets
* To be able to quickly access all of my own care sheets 
* To be able to navigate around the site quickly and cohesively
* I would like to the site to use icons that help me to quickly understand the information being presented to me

##### As the site owner I want

* To be able to edit and delete any content from the site
* To be able to control the flow of information uploaded to the care sheets in order to retain a consistent presentation across the site
* That the user be presented with clear instructions to guide them when creating a sheet.
* That input validations are used to control the validity of the data uploaded by the user
* Preventative “server-side” checks to ensure that only registered users can upload to the site.
* A default image to be loaded if a user does not upload one or if there is an error with the upload.
* That if the requested page does not exist a custom page is loaded that directs the user back to the site


### Design Objectives

* Mobile first, user friendly design
* Intuitive layout, easy to navigate
* Minimal design asthetic to inspire a sense of 'nature' and 'calm'
* Light airy pastel colours used to reinforce the design
* Use of icons where applicable, but in keeping with a minmalist design asthetic
* Design adheres to current norms and conventions e.g clear navigation, icons.
* Accessibility – content is accessible to as many users as possible – clear text, sufficiently contrasted to the background, ‘alt’ tags and ‘aria’ labels used appropriately.

### Design Choices

#### Colours

![Colour Pallet](static/images/colors.png) source www.coolers.co
* The main site color will be green. In keeping with the plant theme and to adhre to a pastel pallete (#9EC2AF) 
* The site background is white (#FFFFFF)
* The cards and boxes will be a very light grey (#FAFAFA)
* Button will have a  grey hover colour of (#777777)
* In addition the flashed messages and information/warnings will use Bootstraps warning yellow (#FFC107)    
 ![Yellow](static/images/yellow.png)

#### Fonts

* The majority of the site uses [Arial](https://www.fonts.com/font/monotype/arial) for its neutral ashthetic
* The Quick Fact Sheets will use [Roboto Mono](https://fonts.google.com/specimen/Roboto+Mono)  in order to give a 'quick', 'informative' feeling to the user
* Text color will be a soft black (#313232)

#### Bootstrap

* I have the CSS framework [Bootstrap](https://getbootstrap.com/) to achieve a design consistency across the site. Bootstraps responsive breakpoints have been utilised to ensure the site layout is responsive across all viewports and devices 
* Buttons - The sites buttons will all be Boostrap's 'Outline Secondary', again they have a neutrality that will compliment rather than distract from the sites color 
* I have used Bootstrap's modals, cards, alerts and forms and responsive navbar, throughout the site to achieve a uniformity of design that is visually pleasing and responsive.

### Initial Planning

#### Wireframes

My initial wireframes can be seen [here](static/images/wireframes)

I have largely stuck to my initial vision for the site in terms of the layout and design. Some features were not implemented due to practical time constraints. I detail this further in the 'features left to implement' section.

#### Site Layout

My initial layout and functionality plans can be seen [here](static/images/site_maps).
These were really useful in developing and building the site. Again not all features were implemented and I elaborate on this in the features section.

#### Database 

I choose to use [MongoDB](https://www.mongodb.com/) to store and access all the data for the site.  
My database schea plans can be viewed [here](static/images/site_maps).
Initially I had planned to have two collections, one for the plant sheets and one for users, but this was expanded to three to include a categories collection in order to better group the sheets. For the purposes of this site, categories could have been part of the sheets collections, but with an eye on future facilitate scalibility it was added as a seperate collection.  MongoDB was the right choice for my purposes as there is not a lot of relational data sets, and the flexibility it offers is key.

### Features

#### Site Header and Footer
* Strap at the top of the site to frame he page and to deliver a headline of the sites aim
* Site logo in the top left that links to the home page
* Navigation menu - items change dependent on whether the user is logged in
* User Logo in the top right, shows if the user is logged out, or displays their userbame if logged in
* User logo hidden on mobile navbar to reduce cluttering
* User logo links to login if the user is not logged in, or to profile page if they are
* Footer displays the social media icons (for demonstration, not currently active)
* Footer navigation menu shows key navigation items so users can easily navigate from the bottom of the page

#### Home page
* Simple clean design
* Welcome paragraph, introduces the features of the site to users
* Buttons to get users on their way, buttons change depending on wheteher the user is logged in

#### Login Page
* Simple clean design
* Icons used to incease accessibility
* Supporting instructive text
* Toggle button to hide/view users password
* Form validation in place to require input and in the correct format
* Backend checks that the username and password match the databse
* User feedback provided by flashed messages
* Link to register now, if the user is not signed up

#### Regiser Page
* Simple clean design
* Icons used to incease accessibility
* Supporting instructive text
* Toggle button to hide/view users password
* Form validation in place to require input and in the correct format
* Confirm password field to ensure user enters their intended password
* Password hashing, to encrypt passwords for security
* Backend checks that the username is not already in use
* User feedback provided by flashed messages
* Link to login now, if the user is already signed up

#### Profile Page
* Greeting message flashed to the user upon signing in
* Username displayed, with a welcome message
* User logo in the navbar becomes un-checked and the users name is added
* Users care sheets displyed in a neat column, as a summary card
* Sheets are paginated to 6 sheets per page for convenience
* pagination links at the top and nottom of the column to aid navigation
* Button to view each sheet in more detail

#### View Sheet Page
* Plant image on the left of the screen
* Quick facts card shown on the right
* Plant care information summarised in succinct easily digestible fashion
* Light, water and feed information have icons to reinforce the meaning quickly and easily
* If the user is the sheet owner, edit and delete buttons are shown
* Plant name, botanical name and general care advice displayed underneath the image
* Sheet owners name displayed 
* Convenient buttons to return to the sheets page or the profile page

#### Add Sheet Page
* Neat and convenient form for users to create a new sheet
* Clearly labelled input fields
* Supporting instructive text
* Form validation in place to require input, and ensure the correct format
* Dropdown boxes allow for selected user input
* Default image added as a placeholder in the URL field to ensure a URL is uploaded if user cannot provide one
* Functionality added to ensure if there is an error loading an image or if the image is not found, the default image is loaded to the site
* User feedback provided by flashed messages on completeing the form
* Backend checks prevent a user accessing this page if they are not logged in

#### Edit Sheet Page
* Neat and convenient form for users to update an existing sheet
* Input fields pre-populated with the existing sheet information
* Clearly labelled input fields
* Supporting instructive text
* Form validation in place to require input, and ensure the correct format
* Dropdown boxes allow for selected user input
* Default image added as a placeholder in the URL field to ensure a URL is uploaded if user cannot provide one
* Functionality added to ensure if there is an error loading an image or if the image is not found, the default image is loaded to the site
* User feedback provided by flashed messages on completeing the form
* Option to cancel editing a sheet, user returned to the sheets page
* Backend checks prevent a user accessing this page if they are not logged in or if they do not own this sheet

#### Delete Sheet functionality
* users have the option to delete their own sheets
* Backend checks prevent a user accessing this option if they are not logged in or if they do not own this sheet
* Defensive programming modal asks user to confirm they wish to delete the sheet
* Option to cancel and return to the view sheet page

#### Sheets Page
* All sheets laid out on summary cards in a responsive layout.
* Pagination prevents the page from being cluttered 
* Pagination lnks allow user to scroll through the pages.
* Each card links to a more detailed individual plant sheet
* Search bar provided for users to search through the sheets
* Users can search by plant name and botanical name to see if the plant they want exists in the collection
* Message displayed to the users if no results returned
* Searvh results paginated 

#### Other features
* Custom 404 and 500 error pages displayed if displayed if a page can't be found
* Button and menu links on the error pages so user can easily return to the site
* Logout button, logs user out of their account, and displays a confirmation message
* Flashed messages appear for 3 seconds and then dissapear 

### Features To Be Implemented

* Full backend image validation
* The ability to filter sheets by category
* Users able to 'favourite' other sheets and view their favourites under their user profile
* Superuser functionality rather than and admin account
* A more detailed user profile, that users can update e.g changing passwords
* Comments section so that users can comment on other sheets

## Testing
You can view my separate TESTING.md file [here](TESTING.md)

## Deployment
This project was developed using [Gitpod](https://www.gitpod.io/) and was committed and pushed to [Github](https://github.com/) using the following terminal commands within Gitpod:

- _git add -A_ 
- _git commit –m “commit message”_
- _git push_

The repository was then automatically deployed to Heroku. In order to do this the following steps were taken:

### Creating an env.py file

You will need to create an __env.py__ file in __Github__. This file will hold your application’s environment variables and should contain the following:
```
import os

os.environ.setdefault("IP", "0.0.0.0")
os.environ.setdefault("PORT", "5000")
os.environ.setdefault("SECRET_KEY", " your secret key")
os.environ.setdefault("MONGO_URI", " mongodb+srv://username@clustername.gkqqu.mongodb.net/ databasename?retryWrites=true&w=majority ")
os.environ.setdefault("MONGO_DBNAME", " your database name ") 

```
Because it contains sensitive information it is important that you __env.py__ file is listed in your __.gitignore__ file to prevent it from being pushed to Github and being available publicly


### Creating Dependancies

Heroku will need to know the dependencies that are required to run your application. These will be stored in a __requirements.txt__ file. In order to create this run the following command in the github terminal
```
pip3 freeze --local > requirements.txt

```
You will then need to create a Procfile using the following command:

```
echo web: python app.py > Procfile

```
You should now have a __requirements.txt__ file which lists your dependencies, as well as __Procfile__ which needs to contain the following line

```
web: python app.py

```

* Push these 2 files to Github

### Creating the Heroku App

* Login to your Heroku account
* From the Dashboard click on __new__ then click on __create new app__
* Name your app (this needs to be lowercase and use dashes or minuses instead of spaces
* Select the region closest to where you are based
* Click __Create app__
* Under the __Deploy__ tab select __Connet to Github__ as the __Deployment method__
* Ensure that your Github profile name is showing and add your repository name in the search field     * Click __search__ to locate your Github repository
* Once you have found your repository click __Connect__
* Before you click on __Enable Automatic Deployment__ click on the __Settings__ tab near the top of the screen
* In the __Config Vars__ section click on __Reveal Config Vars__
* You need to tell __Heroku__ which variables are required, these should match those contained in the __env.py__file, as follows:

```
Key			    Value
IP			    0.0.0.0
PORT			5000
SECRET_KEY		your secret key
MONGO_URI 		mongodb+srv://username@clustername.gkqqu.mongodb.net/databasename?retryWrites=true&w=majority	
MONGO_DBNAME	your database name
```
* Now __Enable Automatic Deployment__
* In the __Manual Deploy__ section select __Master__ from the dropdown 
* Click __Deploy Branch__
* After a few minutes you should see a message confirming __Your app was successfully deployed__
* Click __Open App__ located near the top of the page to launch your app

### Cloning this repository

In order to clone and run this project locally, you will need to follow these steps:

1. On the main repository page in __Github__, click the button to download the _Code_ (located at the top above the list of files)
2. Under the _HTTPS_ tab copy the URL for the repository
3. Open the Terminal in your preferred __IDE__.
4. Change the current working directory to the location that you would like for the new cloned directory.
5. Type _git clone_ into the terminal and then paste in the URL that you copied earlier.
6. Hit _enter_ to create your clone.
7. Remember that you will need to create an env.py file to store your variables as detailed above

Full details of these summarised steps can be found [here](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository)



## Technologies Used

* HTML 5 
* CSS3 
* Javascript 
* [JQuery](https://jquery.com/) 
* [Popper.js](https://popper.js.org/) 
* [PIP3](https://pip.pypa.io/en/stable/)
* [Flask](https://flask.palletsprojects.com/en/1.1.x/)
* [Flask-PyMongo](https://pypi.org/project/Flask-PyMongo/)
* [dnspython](https://www.dnspython.org/)
* [Flask-Paginate](https://pythonhosted.org/Flask-paginate/)
* [Jinja](https://jinja.palletsprojects.com/en/3.0.x/)
* [MongoDB](https://www.mongodb.com/)
* [Werkzeug](https://werkzeug.palletsprojects.com/en/2.0.x/)
* [RandomKeyGen](https://randomkeygen.com/)
* [Responsinator](https://www.responsinator.com/)
* [Bootstrap](https://getbootstrap.com/) 
* [Git](https://git-scm.com/) 
* [Github](https://github.com/) 
* [Gitpod](https://www.gitpod.io/) 
* [Heroku](https://www.heroku.com/)
* [Balsamiq](https://balsamiq.com/) 
* [Google Chrome DevTools](https://developer.chrome.com/docs/devtools/)
* [Google Lighthouse](https://developers.google.com/web/tools/lighthouse)
* [Google Fonts](https://fonts.google.com/) 
* [Font Awesome](https://fontawesome.com/) 
* [Photoshop](https://www.photoshop.com/en) 
* [W3C](https://validator.w3.org/) 
* [w3C](https://jigsaw.w3.org/css-validator/) 
* [JSHint](https://jshint.com/)
* [AutoPrefixer](https://autoprefixer.github.io/) 



## Credits

* This project was created from a [Code Institute](https://codeinstitute.net/) student template
* [Bootstrap](https://getbootstrap.com/) modal, buttons, alerts, navbar and the Bootstrap Grid system was used to streamline layouts and responsive design.
* Ideas and knowledge gleamed from: 
  * [W3 Schools](https://www.w3schools.com/)
  * [CSS-Tricks](https://css-tricks.com/)
  * [Bootstrap](https://getbootstrap.com/)
  * [Stack Overflow](https://stackoverflow.com/) - (specific credits have been added as comment in the code)
  * [MDN](https://developer.mozilla.org/en-US/)
  * Duckett, J. 2011. HTML and CSS: Design and Build Websites. John Wiley & Sons Inc.
  * Duckett, J. 2014. Javascript & JQuery. John Wiley & Sons Inc.

## Media and Content

* Fonts [Google Fonts](https://fonts.google.com/)
* Icons [Font Awesome](https://fontawesome.com/)
* Images [TheSpruce](www.thespruce.com)
* Images [Vecteezy](www.vecteezy.com)
* Images [Unsplash](https://unsplash.com/)
* Icons [Favicon](https://favicon.io/)
* Icons [Favicon](http://clipart-library.com/)
* Audio [Zapsplat](https://www.zapsplat.com/)
* Color choice [Colorhunt](https://colorhunt.co/)
               [Coolers] (https://www.coolers.co)

## Acknowledgements

* My mentor, Can Sucullu - for his knowledge, patience and guidance.
* Code institute tutors, for their help and guidance (at all hours of the day/night)
* Task manager project - Tim Nelson
* Fellow student projects - [Self-Isolution](https://github.com/Edb83/self-isolution)
                          - [CocktailHour](https://github.com/AmyOShea/MS3-Cocktail-Hour)
* Slack forums/webinars 


