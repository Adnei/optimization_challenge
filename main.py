# Time: O(n log n)
# Memory space:
import random as random
from bisect import bisect_right


def random_movies(n_movies):
    'create random data'
    return [round(random.uniform(1.01, 3.00), 2) for i in range(n_movies)]
# =============================================================================


def find_min_days(movies_duration):
    def short_movies(x):
        'Filter fn -> Find duration < 2.00'
        return x < 2.00

    def find_le(a, x):
        'Find rightmost value less than or equal to x'  # O(log n)
        i = bisect_right(a, x)
        if i:
            return i-1  # a[i-1]
        return -1  # should raise ValueError
    short_movies_duration = list(
        filter(short_movies, movies_duration))  # O(n) ??
    days = len(movies_duration) - len(short_movies_duration)
    short_movies_duration.sort()  # O(n log n) # should sort before filtering
    while(True):  # O(n log n) (worst case) --> Const in best case
        if short_movies_duration[0] + short_movies_duration[1] > 3:
            break
        idx = find_le(short_movies_duration, 3 - short_movies_duration[0])
        if idx == -1:
            # should throw error!!!
            break
        short_movies_duration.pop(idx)
        short_movies_duration.pop(0)
        days = days + 1
        if len(short_movies_duration) == 0:
            break
    return days + len(short_movies_duration)


# 1k is the max N value stated by the exercice
duration_list = random_movies(1000)
duration_example = [1.90, 1.04, 1.25, 2.5, 1.75]
_duration_ex = [1.01, 1.01, 1.99, 2.00, 3.00, 1.55, 1.25, 1.75]

find_min_days(duration_example)
find_min_days(duration_list)
find_min_days(_duration_ex)
