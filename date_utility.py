from datetime import datetime, date, timedelta

# convert a DD-MM-YYYY string into a date object
def parse_date(date_str):
    return datetime.strptime(date_str, "%d-%m-%Y").date()

# prompt the user until they enter a valid date in DD-MM-YYYY format
def get_valid_date(prompt):
    while True:
        user_input = input(prompt).strip()
        try:
            return parse_date(user_input)
        except ValueError:
            print("Invalid date! Please enter a valid date in DD-MM-YYYY format (e.g. 15-08-2024).")

# calculate age in years, months, and days
def calculate_age(dob, today=None):
    if today is None:
        today = date.today()

    years = today.year - dob.year
    months = today.month - dob.month
    days = today.day - dob.day

    # if days are negative, borrow days from the previous month
    if days < 0:
        first_day_current_month = date(today.year, today.month, 1)
        last_day_prev_month = first_day_current_month - timedelta(days=1)
        days += last_day_prev_month.day
        months -= 1

    # if months are negative, borrow a year
    if months < 0:
        months += 12
        years -= 1

    return years, months, days

# calculate difference in days, weeks, and remaining days
def get_days_between(date1, date2):
    delta = date2 - date1
    total_days = abs(delta.days)
    weeks = total_days // 7
    remaining_days = total_days % 7
    return total_days, weeks, remaining_days

# count working days (Monday to Friday) between two dates
def count_working_days(start_date, end_date):
    current = start_date
    working_days = 0
    weekend_days = 0

    while current <= end_date:
        # 0 is Monday, 4 is Friday, 5 is Saturday, 6 is Sunday
        if current.weekday() < 5:
            working_days += 1
        else:
            weekend_days += 1
        current += timedelta(days=1)

    return working_days, weekend_days

# check if a year is a leap year
def is_leap_year(year):
    # leap years are divisible by 4, except century years unless divisible by 400
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    return False

# explanation helper for leap year
def get_leap_year_reason(year):
    if year % 400 == 0:
        return "Divisible by 400."
    elif year % 100 == 0:
        return "Divisible by 100, but not divisible by 400."
    elif year % 4 == 0:
        return "Divisible by 4 and not divisible by 100."
    else:
        return "Not divisible by 4."

# -------------------------------------------------------------
# Menu Handlers
# -------------------------------------------------------------

def handle_age_calculator():
    print("\n--- 1. Age Calculator ---")
    today = date.today()
    print(f"Today's Date: {today.strftime('%d-%m-%Y')}")

    while True:
        dob = get_valid_date("Enter your date of birth (DD-MM-YYYY): ")
        if dob > today:
            print("Date of birth cannot be in the future! Please try again.")
            continue
        break

    years, months, days = calculate_age(dob, today)
    total_days = (today - dob).days

    print("\n--- Result ---")
    print(f"Date of Birth: {dob.strftime('%d-%m-%Y')}")
    print(f"Current Age:   {years} years, {months} months, {days} days")
    print(f"Total Days:    {total_days:,} days lived")

def handle_days_between():
    print("\n--- 2. Days Between Two Dates ---")
    date1 = get_valid_date("Enter first date (DD-MM-YYYY): ")
    date2 = get_valid_date("Enter second date (DD-MM-YYYY): ")

    if date2 < date1:
        print("\nNote: Second date was earlier than first date. Swapping dates for calculation.")
        date1, date2 = date2, date1

    total_days, weeks, remaining_days = get_days_between(date1, date2)

    print("\n--- Result ---")
    print(f"From: {date1.strftime('%d-%m-%Y')} ({date1.strftime('%A')}) to {date2.strftime('%d-%m-%Y')} ({date2.strftime('%A')})")
    print(f"Total Difference: {total_days} day(s)")
    print(f"In Weeks & Days:  {weeks} week(s) and {remaining_days} day(s)")

def handle_working_days():
    print("\n--- 3. Working Days Calculator ---")
    date1 = get_valid_date("Enter start date (DD-MM-YYYY): ")
    date2 = get_valid_date("Enter end date (DD-MM-YYYY): ")

    if date2 < date1:
        print("\nNote: End date was earlier than start date. Swapping dates for calculation.")
        date1, date2 = date2, date1

    working_days, weekend_days = count_working_days(date1, date2)
    total_calendar_days = (date2 - date1).days + 1

    print("\n--- Result ---")
    print(f"Start Date: {date1.strftime('%d-%m-%Y')} ({date1.strftime('%A')})")
    print(f"End Date:   {date2.strftime('%d-%m-%Y')} ({date2.strftime('%A')})")
    print(f"Total calendar days (inclusive): {total_calendar_days} days")
    print(f"Working days (Mon to Fri):       {working_days} days")
    print(f"Weekend days (Sat & Sun):        {weekend_days} days")

def handle_datetime_formatter():
    print("\n--- 4. Date/Time Formatter ---")
    now = datetime.now()
    print("Current date and time in various standard formats:\n")
    print(f"  1. DD-MM-YYYY:           {now.strftime('%d-%m-%Y')}")
    print(f"  2. Month DD, YYYY:       {now.strftime('%B %d, %Y')}")
    print(f"  3. Day, Month DD, YYYY:  {now.strftime('%A, %B %d, %Y')}")
    print(f"  4. 12-Hour Time:         {now.strftime('%I:%M:%S %p')}")
    print(f"  5. 24-Hour Time:         {now.strftime('%H:%M:%S')}")
    print(f"  6. Weekday Name:         {now.strftime('%A')}")
    print(f"  7. ISO 8601 Format:      {now.strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"  8. Full Summary:         {now.strftime('%A, %d %B %Y at %I:%M:%S %p')}")

def handle_leap_year_checker():
    print("\n--- 5. Leap Year Checker ---")
    while True:
        year_str = input("Enter a year to check (e.g. 2024): ").strip()
        if not year_str.isdigit() or int(year_str) <= 0:
            print("Invalid input! Please enter a valid positive year (e.g. 2024).")
            continue
        year = int(year_str)
        break

    leap = is_leap_year(year)
    reason = get_leap_year_reason(year)

    print("\n--- Result ---")
    if leap:
        print(f"{year} IS a leap year! (366 days, February has 29 days)")
    else:
        print(f"{year} is NOT a leap year. (365 days, February has 28 days)")
    print(f"Reason: {reason}")

def show_menu():
    print("\n==========================================")
    print("         DATE AND TIME UTILITY            ")
    print("==========================================")
    print("1. Calculate Age (Years, Months, Days)")
    print("2. Days Between Two Dates")
    print("3. Working Days Calculator (Mon-Fri)")
    print("4. Date/Time Formatter (Current Time)")
    print("5. Leap Year Checker")
    print("6. Exit")
    print("==========================================")

def main():
    while True:
        show_menu()
        choice = input("Enter your choice (1-6): ").strip()

        if choice == "1":
            handle_age_calculator()
        elif choice == "2":
            handle_days_between()
        elif choice == "3":
            handle_working_days()
        elif choice == "4":
            handle_datetime_formatter()
        elif choice == "5":
            handle_leap_year_checker()
        elif choice == "6":
            print("\nThank you for using Date and Time Utility. Goodbye!\n")
            break
        else:
            print("Invalid choice! Please select an option between 1 and 6.")

if __name__ == "__main__":
    main()
