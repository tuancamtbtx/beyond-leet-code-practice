def goodDaysToRobBank(security, time):
    n = len(security)
    if time == 0:
        return list(range(n))

    non_increasing = [0] * n
    non_decreasing = [0] * n

    # Fill non_increasing array
    for i in range(1, n):
        if security[i] <= security[i - 1]:
            non_increasing[i] = non_increasing[i - 1] + 1

    # Fill non_decreasing array
    for i in range(n - 2, -1, -1):
        if security[i] <= security[i + 1]:
            non_decreasing[i] = non_decreasing[i + 1] + 1

    # Find all good days
    good_days = []
    for i in range(time, n - time):
        if non_increasing[i] >= time and non_decreasing[i] >= time:
            good_days.append(i)

    return good_days

# Example usage
security1 = [5, 3, 3, 3, 5, 6, 2]
time1 = 2
print(goodDaysToRobBank(security1, time1))  # Output: [2, 3]

security2 = [1, 1, 1, 1, 1]
time2 = 0
print(goodDaysToRobBank(security2, time2))  # Output: [0, 1, 2, 3, 4]

security3 = [1, 2, 3, 4, 5, 6]
time3 = 2
print(goodDaysToRobBank(security3, time3))  # Output: []