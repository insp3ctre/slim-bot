# Slim Bot

### Background
Lewis & Clark College has decided that they will no longer be notifying the student body about new COVID cases. These emails are vital for understanding the current status of the campus. It is important that the students are able to have full transparency when it comes to knowing what is happening on campus. Because of this, Slim Bot was born.

### How does it work?
Slim will web scrape the [Confirmed Cases Status Report](https://college.lclark.edu/offices/health_promotion_and_wellness/covid-resources/list/) for the most recent case count for the College of Arts and Sciences. This number will then be stored in a text file in order to be accessed later, but before doing this, Slim will access the previously stored count and compare it with the new number of cases. Slim then sends an email out to a Google Group which then disperes the message to a list of recipients.

### Clone the repository
If you would like to clone the repository for yourself, you will have to create 2 files which have intentially been excluded from Git.
- connection.py: a Python file for storing confidential login info. It should contain the following three string variables:
	- sender: the email that the emails will be sent from
	- receiver: the email (or group email) that the email will be sent to
	- password: an app password created from Google (see [here](https://support.google.com/accounts/answer/185833?hl=en))
- cases.txt: a blank text file for storing the previous case count