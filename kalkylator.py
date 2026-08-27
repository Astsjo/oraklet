# Användaren ger tal och vad de vill göra
num1 = float(input("Första talet: "))
print(" ")
operator = input("Välj operator (+, -, *, /): ")
print(" ")
num2 = float(input("Andra talet: "))

# Räknaren
if operator == "+":
    answer = num1 + num2
elif operator == "-":
    answer = num1 - num2
elif operator == "*":
    answer = num1 * num2
elif operator == "/":
    answer = num1 / num2
else:
    print(" ")
    print("Error")

# Svar
print(" ")
print(f"Svaret är {answer}")
print(" ")