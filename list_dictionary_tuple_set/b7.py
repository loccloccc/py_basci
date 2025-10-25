a = [1, 2, 3, 2, 4, 1, 5]
new_list = []
for i in a :
    if i not in new_list :
        new_list.append(i)

print(new_list)