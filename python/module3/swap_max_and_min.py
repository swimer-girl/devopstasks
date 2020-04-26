def swap_max_and_min(unique_list):
    if len(unique_list) != len(set(unique_list)):
        raise ValueError()
    i, j = [f(range(len(unique_list)), key=unique_list.__getitem__) for f in [min, max]]
    unique_list[i], unique_list[j] = unique_list[j], unique_list[i]
    return unique_list
