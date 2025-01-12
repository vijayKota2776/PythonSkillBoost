def invert_dict():\
    original_dict = {"Alice": 25, "Bob": 22, "Charlie": 23, "David": 24}\
    if len(original_dict) == len(set(original_dict.values())):
        inverted_dict = {v: k for k, v in original_dict.items()}
        print("Inverted Dictionary:")
        print(inverted_dict)
    else:
        print("Values are not unique. Cannot invert the dictionary.")
invert_dict()