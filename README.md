# psych_test_demo
Demo Django web app, which provides user with a test with multiple options and then exports users answers to .xlsx file on the server. Link to the live implementation of this project: Project is based on one of my older project: <https://ptdemo.pythonanywhere.com>

# Staring the application
1. Open terminal command line prompt
2. Navigate to project directory
3. Install the requirements by calling `pip install -r requirements.txt`
4. Launch local instance by entering `python manage.py runserver`

# Urls in the application:
+ `/` Shows test questions
+ `/results` After submiting form user is sent to this page, if it accessed via GET it will be redirected to `/`
+ `/files` Views all .xlsx files that have been created, user can download any of them by clicking on the name
