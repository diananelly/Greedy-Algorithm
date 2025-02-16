def activity_selection(start_times, finish_times):
    #Combines the start and finish times into a list of activities
    activities= list(zip(start_times, finish_times))

    #Sort activities based on finish times
    activities.sort(key=lambda x: x[1])

    selected_activities = []
    #The finish time of the last selected activity
    last_finish_time =0

    for activity in activities:
        if activity[0] >= last_finish_time:
            selected_activities.append(activity)
            last_finish_time = activity[1]
    return selected_activities

#Example usage
if __name__ == '__main__':
    num_bands = int(input('Enter the number of bands:'))
    start_times = []
    finish_times = []

    for i in range(num_bands):
        start = int(input(f'Enter the start time for band {i+1}:'))
        finish = int(input(f'Enter the finish time for band {i+1}:'))
        start_times.append(start)
        finish_times.append(finish)


    selected = activity_selection(start_times, finish_times)
    print("Selected bands performances")
    for idx, activity in enumerate(selected,1):
        print(f"Band {idx}: Start ={activity[0]}, Finish={activity[1]}")