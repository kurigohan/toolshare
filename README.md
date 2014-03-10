toolshare
=========

Toolshare Project SE261
Required:
Django 1.5 and above
Python 2.7 and above

To Run:

1. From the terminal, change to the toolshare directory
2. Delete db.sqlite3 file if you have one (only if models were modified since last pull)
2. Start the dev server - 'python manage.py runserver'
3. Sync the database - 'python manage.py syncdb'
4. Enter the server ip in your web browser (default 127.0.0.1:8000) 

**You must register an the site to login to the toolshare site. During registration, a profile and shed is created for the user which is required for the site to run properly.  Using the super user account created during syncdb will give an error.

Current-Progress:
- User login: completed
- User registration: completed
- User profiles: completed
- Tool profiles: completed
- Tool management: R1 completed
- Shed profiles: R1 completed
- Share Zone: R1 completed 
- Shed management: in-progress
