print("**********************")
print("Simple BMI Calculator")
print("  by Ajay Kareer")
print(" *******************")
def main():
    a = (input("Enter your name: "))
    print("Hi,"+ a+"!!" " Do you know your height in Metres ?")
    s = (input("Type \"yes\" or \"no\": "))
    while s != "yes" and s != "no" and s != "Yes" and s != "No":
        print("Please enter \"yes\" or \"no\"")
        s = (input("Type \"yes\" or \"no\": "))
    if s == "yes":
        print("ok, cool :)")
    elif s == "no":
        print("No worries, let's calculate your height in Metres!!")
        j = float(input("Enter your height in \"Feet\": "))
        k = float(input("Enter your height in \"Inches\": "))
        l = round((j * 0.3048) + (k * 0.0254), 2)
        print("Your height in Metres is:", l)
        print("good, now...")
    while True:
        try:
            b = float(input("Enter your height in (M): "))
        except ValueError:
            print("Enter Numeric Value")
            continue
        else:
            break
    while True:
        try:
            c = float(input("Enter your weight in (KG): "))
        except ValueError:
            print("Enter Numeric Value")
            continue
        else:
            break
    print(a + " your BMI is: ")
    d = round(c/(b**2),2)
    print(d)

    print("Wanna check if you are fit or overweight ?")

    e = input("Type (\'y\' for yes/ \'n\' for no): ").lower()
    while e != "y" and e != "n":
        print("Enter valid input \"y\" or \"n\"")
        e = input("(\'y\' for yes/ \'n\' for no): ").lower()
    if e == "y" and d < 25:
        print("You are fit, healthy and not overweight.. \m/")
    elif e == "n":
            print("Ok Bye..!!")
            input()
            exit()
    else:
        print("You are overweight.. :(")

    print("Wanna exit or run again ?")
    f = input("Type \"q\" to exit or \"yes\" to run again:  ").lower()
    while f != "q" and f != "yes":
        print("Enter Valid Input")
        f = input("Type \"q\" to exit or \"yes\" to run again:  ").lower()
    if f == "q":
        print("Ok Bye..!!")
        input()
        exit()
    else:
        main()
main()