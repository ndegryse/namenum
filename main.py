from conversion import name_to_lower
from conversion import characters_to_numbers
from conversion import sum_of_numbers
from error_check import check_user_input


def main():
    usr_name = input("Hello and Welcome! Please enter your first name: ")
    print(f"Pleased to meet you {usr_name}! Please standby while we convert your name.")
    user_name_acceptable = check_user_input(usr_name)
    print (f"Testing {user_name_acceptable}")
    if user_name_acceptable == True:
        usr_lower_name = name_to_lower(usr_name)
        print(f"Testing to lower: {usr_lower_name}")
        usr_num_name = characters_to_numbers(usr_lower_name)
        print(f"Your name according to the positions of the characters in the alphbet is {usr_num_name}")
        usr_sum_name = sum_of_numbers(usr_num_name)
        print(f"Your name sum is: {usr_sum_name}")
    else:
        print("Testing error")


if __name__ == "__main__":
    main()