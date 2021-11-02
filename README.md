
Login Tracker
-------------

login_tracker is a Django reusable app to track logins.
It keeps  track of all the login history

Install
------------


    


Quick start
-----------
1. Install login tracker:: 
  
      pip install login-tracker
      or
      pip install git+https://github.com/doddahulugappa/login-tracker.git


2. Add "login_tracker" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'login_tracker',
    ]

3. Include the login_tracker URLconf in your project urls.py like this::

    path('login_tracker/', include('login_tracker.urls')),

4. Run ``python manage.py migrate`` to create the login_tracker models.

5. Login into your django admin panel and you will be able see the Login History Tracker under LOGIN_TRACKER App

