email = input("Email manzillarni vergul bilan kiriting: ")
l_email = email.split(",")
damens = []
for i in l_email:
    i = i.strip()   
    if "@" in i:    
        if damens not in damens:  
            damens.append(damens)
print(damens)

