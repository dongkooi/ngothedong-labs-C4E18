def get_even_list(non_even_list):
    new_list = []
    for i in range(len(non_even_list)):
        if non_even_list[i] % 2 == 0:
            new_list.append(non_even_list[i])
    return new_list

# list_of_even = get_even_list([1, 4, 5, -1, 10])
# print(list_of_even)