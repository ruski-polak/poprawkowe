
def zad1(x):
    for i in x:
        if int(i) % 2 == 0:
            return True      


plik1 = open("wyniki.txt" , "w")
licznik = 0
suma = 0
max1 = 0
min1 = 100000000000
count = 0
tmp = []
#final_count = 0
with open("cyfry.txt" , "r") as f:
    for line in f:
        a = line[:-1].split(" ")
        #print(type(a)) ---> class list
        if zad1(a):
            licznik+=1
        ### podpunkt b
        for i in a:
            count +=1
            suma1 = 0
            for k in i:
                suma1 += int(k)
                print(suma1)
            if suma1 >= max1:
                max1 = suma1
                number = i
            if suma1 <= min1:
                min1 = suma1
                number1 = i
        ### podpunkt c
            countc = 0
            past = 0
            for k2 in i:
                countc +=1
                if int(k2) > past:
                    past = int(k2)  
                else:
                    break
                if countc == len(i):
                    tmp.append(str(i))
                    
    # print(max1)
    # print(number)
    #print(final_count)

    print("Done")
    plik1.write("Zadanie 1a: " + str(licznik) + "\n")
    plik1.write("Zadanie 1b: " + "\n") 
    plik1.write("Najwieksza: " + str(number) + "\n")
    plik1.write("Najmniejsza: " + str(number1) + "\n")
    plik1.write("Zadanie 1c:" + str(tmp) + "\n")






    #print(type(a1)) --> int
    #max1.append(int(a1))
    # b1 = str(a1)
    # max1.append(b1)
    # print(sum(list(map(int,"".join(map(str,max1))))))
    # b2 = str(a2)
    # min1.append(b2)
    # print(sum(list(map(int,"".join(map(str,min1))))))
