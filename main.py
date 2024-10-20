# YOUR CODE HERE
def summation(list1, list2):
    return [x + y for x, y in zip(list1, list2)]

def find_min_max(lst):
    return min(lst), max(lst)

len_list = int(input())

list1 = [int(input()) for i in range(len_list)]
list2 = [int(input()) for i in range(len_list)]

result_list = summation(list1, list2)

print(result_list)

min_val, max_val = find_min_max(result_list)
print(f”( {min_val},  {max_val}”)
