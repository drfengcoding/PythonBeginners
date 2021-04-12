def get_max(lst):
    max_value = lst[0]
    for i in range(0, len(lst)):
        if lst[i] > max_value:
            max_value = lst[i]

    # for l in lst:
    #     if l > max_value:
    #         max_value = l

    return max_value


lst = [4, 2, 1, 6, 7, 9]
m_value = get_max(lst)
print(m_value)
