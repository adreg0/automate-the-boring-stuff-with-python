  
def printTable(lists):
    l=[]
    p=len(lists[0])
    for i in range(p):
        for j in range(len(lists)):
             l.append(len(lists[j][i]))
             maxi=max(l)
    for i in range(p):
        for j in range(len(lists)):

             print(lists[j][i].rjust(maxi),end='')        
        print()

tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]
             
printTable(tableData)