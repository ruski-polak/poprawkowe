#abs

def zad3(x,y):
    tmp_r = []
    min = 10000000000

    for i in range(len(x)):
        for i2 in range(len(y)):
            tmp_r = x[i]-y[i2]
            #print(abs(tmp_r))
            if abs(tmp_r) < min:
                min = abs(tmp_r)
                tab1 = i
                tab2 = i2
                #print(tab1) - indeks
                #print(tab2) - indeks
            elif abs(tmp_r) == 0:
                return x[i],y[i2]
    #print(tab1,tab2)
    print(x[tab1], y[tab2])

tmp = [-1, 5, 10, 20, 28, 3]
tmp_ = [26, 134, 135, 15, 17]
zad3(tmp,tmp_)