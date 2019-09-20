import math;
Unidad=["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
Decena=["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
Centena=["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
Miles=["","M","MM","MMM"]
i=0
for i in range (4000):
    u= i % 10
    d=int(math.floor(i/10))%10
    c=int(math.floor(i/100))%10
    m=int(math.floor(i/1000))%10
    if(i>=1000 and i<=3999): 
     print(Miles[m]+Centena[c]+Decena[d]+Unidad[u])
    else:
        if(i>=100): 
         print(Centena[c]+Decena[d]+Unidad[u])
        else:
            if(i>=10):
              print(Decena[d]+Unidad[u])
            else:
              print(Unidad[i])