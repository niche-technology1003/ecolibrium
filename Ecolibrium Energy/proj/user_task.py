from datetime import datetime


weekday_dict = {"Monday": 0, "Tuesday": 1, "Wednesday": 2, "Thursday": 3, "Friday": 4, "Saturday": 5, "Sunday": 6}
weekday_dict_reverse = {0: "Monday", 1: "Tuesday", 2: "Wednesday", 3: "Thursday", 4: "Friday", 5: "Saturday", 6: "Sunday"}
current_time = datetime.now().strftime("%H:%M:%S")
current_weekday = datetime.now().weekday()
current_weekday_string = datetime.now().strftime("%A")


def matching_day(week_day_one, week_day_two, user_input_len, start_time, end_time):
    if user_input_len == 5:
        if current_time < start_time:
            return start_time
        else:
            return False

    elif start_time <= current_time <= end_time:
        return True
    elif start_time < current_time <= end_time:
        return weekday_dict_reverse[week_day_one] + " " + end_time
    elif current_time > end_time:
        return weekday_dict_reverse[week_day_two] + " " + start_time
    else:
        return weekday_dict_reverse[week_day_one] + " " + start_time


def user_input(input_string):
    user_input_len = len(input_string.split())
    if user_input_len == 5:
        task_type, user, country, start_time, end_time = input_string.split()
        day_one, day_two = current_weekday_string, current_weekday_string
    elif user_input_len == 11:
        task_type, user, country, remaining_str = input_string.split(" - ")
        start_time, end_time, day_one, _, day_two = remaining_str.split()
    else:
        raise ValueError("Input not in proper format. Check README file.")

    week_day_one = weekday_dict[day_one]
    week_day_two = weekday_dict[day_two]

    if min(week_day_one, week_day_two) > current_weekday or current_weekday > max(week_day_one, week_day_two):
        return weekday_dict_reverse[week_day_one] + " " + start_time

    elif max(week_day_one, week_day_two) < current_weekday or current_weekday < min(week_day_one, week_day_two):
        return weekday_dict_reverse[week_day_two] + " " + start_time

    elif week_day_one == current_weekday:
        return matching_day(week_day_one, week_day_two, user_input_len, start_time, end_time)

    elif week_day_two == current_weekday:
        return matching_day(week_day_two, week_day_one, user_input_len, start_time, end_time)


if __name__ == "__main__":
    output = user_input("Incorrect String")
    print(output)
