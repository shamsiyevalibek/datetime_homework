#Task 4:
#Write a Python program that calculates the age of a person based on their birth year. Prompt the user to enter their birth year, and display their current age.
from datetime import datetime
birth_year = int(input("Iltimos, tug'ilgan yilingizni kiriting (yyyy formatida): "))
current_year = datetime.now().year
age = current_year - birth_year
print(f"Sizning yosingiz: {age} yosh.")
