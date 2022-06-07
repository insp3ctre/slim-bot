import requests, smtplib, ssl
from connection import sender, receiver, password
from bs4 import BeautifulSoup

def caseCount(): # get cases and return change
	cases = open("cases.txt", "r")
	URL = "https://college.lclark.edu/offices/health_promotion_and_wellness/covid-resources/list/"

	page = requests.get(URL)

	soup = BeautifulSoup(page.content, "html.parser")
	results = soup.find(id = "lw_widget_b03fe531") # id for the spot on the site with the current undergrad cases
	elements = results.find_all("div", class_="table-cell")

	for element in elements: # get all part of the table cell (only runs once but has to be like this I think)
		current_case = element.find("span", class_ = "lw_profiles_667")
		if current_case == None:
			continue
		new = current_case.text.strip()
		break

	newInt = int(new)
	previous = int(cases.read()) # case count from last time the count was queried
	if newInt > previous:
		message = f"There are a total of {newInt} cases. This is a {newInt-previous} increase from last week."
	elif previous > newInt:
		message = f"There are a total of {newInt} cases. This is a {previous-newInt} decrease from last week."
	else:
		message = f"There has been no change from last week. There are still {newInt} cases."

	cases.close()
	cases = open("cases.txt", "w")
	cases.write(new) # replace old count with new count
	cases.close()
	return message

message = caseCount()

# send email
port = 465
server = "smtp.gmail.com"
context = ssl.create_default_context()
with smtplib.SMTP_SSL(server, port, context=context) as server:
	server.login(sender, password)
	server.sendmail(sender, receiver, message)

print("Email sent!")
