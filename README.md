toolshare
=========

Team 4 Toolshare Project SE261
by: Andy Nguyen, Raymond Bremmer, Cody Tinker, Arron Reed, Ransom Quinn
Test liason: Andy - agn3691@rit.edu

Required:
	Django 1.6.x
	Python 2.7.x and above

--------GETTING STARTED--------

To Run:

	1. From the terminal, change to the toolshare directory
	2. If the directory does not contain a db.sqlite3 file for testing, create a new one - 'python manage.py syncdb'
	3. Start the dev server - 'python manage.py runserver'
	4. Enter the server ip in your web browser (default 127.0.0.1:8000) 

	**When creating a new database, if you create a superuser you cannot use that account to login to the main site. You must register a normal account to login to the toolshare site.

---------APP INFO----------

Toolshare pages:
	- Dashboard options:	
		1. My Tools - This page displays all your tools and tools borrowed
		2. My Sheds - This page displays all your sheds. You will always have one shed designated as your 'home'. Your home shed is used to determine your share zone
		3. Share zone - This page displays all tools within your share zone (zip code)

	- Top-bar Nav:
		1. Bell icon - Your notifications
		2. Mail Icon - Your inbox/outbox for private messaging
		3. Exclamation Icon - Your borrow requests

How borrowing and sharing works:
	- Users can only borrow tools that are in their share zone. When a user 	selects borrow, a borrow request is sent to the tool owner. The tool owner has the option to accept or deny the request. 


KNOWN ISSUES:

	- There is no checking done on the file upload during tool/shed creation
	- Sometimes dropdown selection will become unresponsive during tool/shed create and edit
	- Help page is outdated
	- No restrictions on changing home shed (aka share zone)
	- Superuser panel is outdated and missing many components
