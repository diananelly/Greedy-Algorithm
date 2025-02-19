def activity_selection(start_times, finish_times):
    """
    selects the maximum number of non-overlapping activities

    parameters:
    start_times (list): list of start times for activities
    finish_times (list): list of corresponding finish times

    returns:
    list: list of selected activities (start, finish)
    """
    activities = list(zip(start_times, finish_times))  # combines start and finish times into a list

    activities.sort(key=lambda x: x[1])  # sort activities based on finish times

    selected_activities = []
    last_finish_time = 0  # finish time of the last selected activity

    for activity in activities:
        if activity[0] >= last_finish_time:  # check if activity can be selected
            selected_activities.append(activity)
            last_finish_time = activity[1]  # update last finish time

    return selected_activities


# example usage
if __name__ == '__main__':
    num_bands = int(input('Enter the number of bands: '))
    start_times = []
    finish_times = []

    for i in range(num_bands):
        start = int(input(f'Enter the start time for band {i + 1}: '))
        finish = int(input(f'Enter the finish time for band {i + 1}: '))
        start_times.append(start)
        finish_times.append(finish)

    selected = activity_selection(start_times, finish_times)

    print("Selected bands performances:")
    for idx, activity in enumerate(selected, 1):
        print(f"Band {idx}: Start = {activity[0]}, Finish = {activity[1]}")
