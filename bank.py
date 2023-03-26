def main():
    # create variable greeting in lowercase without whitespaces
    greeting = input("Greeting: ").strip().lower()
    print(value(greeting))

def value(greeting):
    # variable dollars
    dollars = 0

    # conditionals for greetings
    if greeting.startswith("hello"):
        dollars += 0
    elif greeting.startswith("h"):
        dollars += 20
    else:
        dollars += 100

    # print dollars
    return f"${dollars}"

if __name__ == "__main__":
    main()
