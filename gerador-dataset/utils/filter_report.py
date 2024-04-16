import numpy as np


def filter_report(array, crmp):
    """
    Filter report to have only one value per window_size
    Args:
        array (np.ndarray): Report to be filtered
        crmp (dict): Dictionary with parameters

    Returns:
        np.ndarray: Filtered report
    """

    num = crmp["window_size"]
    time_skip = crmp["tpl_time_skip"]
    time_estabilize = crmp["time_estabilize"]
    time_skip += time_estabilize
    array = array[array[:, 0].astype(int) >= time_skip]
    res = []
    last_found = None
    last_mult_found = None
    for x in array[:, 0].astype(int):
        if last_found is None:
            last_mult_found = x
            res.append(x)
        else:
            next_mul = last_mult_found + num
            if x % num == 0:
                last_mult_found = x
                res.append(x)
            elif x < next_mul:
                last_found = x
            elif x > next_mul:
                dist_left = abs(next_mul - last_found)
                dist_right = abs(next_mul - x)
                if dist_left < dist_right:
                    res.append(last_found)
                else:
                    res.append(x)
                last_mult_found = last_mult_found + num
        last_found = x
    values = np.array(res)
    indexes = np.where(np.isin(array[:, 0].astype(int).reshape(-1, 1), values))[0]
    filtered = array[indexes]
    return filtered
