#Task 5:
#Write a Python program that prompts the user to enter a specific date in the format "dd-mm-yyyy" and determines the day of the week on which that date falls.
from datetime import datetime
user_input = input("Iltimos, sana kiriting (dd-mm-yyyy formatida): ")
user_date = datetime.strptime(user_input, "%d-%m-%Y")
day_of_week = user_date.strftime("%A")
print(f"Kiritilgan sana {day_of_week} kuniga to'g'ri keladi.")
