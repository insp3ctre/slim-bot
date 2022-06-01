import requests
from bs4 import BeautifulSoup

URL = "https://college.lclark.edu/offices/health_promotion_and_wellness/covid-resources/list/"
page = requests.get(URL)

file = open("cases.txt", "a+")

soup = BeautifulSoup(page.content, "html.parser")
results = soup.find(id = "lw_widget_b03fe531")
elements = results.find_all("div", class_="table-cell")

for element in elements:
	current_case = element.find("span", class_ = "lw_profiles_667")
	if current_case == None:
		continue
	# print(current_case.text.strip())
	file.write(current_case.text.strip())


	break

file.close()