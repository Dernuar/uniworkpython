from datetime import datetime as dt
from datetime import timedelta as td

def main():
    print(
        f'Today {dt.today().date()} '
        f'Day of the week - {dt.today().isoweekday()}'
    )
    n = int(input("Enter the amount of days: "))
    today = dt.today()
    result = today + td(days=n)
    print(
        f'After {n} days it will be {result.date()}. '
        f'Day of the week - {result.isoweekday()}'
    )

if __name__ == '__main__':
    main()