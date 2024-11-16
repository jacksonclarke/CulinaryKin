# Overview

This project is the web app version of my on-going CulinaryKin project. CulinaryKin is a platform that allows users to save recipes and
create shared cookbooks with family members and friends. 

### How to start the server
To start the server, open the project directory in a terminal and run:

```python manage.py startserver```

The server will then start and notify you in the terminal that it has started. After the server has booted up, open a web-browser and enter the url:
[http://127.0.0.1:8000/](http://127.0.0.1:8000/) This will take you to the homepage of CulinaryKin. You can then login or create an account.

The purpose of CulinaryKin is to help prevent the loss of family recipes, as well as to provide a safe place to store and share recipes. 


[Demo Video Part 1](https://youtu.be/NmktbefnGeA)
[Demo Video Part 2](https://youtu.be/duER3VXVTrc)

# Web Pages

**Home Page:** The home page has the hero image, the name of the app, and links to the login and register pages. The pages use a base template and 
dynamicaly fill in page content. The navigation bar at the top dynamicaly changes if the user is logged in or not.

**Login/Signin Page:** The login page uses the base template for the navigation bar and has a form that allows users to signin to the page. The entered credentials are either authorized or not, depending if the user has an account and if the username and password match.

**Signup Page:** The signup page uses the base template for the navigation bar and has a signup form that will register the user.

**Landing Page:** The temporary landing page uses the base template and dynamically changes the navigation bar since the user is signed in.
The user can then hover over the profile image and signout which will signout the user and return them to the home page.

# Relational Database
The project uses a relational database to connect the users auth information with their profile, and their profile with their recipes and recipe books.

# Development Environment

This project was created in [Visual Studio Code](https://code.visualstudio.com/) and utilizes SQLite3 and Django.

The main programming languages used in this project are Python v3.12, HTML, CSS, and SQL.

# Useful Websites

* [Django](https://docs.djangoproject.com/en/5.1/)
* [Flowbite](https://flowbite.com/docs/getting-started/introduction/)

# Future Work

* Recipe book sharing
* Recipe viewing pages
* Mobile app integration
* Finish UI development.