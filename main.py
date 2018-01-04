import time

from globals import *

from pattern_storage import pattern_storage
from current_pattern import current_pattern
from pattern_recognition import pattern_recognition

total_start = time.time()

# Determines the length of the data
print("Data length:", data_length)

samples = 0
while end_point < data_length:
    average_line = all_data[:end_point]

    pattern_array = []
    performance_array = []
    pattern_for_recognition = []

    # Store the patterns found since now
    pattern_storage(average_line=average_line,
                    pattern_array=pattern_array, performance_array=performance_array)

    # Determine the current pattern based on the last dots_for_pattern data
    current_pattern(average_line=average_line, pattern_for_recognition=pattern_for_recognition)

    # Perform the pattern recognition
    pattern_recognition(samples=samples,
                        pattern_array=pattern_array, performance_array=performance_array,
                        pattern_for_recognition=pattern_for_recognition)

    # Get one more sample
    samples += 1

    accuracy_average = np.average(accuracy_array)
    print("Backtested accuracy is", str(accuracy_average), "% after ", samples, "samples")

    end_point += 1

total_end = time.time()
print("Script took ", total_end - total_start, " seconds")