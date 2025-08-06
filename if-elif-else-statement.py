temperature = int(input("Enter the temperature in Celsius: "))
if temperature >= 30:
    print("It's a hot day.")
elif temperature >= 20:
    print("It's a warm day.")
elif temperature >= 10:
    print("It's a cool day.")
else:
    print("It's a cold day.")