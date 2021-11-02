# Plant Base - Testing 

[View deployed site here](https://plant-base-project.herokuapp.com/)
[README.md]( https://github.com/AledPeart/plant-base/blob/main/README.md)

I have tested my deployed site to ensure that it achieves the intended aims of the owner and the expectations of the users by meeting the user stories detailed in the [README.md]( https://github.com/AledPeart/plant-base/blob/main/README.md). I have also manually tested the deployed site across a number of different devices and browsers to ensure that the design, layout and functionality respond as intended. In addition the validity of my HTML, CSS, Javascript and Python code have been checked using the [W3C Markup](https://validator.w3.org/) , [CSS Validation Service](https://jigsaw.w3.org/css-validator/), [JSONLint](https://jsonlint.com/) and [pep8]( https://pypi.org/project/pep8/) . Finally I have used [Lighthouse](https://developers.google.com/web/tools/lighthouse) in Chrome DevTools to test the accessibility and performance of my site. The specific tests and results are detailed below:

## __Table of Contents__
1. [User Stories](#user-stories)
2. [Owner Stories](#owner-stories)
3. [Manual Functionality Testing](#manual-functionality-testing)
4. [Responsiveness](#responsiveness)
5. [Cross Browser Testing](#cross-browser-testing)
6. [Code Validation](#code-validation)
7. [Lighthouse Testing](#lighthouse-testing)
8. [Testing Results and Bugs](#testing-results-and-bugs)
   - [Resolved Bugs](#resolved-bugs)
   - [Unresolved Bugs](#unresolved-bugs)



## User Stories

### As a new user I want:

### **To quickly understand the purpose of the site and the benefits it can offer me**

![supporting screenshot](https://github.com/AledPeart/plant-base/blob/main/static/images/user-story-screenshot-1.png) 
	
 
-	Clear, uncluttered homepage
-	Introductory paragraph, which informs the users about the site, how it works and what it has to offer
-	Clear navigation links and buttons to guide users towards the next appropriate action
-	Buttons and links change dependent on whether a user is logged in or not


### **To be shown relevant content that is visually pleasing**

![supporting screenshot](https://github.com/AledPeart/plant-base/blob/main/static/images/user-story-screenshot-2.png) 
 
 
-	Clear presentation of the care sheets, laid out in a uniform manner that makes it easy browse.
-	Individual plant sheets show well-presented and clear information on how to care for a plant


### **To be able to browse through the sites content without needing to create an account**

![supporting screenshot](https://github.com/AledPeart/plant-base/blob/main/static/images/user-story-screenshot-4.png)


-	Access to browse the sheets does not require users to have an account
-	Pagination prevents the page from becoming too cluttered and makes navigation easier
-	Access to view individual plant sheets does not require users to have an account


### **To be able to view individual plant sheets**

![supporting screenshot](https://github.com/AledPeart/plant-base/blob/main/static/images/user-story-screenshot-5.png)


### **To be able to search for specific plants**

![supporting screenshot](https://github.com/AledPeart/plant-base/blob/main/static/images/user-story-screenshot-6.png)


-	Search bar on the sheets page allows users to search for plants, by name, botanical name and by category


### **To be signposted to any associated social media accounts**

![supporting screenshot](https://github.com/AledPeart/plant-base/blob/main/static/images/user-story-screenshot-7.png)


-	Social media icons are clearly displayed in the page footer


### **To be able to register as a new user quickly and easily**

![supporting screenshot](https://github.com/AledPeart/plant-base/blob/main/static/images/user-story-screenshot-8.png)

 - 	A clear simple registration form, which is signposted from the home page and from the navigation menu if a user, is not logged in
 - 	Supporting instruction text provided to help users, and ensure the form is completed correctly
 - 	Inputs are required on all fields and in a specified format so that users are able to enter the information in the correct way


### As a registered user I also want:

### **To be able to login in to my account quickly and easily**

![supporting screenshot](https://github.com/AledPeart/plant-base/blob/main/static/images/registered-user-story-screenshot-1.png)

 - 	A clear simple login form, which is signposted from the home page and from the navigation menu if a user, is not logged in


### **To be able to upload my own care sheets for others to use, and for this process to be straightforward and quick**

![supporting screenshot](https://github.com/AledPeart/plant-base/blob/main/static/images/registered-user-story-screenshot-2.png)

- 	Users can upload a new care sheet via the form provided.
- 	Form is straightforward and user friendly
- 	Clear instructions provided to the user for each input field
- 	Set options provided to the user for certain fields 
- 	Confirmation message given to the user to let them know the form was submitted successfully


### **To be able to edit my own care sheets quickly and easily**


![supporting screenshot](https://github.com/AledPeart/plant-base/blob/main/static/images/registered-user-story-screenshot-3.png)


- 	Edit form is straightforward and user friendly
- 	Form is signposted from the individuals care sheet and from the navigation menus
- 	Input fields are pre-populated with the existing information to help the user and provide a batter user experience
- 	Confirmation message given to the user to let them know the form was submitted successfully

### **To be given guidance on how and what to input on when creating a sheet**

![supporting screenshot](https://github.com/AledPeart/plant-base/blob/main/static/images/registered-user-story-screenshot-4.png)

- 	Clear instructions provided to the user for each input field
- 	Set options provided to the user for certain fields 
- 	Confirmation message given to the user to let them know the form was submitted successfully


### **To be able to delete my own care sheets**

![supporting screenshot](https://github.com/AledPeart/plant-base/blob/main/static/images/registered-user-story-screenshot-5.png)


- 	Users are able to delete their own sheets
- 	Defensive programming ensures are asked to confirm that they definitely want to delete the sheet
- 	Confirmation message given to the user to let them know the form was deleted successfully
- 	User returned automatically to the sheets page

### **To be able to quickly access all of my own care sheets** 

![supporting screenshot](https://github.com/AledPeart/plant-base/blob/main/static/images/registered-user-story-screenshot-6.png)

- 	All a users sheets are displayed on their own individual profile page
- 	Here a user can	view, edit and delete their own sheets
	
### **To be able to navigate around the site quickly and cohesively**

![supporting screenshot](https://github.com/AledPeart/plant-base/blob/main/static/images/registered-user-story-screenshot-7.png)

- 	Navigation bar situated at both the top and the bottom of each page
- 	Navigation buttons provided at key locations to aid user navigation

### **I would like to the site to use icons that help me to quickly understand the information being presented to me**

![supporting screenshot](https://github.com/AledPeart/plant-base/blob/main/static/images/registered-user-story-screenshot-8.png)

- 	Icons used across key areas of the site to reinforce meaning and user understanding
- 	High contrast colors used to increase accessibility.

### As the site owner I want

### **To be able to edit and delete any content from the site**

```
elif session["user"] != owner and session["user"] != "admin":
        flash("You do not have permission to edit this sheet")
```
- Admin/superuser profile provides ability to edit or delete any sheets.

### **To be able to control the flow of information uploaded to the care sheets in order to retain a consistent presentation across the site**

-	Clear instructions provided to the user for each input field
-	Set options provided to the user for certain fields 
-	Inputs are required on all fields and in a specified format so that users are able to enter the information in the correct way

### **That the user be presented with clear instructions to guide them when creating a sheet**

-	Supporting instruction text provided to help users, and ensure the form is completed correctly
-	Clearly labeled input fields to avoid confusion


### **That input validations are used to control the validity of the data uploaded by the user**
```
if request.method == "POST":
            user_input_image = request.form.get("image")
            accepted_image_formats = ("image/png", "image/jpeg", "image/jpg")
            r = requests.head(user_input_image)
            if r.headers["content-type"] in accepted_image_formats:
                final_image = user_input_image
            else:
                final_image = "static/images/placeholder-image-potted.jpg"


```

-	Validation checks ensure images are in the correct format

![supporting screenshot](https://github.com/AledPeart/plant-base/blob/main/static/images/owner-user-story-screenshot-1.png)

-	User input validation in place to ensure the information is in the correct format


### **Preventative “server-side” checks to ensure that only registered users can upload to the site**
```
# check if the user is logged in
    if "user" not in session:
        flash("Please Login in order to continue")
        return redirect(url_for("login"))

```

### **Frontend code added to ensure default image to be loaded if a user does not upload one or if there is an error with the upload**
```
onerror="this.onerror=null; this.src='static/images/placeholder-image-potted.jpg'" 
```
-	Additional backend checks also added
```
if request.method == "POST":
            user_input_image = request.form.get("image")
            accepted_image_formats = ("image/png", "image/jpeg", "image/jpg")
            r = requests.head(user_input_image)
            if r.headers["content-type"] in accepted_image_formats:
                final_image = user_input_image
            else:
                final_image = "static/images/placeholder-image-potted.jpg"
```

### **That if the requested page does not exist a custom page is loaded that directs the user back to the site**

- 	Custom 404 and 500 error pages added to the site, with a return to site button and the site’s navigation links

![supporting screenshot](https://github.com/AledPeart/plant-base/blob/main/static/images/owner-user-story-screenshot-2.png)



## Manual Functionality Testing


### Header and Footer (base.html)

#### Do the page header and footer appear and perform as expected?

* __Test__– Does the page logo, navigation items and user icon appear as expected when the user is not logged in?   
__Result__– The result was as expected.

* __Test__– Does the page logo, navigation items and user icon appear as expected when the user is logged in?      
__Result__– The result was as expected.

* __Test__– Do the navigation items and social media icons appear as expected when the user is not logged in??   
__Result__– The result was as expected.

* __Test__– Do the navigation items and social media icons appear as expected when the user is logged in?   
__Result__– The result was as expected.

* __Test__– Do all the anchor links in the page header direct the user to the correct place?   
__Result__– The result was as expected.

* __Test__– Do all the anchor links in the page footer direct the user to the correct place?   
__Result__– The result was as expected.

* __Test__– If a user is logged in does the user icon link to the users profile page?   
__Result__– The result was as expected.

* __Test__– If a user is not logged in does the user icon link to the login page?   
__Result__– The result was as expected.


### Home Page (index.html)

#### Does the home page appear and perform as expected?

* __Test__ – Do the buttons in the text box; appear as expected when the user is not logged in?   
__Result__– The result was as expected.

* __Test__– Do the buttons in the text box; appear as expected when the user is logged in?   
__Result__– The result was as expected.

* __Test__– Do the buttons in the text box; direct the user to the correct place?   
__Result__– The result was as expected.


### Register Page 

#### Does the register page appear and perform as expected?	

* __Test__– Do the text and layout of the registration form appear as expected?   
__Result__– The result was as expected.

* __Test__– Do the appropriate icons sit before the input field name and do both sit and above the input field?   
__Result__– The result was as expected.

* __Test__– Does the instruction text sit below each input field as appropriate?   
__Result__– The result was as expected.

* __Test__– Does the expected validation check prevent users from entering a username that does not meet the required format?   
__Result__– The result was as expected.

* __Test__– Does the expected validation check prevent users from entering an email address that does not meet the required format?   
__Result__– The result was __not__ as expected.

* __Test__– Does the expected validation check prevent users from entering a password that does not meet the required format?   
__Result__– The result was as expected.

* __Test__– Does the expected validation check ensure that the users confirmation password matches the original before they can be allowed to register?   
__Result__– The result was as expected.

* __Test__– Does the show password checkbox work as expected?   
__Result__– The result was as expected.

* __Test__– Does the login link at the bottom of the registration form link to the login page?   
__Result__– The result was as expected.

* __Test__– On successfully registering is the user given a confirmation message and directed to their profile page?   
__Result__– The result was as expected.


### Login Page 

#### Does the login page appear and perform as expected?

* __Test__– Do the text and layout of the login form appear as expected?   
__Result__– The result was as expected.

* __Test__– Do the appropriate icons sit before the input field name and do both sit and above the input field?   
__Result__– The result was as expected.

* __Test__– Does the instruction text sit below each input field as appropriate?   
__Result__– The result was as expected

* __Test__– If an incorrect username is entered does the user receive the correct flash message, and returned to the same page to try again?   
__Result__– The result was as expected.

* __Test__– If an incorrect password is entered does the user receive the correct flash message, and returned to the same page to try again?      
__Result__– The result was as expected.

* __Test__– Does the show password checkbox work as expected?   
__Result__– The result was as expected.

* __Test__– Does the registration link at the bottom of the login form link to the registration page?   
__Result__– The result was as expected.

* __Test__– If the password and username are correct is the user given a welcome message and redirected to their profile page?   
__Result__– The result was as expected.


### Profile Page 

#### Does the profile page appear and perform as expected?

* __Test__– Does the h1 text and the user icon appear as expected?   
__Result__– The result was as expected.

* __Test__– Does the correct username for the user in session appear in the title and in the welcome paragraph?   
__Result__– The result was as expected.

* __Test__– Does the ‘create new sheet’ button appear below the welcome paragraph and does it link to correct page?   
__Result__– The result was as expected.

* __Test__– Are the users care sheets displayed in a stacked block of 6 per page?   
__Result__– The result was as expected.

* __Test__– Do the correct plant images appear as expected in each sheet?   
__Result__– The result was as expected.

* __Test__– Does each sheet contain the correct name, botanical name and category displayed as intended?   
__Result__– The result was as expected.

* __Test__– Do only sheets created by the user in session appear?   
__Result__– The result was as expected.

* __Test__– Are the displayed sheets paginated as expected?   
__Result__– The result was as expected.

* __Test__– Do the page pagination links work correctly?   
__Result__– The result was as expected.

* __Test__– Does the ‘see more’ button open up the appropriate individual sheet as a new page?   
__Result__– The result was as expected.


### Sheets Page 

#### Does the sheets page appear and perform as expected?

* __Test__ – Does the search bar appear at the top of the page, with the search and refresh button icons as intended?   
__Result__– The result was as expected.

* __Test__– Are users able to search for plant name, botanical name and plant category as intended?   
__Result__– The result was as expected.

* __Test__– Are the search results paginated as expected?   
__Result__– The result was as expected.

* __Test__– Do the search result pagination links work as expected?   
__Result__– The result was __not__ as expected.

* __Test__– Are the users care sheets displayed 6 per page?   
__Result__– The result was as expected.

* __Test__– Do the correct plant images appear as expected in each sheet?   
__Result__– The result was as expected.

* __Test__– Does each sheet contain the correct name, botanical name and category displayed as intended?   
__Result__– The result was as expected.

* __Test__– Do sheets created by all users appear?   
__Result__– The result was as expected.

* __Test__– Are the displayed sheets paginated as expected?   
__Result__– The result was as expected.

* __Test__– Do the page pagination links work correctly?   
__Result__– The result was as expected.

* __Test__– Does the ‘see more’ button open up the appropriate individual sheet as a new page?   
__Result__– The result was as expected.

* __Test__–  Can the sheets page be viewed by users when they are logged in, and when logged out?   
__Result__– The result was as expected.


### View Sheet Page 

#### Does the view sheet page appear and perform as expected?

* __Test__ Is the page layout as expected with all the fields from the database populating the correct parts of the page as intended?   
__Result__– The result was as expected.

* __Test__– Do the icons in the quick facts section appear as intended and correspond to the correct user input?   
__Result__– The result was as expected.

* __Test__ Does the general info text appear underneath the image and does owners name appear at the bottom of the sheet–?   
__Result__– The result was as expected.

* __Test__– If the user is not logged in do they only see the button to return to the sheets page, and does that button correctly link to that page?   
__Result__– The result was as expected.

* __Test__– When the user is in session and is the sheet owner do they see the edit and delete buttons?   
__Result__– The result was as expected.

* __Test__– When the user is in session do they see the return to sheets, and return to profile buttons, and do the buttons link to the correct pages?
   
* __Test__– Does the Edit button link to the edit sheet form as expected?   
__Result__– The result was as expected.

* __Test__– Does the delete button launch the delete modal?   
__Result__– The result was as expected.


### Add Sheet Page 

#### Does the Add sheet page appear and perform as expected?

* __Test__– Do the text and layout of the add sheet form appear as expected?   
__Result__– The result was as expected.

* __Test__– Do all the input field names sit above the input fields and correspond to the correct text information underneath the input field?   
__Result__– The result was as expected.

* __Test__– Do all the input field names with a dropdown menu contain the correct options? 
__Result__– The result was as expected.

* __Test__– Does the submit button sit correctly centered at the foot of the form?   
__Result__– The result was as expected.

* __Test__– Do all the user input validation checks work correctly and the appropriate corresponding messages appear if any entry is blank?   
__Result__– The result was as expected.

* __Test__–If a user does not enter valid URL are they prompted to do so and will the form not submit until one is entered?   
__Result__– The result was as expected.

* __Test__– The default image URL is loaded, as placeholder text should the user not have a URL they wish to upload?   
__Result__– The result was as expected.

* __Test__– If the user does enter a blank URL, they are allowed to do so and in this case a default image is loaded when the site is rendered.   
__Result__– The result was as expected.
 
* __Test__– If the user enters a valid image URL, the images is stored correctly and rendered to the appropriate pages.   
__Result__– The result was as expected.

* __Test__– If the user enters an invalid image URL, the images is replaced by a default image when loaded to the appropriate page.
__Result__– The result was as expected.

* __Test__– On submitting the form, does the user receive a message that their new sheet has been created, and they are returned to the sheets page?   
__Result__– The result was as expected.

* __Test__– Does the cancel button appear correctly and return the user to the sheets page?   
__Result__– The result was as expected.


### Edit Sheets Page 

#### Does the edit sheets page appear and perform as expected?

* __Test__– Do the text and layout of the add sheet form appear as expected?   
__Result__– The result was as expected.

* __Test__– Do all the input field names sit above the input fields and correspond to the correct text information underneath the input field?   
__Result__– The result was as expected.

* __Test__– Do all the input field names pre populate with the correct inputs from the original sheet? 
__Result__– The result was as expected.

* __Test__– Do all the input field names with a dropdown menu contain the correct options? 
__Result__– The result was as expected.

* __Test__– Is the user able to amend the input fields as intended? 
__Result__– The result was as expected.

* __Test__– Does the submit changes button sit correctly centered at the foot of the form?   
__Result__– The result was as expected.

* __Test__– Do all the user input validation checks work correctly and the appropriate corresponding messages appear if any entry is blank?   
__Result__– The result was as expected.

* __Test__–If a user does not enter valid URL are they prompted to do so and will the form not submit until one is entered?   
__Result__– The result was as expected.

* __Test__– The default image URL is loaded, as placeholder text should the user not have a URL they wish to upload?   
__Result__– The result was as expected.

* __Test__– If the user does enter a blank URL, they are allowed to do so and in this case a default image is loaded when the site is rendered.   
__Result__– The result was as expected.
 
* __Test__– If the user enters a valid image URL, the images is stored correctly and rendered to the appropriate pages.   
__Result__– The result was as expected.

* __Test__– If the user enters an invalid image URL, the images is replaced by a default image when loaded to the appropriate page.
__Result__– The result was as expected.

* __Test__– On submitting the form the user receives a message that their new sheet has been updated, and they are returned to the sheets page?   
__Result__– The result was as expected.

* __Test__– Does the cancel button appear correctly and return the user to the sheets page?   
__Result__– The result was as expected.


### Delete Sheet Modal and Functionality

#### Does the delete sheet modal warning appear and perform as expected?

* __Test__– Do the text and layout of the delete modal appear as expected?   
__Result__– The result was as expected.

* __Test__– Does the plant name appear correctly in the warning message?   
__Result__– The result was as expected.

* __Test__– Does the close button and the cancel icon (x) close the modal and return the user to the view sheet page without deleting the sheet?   
__Result__– The result was as expected.

* __Test__– Does the modal delete button delete the sheet and show the user a message that the sheet has been deleted?   
__Result__– The result was as expected.

* __Test__– After the sheet has been deleted is the user returned to the sheets page?   
__Result__– The result was as expected.


### 404 Page

#### Does the 404 page load and perform as expected?

* __Test__– Does the 404 page appear when user is directed to a non existent page, and is the layout as expected?      
__Result__– The result was as expected.

* __Test__ – Does the link provided send the user back to the start screen?       
__Result__– The result was as expected.


### Additional Functionality

#### Are users able to force their way on to pages they should not be able to access?

* __Test__– If the user is not logged in and they try and force their way onto the edit sheet page are they met with a message that they need to login and returned to the login page?   
__Result__– The result was __not__ as expected.

* __Test__– If the user is not logged in and they try and force their way onto the add sheet page are they met with a message that they need to login and returned to the login page?   
__Result__– The result was as expected.

* __Test__– If the user is not logged in and they try and force their way onto the delete sheet pages are they met with a message that they need to login and returned to the login page?   
__Result__– The result was as expected.

* __Test__– If the user is logged in and they try and force their way onto the delete sheet page for another users sheet, are they met with a message that they do not have permission to delete and returned to the sheets page?   
__Result__– The result was as expected.

* __Test__– If the user is logged in and they try and force their way onto the edit sheet page for another users sheet, are they met with a message that they do not have permission to edit that sheet and are then returned to the sheets page?   
__Result__– The result was as expected.

#### Flash messages - flashed messages have been tested as part of the functionality testing above, the following test is for their appearance 

* __Test__– Do the flashed messages appear at the top of the screen in dark text within a yellow strap as expected?   
__Result__– The result was as expected.

* __Test__– Do the flashed messages close by themselves after the set time of 3 seconds?   
__Result__– The result was as expected.

