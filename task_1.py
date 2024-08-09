# First task

from datetime import datetime

def get_days_from_today(date):
    if not isinstance(date, str):
        print('Invalid input type. Please enter the date as a string in the format "YYYY-MM-DD".')
        return
    
    try:
        input_date = datetime.strptime(date, '%Y-%m-%d').toordinal()
        now_date = datetime.today().toordinal()
        result = now_date - input_date
        return result
    except ValueError:
        print('Wrong date format. Please enter date in this format "YYYY-MM-DD".')
    
print(get_days_from_today("2021-10-09"))