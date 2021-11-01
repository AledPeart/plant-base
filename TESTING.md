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
