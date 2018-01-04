from globals import *
from percent_change import percent_change

def current_pattern(average_line, pattern_for_recognition: list):
    """
    Create a pattern that will be compared to in-memory patterns formed by the last dots_for_pattern entries of the data
    """
    # This pattern will be based on the last 10 elements of the data
    for index in reversed(range(1, dots_for_pattern + 1)):
        pattern = percent_change(average_line[- dots_for_pattern - 1],
                                 average_line[- index])
        pattern_for_recognition.append(pattern)
