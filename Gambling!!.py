import random
import time

while restart:
    point = 10
    cont = True
    print(" ")

    while cont:
        # Användaren förlorar om de har inga poäng kvar
        InvalidNumber = True
        if point > 0:
            while InvalidNumber:
               # Användaren väljer sin gissning och hur mycket de lägger på sin gissning
               print(" ")
               choice = input("Datorn står och skakar två tärningar i handen. Tror du den kommer att slå mindre, större, eller exact 6: ")
               print(" ")
               amount = int(input(f"Hur mycket vill du lägga (du har {point} just nu): "))
               print(" ")
               if (point - amount) < 0:
                    print("Du kan inte välja mer än poängen du har!")
               else:
                InvalidNumber = False
                point = point - amount

            # Datorns slag, sätts slumpat
            rnd_num = random.randint(1, 12)
            print("Datorn kastar tärningarna, de studsar omkring")
            time.sleep(1.2)
            print(" ")
            print("En av tärningarna snurrar...")
            time.sleep(2.4)
            print(" ")
            print(f"Datorn slog {rnd_num}")

            # Kollar om gissningen är korrekt och updaterar vinsten/förlusten
            if (choice.lower() == "mindre") and (rnd_num < 6):
                print("Du gissade rätt, du vann!")
                amount = amount*2
            elif (choice.lower() == "större") and (rnd_num > 6):
                print("Datorn fick större än 6, du vann!")
                amount = amount*2
            elif (choice.lower() == "exact" or "6" or "exact 6") and (rnd_num == 6):
                print("Den fick exact 6, du vann stort!")
                amount = amount*4
            else:
                print("Du gissade fel, du förlorade.")
                amount = 0

            # Nya summan sätts
            point = point + amount

            # Användaren väljer om de vill fortsätta
            cont_choice = input("Vill du fortsätta (y/n): ")
            if (cont_choice.lower() == "y") or (cont_choice.lower() == "yes") or (cont_choice.lower() =="ja") or (cont_choice.lower() == "j"):
                cont = True
            else:
                cont = False
                print(" ")
                print(f"Tack för att du spelade, du slutade med {point} poäng!")
                print(" ")
        else:
            print(" ")
            game_over = input("Du har inga poäng kvar! Vill du starta om (y/n): ")
            print(" ")
            if (game_over.lower() == "y") or (game_over.lower() == "yes") or (game_over.lower() == "n") or (game_over.lower() == "no") or (game_over.lower() == "ja") or (game_over.lower() == "nej"):
                restart = True
            else:
                restart = False
            cont = False