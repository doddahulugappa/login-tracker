=====
login_tracker
=====

login_tracker is a Django app to conduct Web-based login_tracker.
It keeps  track of all the login history


Quick start
-----------

1. Add "login_tracker" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'login_tracker',
    ]

2. Include the login_tracker URLconf in your project urls.py like this::

    path('login_tracker/', include('login_tracker.urls')),

3. Run ``python manage.py migrate`` to create the login_tracker models.

4. Start the development server and visit http://127.0.0.1:8000/admin/
   to create a login_tracker (you'll need the Admin app enabled).

5. Visit http://127.0.0.1:8000/login_tracker/ to participate in the login_tracker.