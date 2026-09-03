print(" ")
deltagare = int(input("Hur många deltagare: "))
print(" ")

a = 0
b = 1
x = 0

while deltagare > a:
    a = b
    b = b + a
    x += 1

print(f"Deltagare Nr {deltagare} försvinner på ö {x}")
print(" ")