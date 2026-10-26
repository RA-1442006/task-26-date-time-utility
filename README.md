# Date and Time Utility (Task 26)

A clean, menu-driven Python console application that performs common calendar, date, and time calculations using only Python's standard `datetime` module.

---

## Objective

The goal of this project is to learn and demonstrate practical date and time manipulation in Python without relying on any external third-party libraries. It covers parsing, formatting, date arithmetic, calendar boundary management, leap year rules, and robust user input validation.

---

## Tools Used

- **Language:** Python 3 (standard library only)
- **Built-in Modules:**
  - `datetime.datetime` – Parsing, formatting, and inspecting timestamps.
  - `datetime.date` – Calendar dates and day/month/year arithmetic.
  - `datetime.timedelta` – Date differences and day-stepping loops.

---

## How to Run

1. Open a terminal or command prompt.
2. Navigate to the project directory:
   ```bash
   cd date_time_utility
   ```
3. Run the program with Python:
   ```bash
   python date_utility.py
   ```

No virtual environment or third-party packages are needed.

---

## Supported Operations

1. **Age Calculator:**
   - Prompts for a date of birth in `DD-MM-YYYY` format.
   - Computes current age precisely in **years, months, and days**, properly borrowing days from the previous month and borrowing months when needed.
   - Also displays total days lived.
   - Rejects future dates with a clear prompt to try again.

2. **Days Between Two Dates:**
   - Takes two dates in `DD-MM-YYYY` format.
   - Computes total difference in calendar days.
   - Breaks down the difference into full weeks and remaining days (e.g., 42 weeks and 4 days).
   - If the second date is earlier than the first, the program gracefully swaps them and informs the user.

3. **Working Days Calculator:**
   - Counts all Monday through Friday days between a start and end date (inclusive).
   - Automatically skips weekend days (Saturday and Sunday).
   - Provides total calendar days, working days, and weekend days.

4. **Date/Time Formatter:**
   - Retrieves the system's current date and time.
   - Displays it across several standard and friendly formats:
     - `DD-MM-YYYY`
     - `Month DD, YYYY`
     - `Day, Month DD, YYYY`
     - 12-Hour time with AM/PM
     - 24-Hour time
     - Weekday name
     - ISO 8601 format (`YYYY-MM-DD HH:MM:SS`)

5. **Leap Year Checker:**
   - Takes any 4-digit positive year and checks whether it is a leap year.
   - Explains the exact mathematical reason according to the Gregorian calendar rules:
     - Divisible by 400 $\rightarrow$ Leap year.
     - Divisible by 100 but not 400 $\rightarrow$ Not a leap year (common year).
     - Divisible by 4 and not 100 $\rightarrow$ Leap year.
     - Otherwise $\rightarrow$ Not a leap year.

6. **Exit:**
   - Terminates the interactive console loop cleanly.

---

## Sample Calculations

- **Age Calculation:**
  - Date of Birth: `15-08-2003`
  - Current Date: `26-10-2026`
  - Result: **23 years, 2 months, 11 days** (8,473 days lived).

- **Days Between Dates:**
  - Range: `01-01-2026` to `26-10-2026`
  - Result: **298 day(s)** $\rightarrow$ **42 week(s) and 4 day(s)**.

- **Working Days:**
  - Range: `01-01-2026` to `26-10-2026` (inclusive)
  - Total calendar days: 299 days.
  - Working days (Monday to Friday): **213 days**.
  - Weekend days (Saturday & Sunday): **86 days**.

- **Leap Year Checks:**
  - `2024`: **Leap year** (366 days, Feb has 29 days – divisible by 4 and not 100).
  - `2100`: **Not a leap year** (365 days, Feb has 28 days – divisible by 100 but not 400).
  - `2000`: **Leap year** (366 days – divisible by 400).

---

## Handling Leap Years and Invalid Input

- **Date Input Validation:**
  - All date entries are strictly parsed using `datetime.strptime(user_input, "%d-%m-%Y").date()`.
  - Non-existent dates (such as `31-02-2026`, `31-04-2024`, or malformed text like `abc`) raise a `ValueError` inside Python's parser.
  - The program traps this exception, prints a friendly error message, and re-prompts the user without crashing.

- **Leap Year Verification:**
  - Because `strptime` validates against calendar rules, `29-02-2000` is accepted as a valid leap day, while `29-02-2100` and `29-02-2025` are automatically recognized as invalid and rejected.

- **Chronological Ordering & Future Dates:**
  - For age calculation, dates of birth that are strictly greater than `date.today()` are rejected with an informative message.
  - For range calculations (days between, working days), if the second date is chronologically earlier than the first date, the values are automatically swapped with a notification message so the calculation remains valid and positive.

---

## Technical Questions & Answers

### 1. What is the datetime module?
The `datetime` module is a core part of Python's standard library that supplies classes for manipulating dates and times (`date`, `time`, `datetime`, `timedelta`, `timezone`). It provides built-in calendar logic (such as days per month, leap years, and weekday tracking) as well as conversion methods like `strptime` (string parsing) and `strftime` (string formatting).

### 2. How do you calculate the difference between two dates?
In Python, subtracting two `date` or `datetime` objects using the subtraction operator (`-`) returns a `timedelta` object. For example:
```python
difference = date2 - date1
total_days = difference.days
```
The `.days` attribute provides the elapsed time in whole days. You can further divide `total_days // 7` to get full weeks and `total_days % 7` for remaining days.

### 3. Why should date calculations use standard libraries?
Date calculations should use standard libraries because calendars are surprisingly complex:
- Months vary in length (28, 29, 30, or 31 days).
- Leap years follow non-trivial multi-century rules (every 4 years, skip century years unless divisible by 400).
- Daylight saving time transitions, timezones, and leap seconds can easily introduce bugs into manual arithmetic.
Standard libraries like `datetime` encapsulate these edge cases reliably, preventing silent calculation errors, off-by-one bugs, and invalid date representations.
