#Task 3:
#Write a Python program that prompts the user to enter a specific date in the format "dd-mm-yyyy" and calculates the number of days between the current date and the entered date.
from datetime import datetime
user_input = input("Iltimos, sana kiriting (dd-mm-yyyy formatida): ")
user_date = datetime.strptime(user_input, "%d-%m-%Y")
current_date = datetime.now()
days_difference = (current_date - user_date).days
print(f"Kiritilgan sana bilan hozirgi sana orasidagi kunlar soni: {abs(days_difference)}")