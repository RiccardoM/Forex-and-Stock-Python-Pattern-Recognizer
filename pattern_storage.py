from globals import *
from percent_change import percent_change


def pattern_storage(average_line: list, pattern_array: list, performance_array: list):
    # Get the length of the array
    x = len(average_line) - (30 + dots_for_pattern)

    y = 1 + dots_for_pattern

    while y < x:
        pattern = []

        for index in reversed(range(dots_for_pattern)):
            point = percent_change(average_line[y - dots_for_pattern], average_line[y - index])
            pattern.append(point)

        # Create the pattern array and store it
        pattern_array.append(pattern)

        # Take the range of the outcome using 10 values from the 20th after the current point
        outcome_range = average_line[y+20:y+30]

        # Take the current point
        current_point = average_line[y]

        # Get the average value of the outcome
        try:
            average_outcome = np.average(outcome_range)
        except Exception as e:
            print(e)
            average_outcome = 0

        # Get the future outcome for the pattern based on the average outcome value
        future_outcome = percent_change(current_point, average_outcome)

        # Store the outcome value
        performance_array.append(future_outcome)

        y += 1
