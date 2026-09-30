

day = int(input("Key in the day of the month: "))
month = int(input("Key in the month number (1 = Jan, 2 = Feb, ...): "))
year = int(input("Key in the year: "))
y_prime = year - (14 - month) // 12
leap = y_prime + y_prime // 4 - y_prime // 100 + y_prime // 400
m_prime = month + 12 * ((14 - month) // 12) - 2
d_prime = (day + leap + (31 * m_prime) // 12) % 7



days_of_week = ["Sunday", "Monday", "Tuesday", "Wednesday",
                     "Thursday", "Friday", "Saturday"]
months = ["January", "February", "March", "April", "May", "June",
              "July", "August", "September", "October", "November", "December"]

day_name = days_of_week[d_prime]
month_name = months[month - 1]
print(f"{day:02d} {month_name} {year} is a {day_name}.")