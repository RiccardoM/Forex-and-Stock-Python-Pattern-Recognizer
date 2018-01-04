import matplotlib.pyplot as plt

from globals import *
from percent_change import percent_change

def pattern_recognition(samples: int, pattern_array: list, performance_array: list, pattern_for_recognition: list):
    """

    :return:
    """

    # Identifiers whenever a similar pattern has been found or not
    found_pattern = False

    # Contains the array of patterns to be plotted
    plot_pattern_array = []

    # Contains the array of outcomes predicted by the identified patterns
    predicted_outcomes_array = []

    for pattern in pattern_array[:-5]:
        # Tells if enough similarities have been found in order to consider the pattern similar to the one currently
        #samples considered
        similarities_are_found = True

        # Compute the percent changes for each point of the two patterns, the one that we are considering and the
        # current one obtained from the last 10 entries of the data
        similarities_array = []
        for index in range(dots_for_pattern):
            # Compute the values of similarity only if it's the first value to be computed, or if the previous one was
            # at least 50% similar
            if index == 0 or similarities_array[index - 1] > 50:
                similarities_array.append(100.00 - abs(percent_change(pattern[index], pattern_for_recognition[index])))

            # Otherwise just break the for loop and stop computing similarities
            else:
                similarities_are_found = False
                break

        # If sufficient similarities were found continue on
        if similarities_are_found:
            # Compute how similar are the two patterns
            how_similar = np.sum(similarities_array) / dots_for_pattern

            if how_similar > pattern_similarity_value:
                # If a pattern satisfies the similarity value, remember that a pattern was found and append that
                # pattern to the list of patterns to plot
                found_pattern = True
                plot_pattern_array.append(pattern)

    prediction_array = []

    if found_pattern:
        # If at least one similar pattern was found then print all the pattern that are in the array of patterns to be
        # plotted
        xp = np.arange(0, dots_for_pattern, 1)
        if plot_data:
            plt.figure(figsize=(10, 6))

        for pattern in plot_pattern_array:
            pattern_index = pattern_array.index(pattern)

            # Determine the color based on the prediction of the pattern
            if performance_array[pattern_index] > pattern_for_recognition[dots_for_pattern - 1]:
                # If the prediction of the pattern is greater than the value of the pattern use the green
                plot_color = '#24BC00'
                prediction_array.append(1.00)

            else:
                # Otherwise use the red
                plot_color = '#D40000'
                prediction_array.append(-1.00)

            if plot_data:
                plt.plot(xp, pattern)
                predicted_outcomes_array.append(performance_array[pattern_index])

                # Plot the dot representing the value predicted by the pattern
                # The color of the dot will be red if the outcome is good, and red otherwise
                plt.scatter(dots_for_pattern + 5, performance_array[pattern_index], c=plot_color, alpha=.3)

        # Get the average of 10 future values to determine the chart gait and plot the dot as a reference of what is
        # going to happen
        real_outcome_range = all_data[end_point+20:end_point+30]
        real_average_outcome = np.average(real_outcome_range)
        real_movement = percent_change(all_data[end_point], real_average_outcome)

        if plot_data:
            plt.scatter(40, real_movement, s=25, c='#54FFF7')

        # Get the average of the predicted values and plot a dot representing what the system has predicted will happen
        predicted_average_outcome = np.average(predicted_outcomes_array)

        if plot_data:
            plt.scatter(40, predicted_average_outcome, s=25, c='b')

        # Also plot the patter that has been recognized with a different line width and color to make it stand out on
        # the graph with all the similar patterns
        if plot_data:
            plt.plot(xp, pattern_for_recognition, '#54FFF7', linewidth=3)

            plt.grid(True)
            plt.title("Pattern recognition")
            plt.suptitle("Patterns recognized after {} samples".format(samples))
            plt.savefig(pattern_images_folder + "patter_recognition_{}_samples.png".format(samples))

        print(prediction_array)

        prediction_average = np.average(prediction_array)
        print(prediction_average)

        if prediction_average < 0:
            print("Drop predicted")
            print(pattern_for_recognition[29])
            print(real_movement)
            if real_movement < pattern_for_recognition[29]:
                accuracy_array.append(100)
            else:
                accuracy_array.append(0)

        if prediction_average > 0:
            print("Rise predicted ")
            print(pattern_for_recognition[29])
            print(real_movement)
            if real_movement > pattern_for_recognition[29]:
                accuracy_array.append(100)
            else:
                accuracy_array.append(0)