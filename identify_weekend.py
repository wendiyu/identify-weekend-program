#
#Created by: Wendi Yu
#Created on: Mar 20 2018
#
#Indentify weekend
#

day = input ("What is day today?")
if day == "saturday" or day == "sunday":
	print("Please, capital the first letter.")
elif day == "Saturday" or day == "Sunday":
	print("It is weekend.") 
else:
  print("It is not weekend, it is weekday !")
