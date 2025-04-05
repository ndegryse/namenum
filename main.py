from conversion import name_to_lower

def main():
    usr_name = input("Hello and Welcome! Please enter your name: ")
    print(f"Pleased to meet you {usr_name}! Please standby while we convert your name.")
    usr_lower_name = name_to_lower(usr_name)
    print(f"Testing to lower: {usr_lower_name}")

if __name__ == "__main__":
    main()