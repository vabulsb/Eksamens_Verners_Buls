skaitli = []
for i in range(10):
    skaitlis = int(input("Ievadiet skaitli: "))
    skaitli.append(skaitlis)

print("Dalāmie ar 3:")
for skaitlis in skaitli:
    if skaitlis % 3 == 0:
        print(skaitlis)