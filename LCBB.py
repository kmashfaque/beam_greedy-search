# implementing least count with branch and bound method

weight = [10, 20, 30]
value = [60, 100, 120]
c = 50


def fractional_knapsack(weight, value, c):
    

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

        # checking the capacity
        if WT + weight[index] < c:
            X[index] = 1
            
            WT = WT + weight[index]

        else:
            x_float = (c - WT)/weight[index]
            X[index] =x_float

            WT = WT + weight[index]
        

        
        profit = profit + (value[index]+ X[index])

    return profit, X


def branch_bound(weight, value, c):
    item_selected = []  # stores indices of selected items
    n = len(weight) 
    UB = 0 # Upper Bound (but stored as negative)
    item = 0 # current item index (branching level)

    profit, X = fractional_knapsack(weight, value, c)

    LB = -profit

    for x in range(len(X)):
        if X[x] == 1:
            UB = UB + value[x]
    UB = -UB
    print("UB is, ", UB)
    print("LB is, ", LB)

    # start branching

    while item < n:
        wt_list = []
        val_list = []

        for j in range(n):
            if j != item:
                val_list.append(value[j])
                wt_list.append(weight[j])

        print("wt list is",wt_list)
        print("val list is",val_list)
        UB1=UB
        LB1=LB
        left_branch_potential=UB1-LB1
        UB2=0
        
        LB2, X2=fractional_knapsack(wt_list,val_list,c)
        LB2=-LB2
        print("LB2 is",LB2)
        print("X2 is",X2)


        for y in range(len(X2)):
            if X2[y]==1:
                UB2=UB2+val_list[y]
                
        UB2=-UB2
        print("ub2 is",UB2)
        
        right_branch_potential=UB2-LB2
        print("right_branch_potential is",right_branch_potential)
        
        if left_branch_potential<right_branch_potential:
            print("left_branch_potential is less than right_branch_potential")
            item_selected.append(item)
            item+=1        
        elif left_branch_potential==right_branch_potential:
            if UB1<UB2:
                print("left_branch_potential is equal to right_branch_potential so here we consider Ub values and here left node has less UB value")
                item_selected.append(item)
                item+=1
            elif UB2<UB1:
                print("left_branch_potential is equal to right_branch_potential so here we consider Ub values and here right node has less UB value")
                UB=UB2
                LB=LB2
                item+=1
            else:
                print("here both have same vales of Ub and even left_branch_potential and right_branch_potential so we can consider any")
                item_selected.append(item)
                item+=1  
        else:
            print("right_branch_potential is lesser so we won't include it")
            UB=UB2
            LB=LB2
            item+=1
                
    print("item selected", item_selected)



branch_bound(weight, value, c)

