a_list = [1,2,3,4,5,6,7,8,9]

another_list = [3,4,5,6]

third_list = [x for x in a_list if x not in another_list]

print third_list