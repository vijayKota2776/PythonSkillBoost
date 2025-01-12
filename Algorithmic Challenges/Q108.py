import itertools

def generate_permutations(lst):
    return list(itertools.permutations(lst))
user_list = list(map(int, input("Enter a list of distinct elements (space-separated): ").split()))
permutations = generate_permutations(user_list)
print("All permutations:")
for perm in permutations:
    print(perm)
