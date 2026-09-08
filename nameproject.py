
#!/usr/bin/env python3
# ───────────────────────────────────────────────────────────────
# MIT License
# 
# Copyright (c) 2025 Venkat Praveen Ambati
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
# ───────────────────────────────────────────────────────────────

# ───────────────────────────────────────────────────────────────
# This Python program:
# - Prints the current date/time in two formats
# - Asks for your name (shows original + reversed)
# - Greets you based on time of day
# - Safely asks for your age (with validation)
# - Calculates your age in 5 years and your birth year
# - Asks for your birthday (month as number or name) and shows days until next birthday
# - Shows your age in months and (approx) days
# - Ends with a random motivational quote
# ───────────────────────────────────────────────────────────────

from datetime import datetime
from datetime import date 
import random
# Import the built-in 'random' module, which contains functions
# for generating random numbers and making random selections.
# Define a list of motivational quotes (a list is a collection of items in Python)
# ── Motivational quotes ────────────────────────────────────────
quotes = [
    "Believe in yourself!",
    "Every day is a second chance.",
    "Keep going, you're doing great!",
    "Dream big and dare to fail."
]

# ── Current date/time ──────────────────────────────────────────
now = datetime.now()

# Format 1 → Numeric (e.g., 2025-08-11 09:47:35)
# %Y → 4-digit year | %m → 2-digit month | %d → 2-digit day
# %H → hour (00–23) | %M → minute        | %S → second
formatted_time_numeric = now.strftime("%Y-%m-%d %H:%M:%S")

# Format 2 → Readable (e.g., Monday, August 11, 2025 at 09:47 AM)
# %A → weekday | %B → month name | %I → 12-hour | %p → AM/PM
formatted_time_readable = now.strftime("%A, %B %d, %Y at %I:%M %p")

print("Welcome to Python program!")
print("Today's Date and Time")
print(f"  Numeric format : {formatted_time_numeric}")
print(f"  Readable format: {formatted_time_readable}")

# ── Name input and reversing ───────────────────────────────────
name = input("\nWhat is your name? ")

print(f"\nOriginal name : {name}")
# name[::-1] → slice with step -1 → reverses the string


# name[::-1] → This is Python slicing with a negative step (-1), which reverses the string.
# Slicing syntax: sequence[start:end:step]
# - start (blank here) → default is start of the sequence (or end if step is negative)
# - end (blank here) → default is end of the sequence (or start if step is negative)
# - step = -1 → moves through the sequence backwards, one character at a time
#
# Example:
#   name = "Venkat"
#   name[::-1] → "takneV"
#   1. Start from the last character ('t')
#   2. Step backwards (-1) until the start of the string
#   3. Return the reversed string
print(f"Reversed name : {name[::-1]}")

# ── Time-of-day greeting ───────────────────────────────────────
hour = now.hour
if hour < 12:
    greeting = "Good Morning"
elif hour < 18:
    greeting = "Good Afternoon"
else:
    greeting = "Good Evening"

print(f"{greeting}, {name.upper()}!")

# ── Age input with validation ──────────────────────────────────
# Note: input() always returns a string.
# We used int(input()) above to convert it into a number immediately.
while True:
    try:
        age = int(input("\nHow old are you? "))
        if age < 0 or age > 130:
            print("❌ Please enter a realistic age (0–130).")
            continue
        break
    except ValueError:
        print("❌ Please enter a valid number for age.")

# Age in 5 years and birth year
future_age = age + 5
birth_year = now.year - age
print(f"\nYou were born in {birth_year}.")
print(f"Hello {name}, you will be {future_age} years old in 5 years!")

# ── Helpers for birthday input ─────────────────────────────────
def read_int(prompt, lo, hi):
    """Read an integer within [lo, hi] with validation."""
    while True:
        try:
            value = int(input(prompt))
            if value < lo or value > hi:
                print(f"❌ Please enter a number between {lo} and {hi}.")
                continue
            return value
        except ValueError:
            print("❌ Please enter a valid number.")

def read_month():
    """
    Read month as number (1–12) or name ('Jan', 'January').
    Returns the month number (1–12).
    """
    month_names = {
        "jan": 1, "january": 1,
        "feb": 2, "february": 2,
        "mar": 3, "march": 3,
        "apr": 4, "april": 4,
        "may": 5,
        "jun": 6, "june": 6,
        "jul": 7, "july": 7,
        "aug": 8, "august": 8,
        "sep": 9, "sept": 9, "september": 9,
        "oct": 10, "october": 10,
        "nov": 11, "november": 11,
        "dec": 12, "december": 12
    }
    while True:
        month_input = input("Enter your birth month (1–12 or name): ").strip().lower().rstrip(".")
        # Numeric input
        if month_input.isdigit():
            month_num = int(month_input)
            if 1 <= month_num <= 12:
                return month_num
            print("❌ Month number must be between 1 and 12.")
            continue
        # Text input (short or full)
        if month_input in month_names:
            return month_names[month_input]
        print("❌ Please enter a valid month number or name (e.g., 3, Mar, March).")

# ── Ask for birthday and compute days until next one ───────────
print("\nLet's figure out your next birthday!")
birth_month = read_month()
birth_day = read_int("Enter your birth day (1–31): ", 1, 31)

# Try to build this year's birthday; if invalid date (e.g., Feb 30), re-ask both fields
while True:
    try:
        this_year_birthday = datetime(now.year, birth_month, birth_day)
        break
    except ValueError:
        print("❌ That date doesn't exist. Please re-enter month and day.")
        birth_month = read_month()
        birth_day = read_int("Enter your birth day (1–31): ", 1, 31)

# If birthday already passed this year, use next year
if this_year_birthday < now:
    next_birthday = datetime(now.year + 1, birth_month, birth_day)
else:
    next_birthday = this_year_birthday

days_left = (next_birthday - now).days
if days_left == 0:
    print("🎉 Happy Birthday! It's today!")
elif days_left == 1:
    print("🎂 Your next birthday is in 1 day!")
else:
    print(f"🎂 Your next birthday is in {days_left} days!")

# Build date of birth using the year you calculated
dob = date(birth_year, birth_month, birth_day)

# Print in a nice format (e.g., Monday, August 11, 2000)
print("Your date of birth is:", dob.strftime("%A, %B %d, %Y"))
# ── Age in months and (approx) days ────────────────────────────
age_in_months = age * 12
age_in_days = age * 365  # Approximation (ignores leap years)
print(f"\nApproximate age conversions:")
print(f"  Months: {age_in_months}")
print(f"  Days  : {age_in_days} (approximate)")

# ── Motivational quote to end ──────────────────────────────────
print("\n💡 Motivational Quote for You:")
print(random.choice(quotes))

# random.choice(list_name) → Selects ONE random element from the given list
# Here, it will randomly pick one of the quotes from the 'quotes' list