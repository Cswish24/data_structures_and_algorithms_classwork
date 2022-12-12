
def activity_max(activity_list):
    activity_list.sort(key=lambda item: item[1])
    optimal_activities = [activity_list[0]]
    for activity in activity_list:
        if activity[0] >= optimal_activities[-1][1]:
            optimal_activities.append(activity)
    return optimal_activities


activites = [[1, 3], [1, 4], [0, 2], [2, 5],
             [2, 3], [5, 8], [5, 6], [6, 9], [7, 8]]

print(activity_max(activites))
