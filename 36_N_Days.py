from datetime import datetime, timedelta

# Input: number of days before today
n = int(input("Enter number of days before today: "))

# Get today's date
today = datetime.today()

# Calculate the date before n days
date_before_n_days = today - timedelta(days=n)

# Print the result
print("Today's Date:", today.strftime("%Y-%m-%d"))
print(f"Date before {n} days:", date_before_n_days.strftime("%Y-%m-%d"))
