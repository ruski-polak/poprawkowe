def function(a):
    tmp = []
    tmp1 = []
    tmp2 = []
    suma = 0
    for i in range(len(a)):
        a1 = a[(i-len(a))+1] #->12; +2->3; 
        a2 = a[(i-len(a))+2]
        a3 = a[(i-len(a))+3]
        a4 = a[(i-len(a))+4]
        a5 = a[(i-len(a))+5]
        a6 = a[(i-len(a))+6]
        a7 = a[(i-len(a))+7]
        a8 = a[(i-len(a))+8]
    b = a1+a2
    b2 = a2+a3
    b3 = a3+a4
    b4 = a4+a5
    b5 = a5+a6
    b6 = a6+a7
    b7 = a7+a8
    b8 = a8+a1

    if b7 + a4 == suma:
        tmp1.append(a4)
        tmp1.append(a7)
        tmp1.append(a8)
    if b5 + a3 == suma:
        tmp2.append(a3)
        tmp2.append(a5)
        tmp2.append(a6)
    if b6 + a2 == suma:
        tmp.append(a2)
        tmp.append(a7)
        tmp.append(a6)

    tmp_odp = []
    tmp_odp.append(tmp)
    tmp_odp.append(tmp1)
    tmp_odp.append(tmp2)
    print(tmp_odp)

    
tmp = [12,3,1,2,-6,5,-8,6]
function(tmp)
#-8 6 2        
#print(len(a)) --> 8
