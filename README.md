README.md

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
* In addition the flashed messages and information/warnings will use Bootstraps warning yellow (#FFC107) ![Yellow](static/images/yellow.png)

#### Fonts

* The majority of the site uses ![Arial](https://www.fonts.com/font/monotype/arial) for its neutral ashthetic
* The Quick Fact Sheets will use ![Roboto Mono](https://fonts.google.com/specimen/Roboto+Mono)  in order to give a 'quick', 'informative' feeling to the user
* Text color will be a soft black (#313232)

#### Bootstrap

* I have the CSS framework ![Bootstrap](https://getbootstrap.com/) to achieve a design consistency across the site. Bootstraps responsive breakpoints have been utilised to ensure the site layout is responsive across all viewports and devices 
* Buttons - The sites buttons will all be Boostrap's 'Outline Secondary', again they have a neutrality that will compliment rather than distract from the sites color 
* I have used Bootstrap's modals, cards, alerts and forms and responsive navbar, throughout the site to achieve a uniformity of design that is visually pleasing and responsive.

### Initial Planning

#### Wireframes

My initial wireframes can be seen ![here](static/images/wireframes)

I have largely stuck to my initial vision for the site in terms of the layout and design. Some features were not implemented due to practical time constraints. I detail this further in the 'features left to implement' section.

#### Site Layout

My initial layout and functionality plans can be seen ![here](static/images/site maps) These were really useful in developing and building the site. Again not all features were implemented and I elaborate on this in the features section.

#### Database 

I choose to use ![MongoDB](https://www.mongodb.com/) to store and access all the data for the site.  
My database schea plans can be viewed ![here](static/images/site maps).
Initially I had planned to have two collections, one for the plant sheets and one for users, but this was expanded to three to include a categories collection in order to better group the sheets. For the purposes of this site, categories could have been part of the sheets collections, but with an eye on future facilitate scalibility it was added as a seperate collection.  MongoDB was the right choice for my purposes as there is not a lot of relational data sets, and the flexibility it offers is key.


