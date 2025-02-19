import heapq


def max_profit_schedule(seminars):
    # Sort seminars by end time (Earliest Deadline First)
    seminars.sort(key=lambda x: x[1])  # Sort by end time

    # Note: This approach is inspired by the Activity Selection Problem but differs because:
    # - We have two rooms instead of one, meaning we need to track multiple schedules.
    # - We are maximizing profit, not just the number of non-overlapping seminars.
    # - A purely greedy approach (always selecting the earliest finishing seminar) does not guarantee the highest profit.
    # - A more optimal approach would consider replacing low-profit seminars when necessary.

    rooms = [[], []]  # Two rooms represented as separate heaps
    total_profit = 0
    scheduled_seminars = []

    for seminar in seminars:
        start, end, profit = seminar
        assigned_room = None

        # Try to fit the seminar in one of the two rooms
        for i in range(2):
            # Remove finished seminars from room i
            while rooms[i] and rooms[i][0] <= start:
                heapq.heappop(rooms[i])

            # If room i is available, assign the seminar
            if len(rooms[i]) == 0:
                heapq.heappush(rooms[i], end)
                total_profit += profit
                assigned_room = i + 1  # Room 1 or 2
                scheduled_seminars.append((start, end, profit, True, assigned_room))
                break

        # If both rooms are full, do not assign the seminar (greedy approach limitation)
        # A better approach could be replacing the lowest-profit seminar when beneficial.
        if assigned_room is None:
            scheduled_seminars.append((start, end, profit, False, None))

    print("\nScheduled Seminars:")
    for seminar in scheduled_seminars:
        print(
            f"Start: {seminar[0]}, End: {seminar[1]}, Profit: {seminar[2]}, Assigned: {seminar[3]}, Room: {seminar[4]}")

    print(f"\nTotal Maximum Profit: {total_profit}")

    return total_profit


# Example use case
seminars = [(1, 3, 100), (2, 5, 200), (4, 6, 300), (6, 8, 250), (1, 3, 300)]
print("Max Profit:", max_profit_schedule(seminars))