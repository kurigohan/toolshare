toolshare
=========

Team 4 Toolshare Project SE261
by: Andy Nguyen, Raymond Bremmer, Cody Tinker, Arron Reed, Ransom Quinn
Test liason: Andy - agn3691@rit.edu

Required:
	Django 1.6 +
	Python 2.7 +

Getting Started
===============

To Run:

	1. From the terminal, change to the toolshare directory
	2. If the directory does not contain a db.sqlite3 file for testing, create a new one - 'python manage.py syncdb'
	3. Start the dev server - 'python manage.py runserver'
	4. Enter the server ip in your web browser (default 127.0.0.1:8000) 

	**When creating a new database, if you create a superuser you cannot use that account to login to the main site. You must register a normal account to login to the toolshare site.

Reccomended browsers: Google Chrome or Mozilla Firefox 

App Info
========

Toolshare pages:

	Dashboard options:	
	
	1. My Tools - This page displays all your tools and tools borrowed.
	2. My Sheds - This page displays all your sheds. You will always have one shed designated as your 'home'. Your home shed is used to determine your share zone.
	3. Share zone - This page displays all tools within your share zone (zip code). You can only borrow tools from within your share zone. 

	Top-bar Nav:

	1. Bell icon - Your notifications
	2. Mail Icon - Your inbox/outbox for private messaging
	3. Exclamation Icon - Your borrow requests

How borrowing and sharing works:

	- Users can only borrow tools that are in their share zone. When a user selects borrow, a borrow request is sent to the tool owner. The tool owner has the option to accept or deny the request. 

*Refer to the help page of the web app for more info.
