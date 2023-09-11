def selection_sort(num_list):
    for i_mn in range(len(num_list)):
        for curr in range(i_mn, len(num_list)):
            if num_list[curr] < num_list[i_mn]:
                num_list[curr], num_list[i_mn] = num_list[i_mn], num_list[curr]
    return num_list

num_list = [4, 9, 7, 6, 3, 2]
selection_sort(num_list)
print(num_list)
