from collections import deque

list_=[1,4,2,3,5,6]
new_list=deque(list_)
new_list.rotate(-3)
print(list(new_list))

