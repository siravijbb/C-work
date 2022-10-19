b = 5.0000000 
a = float(input("K: "))
v = float(input("V: "))
r = float(input("Round: "))
s = float(input("Shunt: "))
e = float(input("External: "))
c = v / (s+e)
print(c)
for a in range (int(b)):
        d = c*a/b
        print("KO =" + str(a) + " v/s")
        print("Ia = "+ str(d) + " A")
        f = a * (r/60)
        s = f
        f = v - f
        j = f / (2.8+1.2)
        print(str(s) +" Eb")
        print(str(j) + " iA")  
        pin = v * j + v * d
        print(str(pin) +" W")
        pout = s * j
        print(str(pout) +"W")
        if pout/pin < 1.000000:
            n = pout/pin*100
        else:
            n =	pin/pout*100
        
        print("n " + str(n))

        w = 2*3.14*(r/60)
        t = pout / w
        print("w = " + str(w))
        print("rad/s t"+ str(w))
        print("T = " + str(t) + " NM \n \n")
        
