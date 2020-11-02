INTRODUCTION
------------
This is a simple Web Application that queries Github for the most starred repositories and displays the output. 
It has two main files:
 1) apicall.py:  Module to make an  API request to Github and save the output. 
 2) UI.pyA: web-server that displays the retrieved information in browser. 
 
 The first module uses python requests library to make the API call and save the output as a flat file. 
 The second module is flask web-server that uses pandas library to load the saved data from the first module 
 and display it using html and javaSCript.
 
 A CRON job is created to periodically run the API request module that takes the backup of the current output file and then updates it. 
 
 
REQUIREMENTS
------------
This application requires the following modules:
Python 3.6 or above and following packages


Installations
------------
pip install pandas 
pip install requests
pip install Flask

MAINTAINER
-----------
Rajesh Shrestha




 
 
 
 
  
 

