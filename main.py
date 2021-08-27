from datetime import datetime
import pandas
import random
import smtplib

MY_EMAIL = "thurrappattujoseph@gmail.com"
MY_PASSWORD = "thurrappattu@007"

today = datetime.now()
today_tuple = (today.month, today.day)

data = pandas.read_csv("birthdays.csv")
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}
if today_tuple in birthdays_dict:
    birthdays_person = birthdays_dict[today_tuple]
    file_path = f"letter_templates/letter_{random.randint(1, 3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents.replace("[NAME]", birthdays_person["name"])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)


# 4. Send the letter generated in step 3 to that person's email address.
# HINT 4: The message should have the Subject: Happy Birthday then after \n\n The Message Body.



