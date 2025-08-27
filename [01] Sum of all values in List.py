List = [1,1]
while True:
    List_Sum = sum(List)
    List.append(List_Sum)

    if List_Sum >= 10000:
        break
print(List)