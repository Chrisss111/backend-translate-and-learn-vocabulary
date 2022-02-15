Translate and Build Vocabulary

Welcome to the backend repo for this project!

## Introduction

This is a translation web app. The target audience is intermediate to advanced foreign language learners. With this app you can paste a text in a foreign language into the designated text box then indicate with an asterisk (*) which specific words in the text you want translated. Then when you press enter a vocabulary list of the words you indicated will appear, along with your original text. For each word in the vocabulary list you will have the foreign word and its English translation, a link to a more detailed translation (on Google Translate), and an input box to write any notes you may have about the word. 

After your vocabulary list has been generated you will have the option to save it (along with the original text) for future reference/study.


## Technologies

Front-end - React

Backend - Python, Flask, SQLAlchemy, PostgresSQL

External APIs - Google Translate API 

## Instructions

***In order to use this web app you will need to get your own Google API key to use the Google Translate API ***

1.) Clone both the front-end and backend repositories

2.) For the backend: 
-create and activate the virtual environment with $ python3 -m venv venv  and then  $ source venv/bin/activate
-in the virtual environment install project requirements with $ pip install -r requirements.txt
-create a local SQL database for the project, you can call this database something like translate_and_vocab_development 
-create a .env file and add this environment variable: FLASK_ENV=development
-also, add the environment variable SQLALCHEMY_DATABASE_URI to hold the path to your development database. For example you can type: SQLALCHEMY_DATABASE_URI=here put the path to the database you created on your local machine
-download the JSON file associated with your Google Translate API key and make sure to put it in the root of the project folder. Then in your .env file set the GOOGLE_APPLICATION_CREDENTIALS variable equal to the name of the JSON file
-lastly, run the backend server with $ FLASK_ENV=development flask run

3.) For the front-end:
-install axios with $ yarn add axios
-create a .env file with the variable REACT_APP_BACKEND_URL equal to your local host
-start the front-end server and open up the webpage for the app with $ npm start or $ yarn start

Once the web app opens up, and assuming the backend along with the Google API key/JSON file have been set up correctly, you should be able to follow the instructions on the homepage and start using the app!



