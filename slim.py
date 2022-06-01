import requests
from bs4 import BeautifulSoup

file = open("cases.txt", "a+")

URL = "https://college.lclark.edu/offices/health_promotion_and_wellness/covid-resources/list/"
page = requests.get(URL)



soup = BeautifulSoup(page.content, "html.parser")
results = soup.find(id = "lw_widget_b03fe531")
elements = results.find_all("div", class_="table-cell")

for element in elements:
	current_case = element.find("span", class_ = "lw_profiles_667")
	if current_case == None:
		continue
	# print(current_case.text.strip())
	file.write(current_case.text.strip())
	file.write("\n")
	break

lines = file.readlines()

print(lines)


if (int(lines[-2]) > int(lines[-3])):
	delta = int(lines[-2]) - int(lines[-3])
	print(f"{lines[-2]} case(s) this week.\n{delta} case increase.")
elif (lines[-2] < lines[-3]):
	delta = int(lines[-3]) - int(lines[-2])
	print(f"{lines[-2]} case(s) this week.\n{delta} case decrease.")
else:
	print("No change in cases.")


file.close()