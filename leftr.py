n = int(input("Enter the number of productions : "))

prod = []
line = []
lhs = []
rhs = []
mark = []

print("Enter the productions : ")
for i in range(n) :
    prod.append(input(str(i+1) + ": "))

for x in prod :
    line = x.split('->')
    lhs.append(line[0])
    rhs.append(line[1].split('|'))

print()    
for x in lhs :
    mark.clear()
    i = lhs.index(x)  
    for y in rhs[i] :
        if x == y[0] :
            print("Direct left recursion in " + str(x) + "->" + str(y))
            mark.append(y)
            new_x = x+'\''
            if new_x not in lhs :
                lhs.append(new_x)
                new_y = [y[1:]+x+'\'']
                rhs.append(new_y)
                rhs[-1].append('eps')
            else :
                k = int(lhs.index(new_x))
                rhs[k].append(y[1:]+x+'\'')
    for rem in mark :
        rhs[i].remove(rem)
    if mark :
        for j in range(len(rhs[i])) :
            rhs[i][j] = rhs[i][j]+x+'\''
    mark.clear()

  
    for y in rhs :
        if rhs.index(y) > i and rhs.index(y) < n:
            for z in y :
                if lhs[i] == z[0] :
                    print("Indirect left recursion in " + str(lhs[i]) + "*=>" + str(z))
                    mark.append(z)
                    for k in rhs[i] :
                        y.append(k+z[1:])       
            for rem in mark :
                y.remove(rem)

print("\nProductions with left recursion eliminated :")
for x in lhs :
    print(str(x) + "->", end = '')
    i = lhs.index(x)
    for y in rhs[i] :
        if rhs[i].index(y) != len(rhs[i])-1 :
            print(str(y)+'|', end = '')
        else :
            print(str(y))