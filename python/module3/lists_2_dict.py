def lists_2_dict(list1, list2):
    combined_dict = {}
    for key, value in zip(list1, list2):
        combined_dict[key] = value
    return combined_dict
