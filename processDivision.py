def divide():
    try:
        a = float(input("Enter the numerator: "))
        b = float(input("Enter the denominator: "))
        result = a/b
    #except:
        #print("Something went wrong!")
    except ZeroDivisionError:
        print("You tried to divid by zero")
        divide()
    except ValueError:
        print("You entered a non-numerical value")
        divide()

    else:
        print("Result = ", result)

def main():
    divide()
main()