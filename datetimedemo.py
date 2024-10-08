"""
This Python program retrieves and displays the current date and time in various formats using the `datetime` module.

Author: Sarju S
Date: 8-10-2024

The program performs the following tasks:
1. Retrieves the current date and time using `datetime.now()`.
2. Displays the current date and time in its default format.
3. Formats and displays the date and time in the following formats:
   - [YYYY-MM-DD HH:MM:SS]
   - [MM/DD/YYYY]
   - [Day, Month DD, YYYY]
   - [Day, Month DD, YYYY HH:MM:SS AM/PM]
   - [Abbr Weekday Name-Abbr Month Name-DD HH:MM:SS IST YYYY]
4. Displays the current date and time in ISO 8601 format.
5. Separately displays:
   - The date only (YYYY-MM-DD)
   - The time only (HH:MM:SS)
   - The month only (Full Month Name)
   - The year only (YYYY)

This program provides a simple example of how to format dates and times using the `strftime()` method from the `datetime` module.
"""

from datetime import datetime

# Get the current date and time
current_time = datetime.now()

# Display the current date and time
print(f"Current date and time: {current_time}")

# Display in the format [YYYY-MM-DD HH:MM:SS]
formatted_1 = current_time.strftime("%Y-%m-%d %H:%M:%S")
print(f"Format [YYYY-MM-DD HH:MM:SS]: {formatted_1}")

# Display in the format [MM/DD/YYYY]
formatted_2 = current_time.strftime("%m/%d/%Y")
print(f"Format [MM/DD/YYYY]: {formatted_2}")

# Display in the format [Day, Month DD, YYYY]
formatted_3 = current_time.strftime("%A, %B %d, %Y")
print(f"Format [Day, Month DD, YYYY]: {formatted_3}")

# Display in the format [Day, Month DD, YYYY HH:MM:SS AM/PM]
formatted_4 = current_time.strftime("%A, %B %d, %Y %I:%M:%S %p")
print(f"Format [Day, Month DD, YYYY HH:MM:SS AM/PM]: {formatted_4}")

# Format the date and time like "Thu-Jul-11 10:26:23 IST 2024"
formatted_5 = current_time.strftime("%a-%b-%d %H:%M:%S %Z %Y")
print(f"Format [Abbr Weekday Name-Abbr Month Name-DD HH:MM:SS IST YYYY]: {formatted_5}")

# Display in ISO format
formatted_6 = current_time.isoformat()
print(f"ISO format: {formatted_6}")

# Display the date only
date_only = current_time.strftime("%Y-%m-%d")
print(f"Date only: {date_only}")

# Display the time only
time_only = current_time.strftime("%H:%M:%S")
print(f"Time only: {time_only}")

# Display the month only
month_only = current_time.strftime("%B")
print(f"Month only: {month_only}")

# Display the year only
year_only = current_time.strftime("%Y")
print(f"Year only: {year_only}")