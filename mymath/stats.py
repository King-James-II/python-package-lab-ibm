# stats.py

def mean(numbers):
    """
    This function calculates the mean (average) of the given list of numbers.

    Parameters:
    numbers (list): A list of numbers.

    Returns:
    float: The mean of the given list of numbers.
    """
    return sum(numbers) / len(numbers)

def median(numbers):
    """
    This function calculates the median of the given list of numbers.

    Parameters:
    numbers (list): A list of numbers.

    Returns:
    float: The median of the given list of numbers.
    """
    numbers.sort()

    if len(numbers) % 2 == 0:
        median1 = numbers[len(numbers) // 2]
        median2 = numbers[len(numbers) // 2 - 1]
        mymedian = (median1 + median2) / 2
    else:
        mymedian = numbers[len(numbers) // 2]
    
    return mymedian
