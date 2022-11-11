N = int(input("ievadiet žetonu skaitu "))
m1 = int(input("ievadiet pirmo dalītāju "))
m2 = int(input("ievadiet otro dalītāju "))
g = int(input("kustību skaits "))

skaitlis = [i for i in range(1, N+1) if i%m1==0 or i%m2==0]
counter = 0

while counter<g:
    new_list = []
    a = int(input())
    b = int(input())
    
    minimum, maximum = min(a,b), max(a,b)
    for n in skaitlis:
        if n<minimum or n>maximum:
            new_list.append(n)
    skaitlis = new_list
    counter=counter+1

print(len(skaitlis))