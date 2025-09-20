text = "Ism:Ali, Familiya:Valiyev, Yil:2002"
l = text.split(",")
for i in l:
    i = i.strip()   
    print(i.replace(":", ": "))