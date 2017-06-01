number = 23
guess = int(input("Enter an integer : "))

if guess == number:
    print("Congratulations, you guessed it.")
    print("(but you don't win any prizes!)")
elif guess < number:
    print("No, it is little higher than that.")
else:
    print("No, it is little lower than that.")

print("Done")
