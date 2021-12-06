def bubblesort(list):
    count = 0
    for i in range(len(list)-1):
        if list[i] > list[i+1]:
            list[i],list[i+1] = list[i+1],list[i]
            count += 1            
    if count == 0:
        return list
    else:
        return bubblesort(list)

print(bubblesort(list))
