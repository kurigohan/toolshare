toolshare
=========

Team 4 Toolshare Project SE261
by: Andy Nguyen, Raymond Bremmer, Cody Tinker, Arron Reed, Ransom Quinn
Test liason: Andy - agn3691@rit.edu

Required:
Django 1.6.x
Python 2.7.x or 3.3.x

To Run:
1. From the terminal, change to the toolshare directory
2. Start the dev server - 'python manage.py runserver'
3. If the directory does not contain a db.sqlite3 file for testing, create a new one - 'python manage.py syncdb'
4. Enter the server ip in your web browser (default 127.0.0.1:8000) 

If developer:
- Delete db.sqlite3 file and resync if you updated any models since the last pull

**When creating a new database, if you create a superuser you cannot use that account to login to the main site. You must register a normal account to login to the toolshare site.


Toolshare pages:
- Dashboard options:	
	My Tools - This page displays all your tools and tools borrowed
	My Sheds - This page displays all your sheds. You will always have one shed 		designated as your 'home'. Your home shed is used to determine your share 		zone.
	Share zone - This page displays all tools within your share zone (zip code)
- Top-bar Nav:
	Bell icon - Your notifications
	Mail Icon - Your inbox/outbox for private messaging
	Exclamation Icon - Your borrow requests

How borrowing and sharing works:
	Users can only borrow tools that are in their share zone. When a user 	selects borrow, a borrow request is sent to the tool owner. The tool owner has the option to accept or deny the request. 


KNOWN ISSUES:
	- Changing the image of a shed or tool after creation does not work
	- There is no checking done on the file upload during tool/shed creation
	- Profile image upload not implemented yet
	- Sometimes dropdown selection will become unresponsive during tool/shed 		  create and edit
	- Help page is outdated
	- No restrictions on changing home shed (aka share zone)
