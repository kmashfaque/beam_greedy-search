# implementing least count with branch and bound method

# def fractional_knapsack(weight, value, c):
weight = [10, 20, 30]
value = [60, 100, 120]
c = 50

n = len(weight)
ratio = []
index = 0
WT = 0
X = [0]*n
profit = 0

for i in range(n):
    ratio.append(value[i]/weight[i])

# print(ratio)

enum = enumerate(ratio)
ratio_dict = dict((i,j) for i, j in enum)
# print(ratio_dict)


# GREEDY SELECTION
while len(ratio) > 0:
    maximum = 0
    for r in ratio:
        if r > maximum:
            maximum = r
    
    # removing the used ratio
    ratio.remove(maximum)
    # print(ratio)

    # finding index of this ratio
    for k, v in ratio_dict.items():
        if v == maximum:
            index = k
            break
    del ratio_dict[index]
    print(index)

    # checking the capactys
    if WT + weight[index] < c:
        X[index] = 1
        
        WT = WT + weight[index]

    else:
        x_float = (c - WT)/weight[index]
        X[index] =x_float

        WT = WT + weight[index]
    

    
    profit = profit + (value[index]+ X[index])

print(X)
print(profit)  