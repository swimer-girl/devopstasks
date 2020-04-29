def multiple_in_range(start, stop):
    return [i for i in range(start, stop+1) if (i % 7 == 0) and (i % 5 != 0)]

