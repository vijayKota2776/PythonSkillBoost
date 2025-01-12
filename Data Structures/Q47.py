def merge_dicts():
    dict1 = {"Alice": 25, "Bob": 22}
    dict2 = {"Charlie": 23, "David": 24}
    merged_dict = {**dict1, **dict2}
    print("Merged Dictionary:")
    print(merged_dict)
merge_dicts()