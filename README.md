# MotivateMe
#### Video Demo:  <URL>
### Description:
This is a fun web app for the **Final Project of CS50: Introduction to Computer Science**. I decided to make a web application that takes a minimalistic approach. In real life usage people would use this website to share motivational or philosophical ideas and thoughts. People would be able to connect and network in a similar way Twitter does but with the clear purpose of uplifting each other and providing moral support to others. In its initial state the website only supports a global *“feed”* page where all posts are shared, the users can read, create, and delete messages. In the future I’m planning to expand its features, allowing users to connect and follow each other, like posts, search terms, and much more!
### Concept: 
This is a page where random people motivate each other by sharing motivational thoughts, quotes, ideas & stories. The user will be able to read recent post made by people all around the world. People can choose posting anonymously or they can opt for creating an account and post under their username. The user can create and/or delete their own posts.
The website is minimalistic by design, that means features and buttons are kept to a minimum necessary and their looks integrate well with the overall design of the website.
### Design:  
The design might look simple; but is in fact the main feature of the site and probably one of the elements that required the most amount of time and effort to be achieved. While sporting a minimalistic look it also has a very responsive design. I put a lot of time making sure the website functions in a set of different screens and sizes. Some of the decorative elements of the design might disappear in relation to the size of the screen to sustain an attractive and easy to understand layout.
The buttons, for example, are one of the design features I put a lot of effort into. When the user interact with the buttons these have an animation fitting the overall feeling of the site.
This website contains four main pages: 

1.  **Landing page**

The landing page contains three buttons that allow the user to Sign-in, Sign-up or Sign as Anonymous. The sign-up button sends the user to the register page where they can proceed to create an account, the sign-in button sends the user to the login page where they can proceed to login, and the sign as Anonymous button sends the user to the feed page signed in as an Anonymous account that they can use anonymously.

2. **Registering page**

The registering page consists of three input fields: username, password, and confirmations. Some of these fields stick to certain particularities in they way they are ruled. The password input, for instance, implement regular expressions that require the user to type a password that is strong enough for their own security. It is noted under the password field that the password needs to be eight (8) characters long and must contain at least one uppercase letter and one digit. The confirmation field verifies that the password was correctly input by user. If the user fails to type any of the fields correctly, the page will alert the user and require them to re-input the information.

3. **Login page**

The login page consists of two input fields: username and password. It also has a Submit button. As the name suggest this page will simply allow the user to enter their account by typing their credentials, after which they are sent to the feed page signed as their username. If the user fails to properly fill any of the fields, they are prompted to try again with an alert message.

4. **Feed page**

This is the main page of the website. In this page the user can browse for inspirational and motivational thoughts, ideas and stories shared by other users around the world. The user can also post their own messages and can choose to delete them at any point in the future. In the page is clearly stated the username of the account being in use and it also sports a Log out button right next to the username.

### Resources and Tools: 
For the design and implementation of this website, I have used the following tools:

- HTML & CSS 

The skeleton of the website was made using HTML and CSS. There’s a decent amount of design made with CSS, a big part of the responsiveness of the site relies on the CSS stylesheet using @media conditionals. The HTML and CSS are complemented with different frameworks that I will be covering next.

- Bootstrap & Tailwind CSS frameworks

For the CSS design two frameworks are used. Personally, I like Tailwind more than Bootstrap simply because I think it has a better and more understandable [documentation](https://tailwindcss.com/docs/background-size). Despite this I decided to still use bootstrap in some parts of the website, considering I had experience using it on the ‘Homepage’ pset8 project (e.g., implementation of cards).

- SQLite3 

SQLite3 is the tool used for managing the database, it is used in accordance with the material learned during the CS50 introduction to Computer Science course.

- Python 3, Flask & Jinja2

I decided to use python because I wanted to implement a web app, and so far I have had the most exposition with it during the CS50 course. I felt I wanted to continue to build and experiment using these tools. Going forward I’m interested in using more tools such as more JavaScript and its corresponding frameworks.

### Files:

This project contains three (3) folders and four (4) files. Each folder has a number of files of their own. In this section I will cover each and one of them and their purpose. I will go over them in order from top to bottom in alphabetic order, starting with the folders and their respective files and moving to the general files.

- [Folder] flask_session

  Flask-Session is an extension for Flask that supports Server-side Session to the application. The Session is the time between the client logs in to the server and logs out of the server. The data that is required to be saved in the Session is stored in a temporary directory on the server.

  *This folder was borrowed from the CS50 finance pset and is not of my own.*

- [Folder] static

  - [File] favicon-16x16.png
  
    This is an image of an emoji and it is used as the site favicon on the browser’s tab.

  - [File] feedstyle.css

    This is the CSS file corresponding to the feed page. CSS files has been separate it for clarity and better organize the files.

  - [File] indexstyle.css

    This is the CSS file corresponding to the Landing page.

  - [File] registerstyle.css

    This CSS file correspond to the Login and Register pages.

- [Folder] templates

  - [File] feed.html

    This HTML file contains the inner block for the feed page. That is the main part of the website since is the element that renders the posts of users.

  - [File] index.html

    Index refers to the Landing page. It is by default the page the users first see and interact with. In this file is the skeleton for the main three buttons

  - [File] layout-feed.html

    This is the layout of the feed page. Technically the feed page could have been designed in one HTML file, but I decided to separate it in two parts for future-proofing; as I add more features it will be particularly handy to have the layout and the main block separated.

  - [File] layout-index.html

    This is the layout for the Landing, Login and Register pages.

  - [File] login.html

    This HTML file contains the main block for the Login page. It basically has input fields that allow users to Login.

  - [File] register.html

    Like login.html, this file contains input fields and extra directions for the user to register for the site. It also has a submit button.

- [File] app.py

  This is the main python file. It controls all the features of the site and support the management of the database as well as the rederization of the pages. This is the heart of the project. The design of this file was deeply influenced by the Finance pset exercise, and *some of its line of code were borrowed from that problem*. However, most of the code was created anew the for the purpose of this project.

- [File] helpers.py

  This file contains the conditions for the @login_required decoration. *It is a borrowed element from Finance pset* that has been repurpose for this project. While I have modified some of the code **the vast majority of the code in this file was done by CS50 staff and is not of my own**.

- [File] README.md

  You are reading me right now. Cheers!

- [File] users.db

  This file contains a database for the website. The database has two tables: accounts and posts. Accounts keep track of all the usernames and corresponding hash numbers. The posts table keep track of all the messages done by the users as well as the date and time.

Thank you for reading. For any questions or comments feel free to contact me at *teacherrickyricardo@gmail.com*.