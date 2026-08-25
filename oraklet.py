import random
svar = ["Ja, helt klart", "Nej, absolut inte", "Fråga igen imorgon", "Det vill du inte veta"]
fråga = input("Fråga oraklet: ")
print("Du frågade: " + fråga)
print(random.choice(svar))
