numbers = [10, 20, 30, 40, 50]
print(f"Initial list: {numbers}")
numbers.append(60)
print(f"After appending 60: {numbers}")
numbers.insert(2, 25)
print(f"After inserting 25 at index 2: {numbers}")
numbers.remove(40)
print(f"After removing 40: {numbers}")
popped_element = numbers.pop()
print(f"After popping the last element ({popped_element}): {numbers}")
print(f"Final list: {numbers}")