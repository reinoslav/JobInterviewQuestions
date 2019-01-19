def flatten(input_arr, flat_arr=None):
    if not flat_arr:
        flat_arr = []

    for item in input_arr:
        if not isinstance(item, list):
            flat_arr.append(item)
        else:
            flatten(item, flat_arr)

    return flat_arr


arr = [1, [2, [3, 4], 5], [6, [7, 8, 9]], 10]

print(flatten(arr))
