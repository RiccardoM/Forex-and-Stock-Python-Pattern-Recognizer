

def percent_change(starting_point, current_point):
    """
    Computes the percentage difference between two points
    :return: The percentage change between starting_point and current_point
    """
    default_change = 0.00001
    try:
        change = ((float(current_point) - starting_point) / abs(starting_point)) * 100.00
        if change == 0.0:
            return default_change
        else:
            return change
    except:
        return default_change
