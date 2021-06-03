def find_cycle(array):
    slow_i, fast_i = 0, 1
    while slow_i < len(array) and fast_i < len(array):
        slow_num = array[slow_i]
        fast_num = array[fast_i]
        if slow_num == fast_num:
            slow_num_indexes = [i for i, x in enumerate(array) if x == slow_num]
            return ''.join(array[slow_num_indexes[0]:slow_num_indexes[1]])
        slow_i += 1
        fast_i += + 2
    return False