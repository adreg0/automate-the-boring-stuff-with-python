def comma(ls):
    if len(ls)==0:
        return ""  
    else:
        s=str(ls[0])
        for i in range(1,len(ls)-1):
            s+=','+str(ls[i])
        s+=' and '+str(ls[-1])
        return s

ls = [1,2,3,4,'abc']
string=comma(ls)  
print(string)