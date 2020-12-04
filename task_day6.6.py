from datetime import datetime, date
# input your birth day like this 17 09 2000
date_of_birth = datetime.strptime(input("Format Input day month year : "),"%d %m %Y")
print("")
def calculate_age(born):
	today = date.today()
	return today.year - born.year 

age = calculate_age(date_of_birth)

print("Now you're ",age," years old")