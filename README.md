# Microsoft-WIT-submission
## Languages Used:
1. Frontend- Html,css
2. Backend- Python
3. Database- MySql
4. Hosting- Azure Cloud Services
5. Frameworks - Django, twilio, opencv, geocoder
## Installation
To install all python dependencies:
```
 pip install -r requirements
```
Make sure you have your MySql database credentials in settings.py
To run the django server on localhost:
```
python manage.py makemigrations 
python manage.py migrate
python manage.py runserver
```
You will see the following on the command line
```
Performing system checks...

System check identified no issues (0 silenced).

February 12, 2021 - 15:50:53
Django version 3.1, using settings 'mysite.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

Visit http://127.0.0.1:8000/ with your Web browser.
The project is also hosted on Azure cloud: https://women-safety.azurewebsites.net/
The hosted project is not fully functional due to database hosting issues.
## User Guideline:
1. Please use the default as the phone number of the emergency contacts as Twilio only sends messages to verified numbers
https://www.twilio.com/docs/usage/tutorials/how-to-use-your-free-trial-account
2. The hosted version of the website https://women-safety.azurewebsites.net/  is not fully functional due to database integration issues.
