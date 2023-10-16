from datetime import datetime, timedelta


users = [{"name": "Bill Gates", "birthday": datetime(1955, 10, 17)},
         {"name": "Dariia Babii", "birthday": datetime(2002, 10, 30)},
         {"name": "Charles Moss Duke", "birthday": datetime(1935, 10, 18)},
         {"name": "Michael Collins", "birthday": datetime(1930, 10, 30)},
         {"name": "Buzz Aldrin", "birthday": datetime(1930, 10, 20)},
         {"name": "Neil Alden Armstrong", "birthday": datetime(1930, 8, 5)},
         {"name": "Alan Bartlett Shepard", "birthday": datetime(1923, 11, 18)}]

def get_birthdays_per_week(users):
    working_days = {
        'Monday': [],
        'Tuesday': [],
        'Wednesday': [],
        'Thursday': [],
        'Friday': []
    }

    today = datetime.today().date()
    print(f"Today is {today}")
    for user in users:
        name = user["name"]
        birthday = user["birthday"].date()
        birthday_this_year = birthday.replace(year=today.year)

        if birthday_this_year < today:
            birthday_this_year = birthday.replace(year=today.year+1)

        delta_days = (birthday_this_year - today).days
        day_of_week = birthday_this_year.strftime('%A')
        
        if day_of_week in ['Saturday', 'Sunday'] and delta_days < 7:
            birthday_this_year += timedelta(days=(7 - delta_days))
            delta_days = (birthday_this_year - today).days
            day_of_week = 'Monday'

        if 0 <= delta_days < 7 and day_of_week in working_days:
            working_days[day_of_week].append(name)

    return working_days


def main():
    result = get_birthdays_per_week(users)
    for day, names in result.items():
        if names:
            print(f"{day}: {', '.join(names)}")


if __name__ == "__main__":
    main()