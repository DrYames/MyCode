#Arrival Time Estimator by James Porter for CIS3145 for 3/14/21
from datetime import date, time, datetime, timedelta


def main():
    print("Arrival Time Estimator")
    print()
    resume = "y"
    while resume.lower() == "y":
        #inputs
        date_raw = input("Enter date of departure (YYYY-MM-DD): ")
        departure_date = datetime.strptime(date_raw, "%Y-%m-%d")
        time_raw = input("Enter time of departure (HH:MM AM/PM): ")
        departure_time = datetime.strptime(time_raw, "%I:%M %p").time()
        mydatetime = datetime.combine(departure_date,departure_time)
        miles_input = int(input("Enter miles: "))
        speed_input = int(input("Enter miles per hour: "))
        print()

        #outputs
        print("Estimated travel time")
        hours = miles_input // speed_input
        print("Hours: ", hours)
        minutes = int(((miles_input / speed_input)-hours)*60)
        print("Minutes: ", minutes)
        travel_time = mydatetime + timedelta(hours=hours, minutes=minutes)
        new_time = datetime.strftime(travel_time, "%I:%M %p")
        travel_days = mydatetime + timedelta(hours=hours, minutes=minutes)
        new_date = datetime.strftime(travel_days, "%Y-%m-%d")

        print("Estimated date of arrival: ", new_date)
        
        print("Estimated time of arrival: ", new_time)
        #loop
        print()
        resume = input("Continue? (y/n): ")
        print()
    print("Bye!")


if __name__ == "__main__":
    main()
    

