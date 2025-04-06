from conversion import name_to_lower
from conversion import characters_to_numbers
from conversion import sum_of_numbers
from error_check import check_user_input
import time

def main():
    #Call for user input.. Start of program
    usr_name = input("Hello and Welcome! Please enter your first name: ")
    print(f"Pleased to meet you {usr_name}! Please standby while we convert your name...")
    time.sleep(1)
    print("Beep Boop Beep")
    time.sleep(2)
    print("Calculating...")
    time.sleep(2)
    print(f"The results are in {usr_name}!!!")
    time.sleep(2)
    print("HERE WE GO!")
    time.sleep(1)

    #check the user input to see if it meets the requirements
    # user_name_acceptable = check_user_input(usr_name)
    # print (f"Testing {user_name_acceptable}")

    #Change acceptable user input to lowercase characters to keep numbers consistent
    usr_lower_name = name_to_lower(usr_name)

    #Send lowercase input to get a list of characters to numbers in correlation to the alphabet index
    usr_num_name = characters_to_numbers(usr_lower_name)

    #Add all of the numbers together to get the sum
    usr_sum_name = sum_of_numbers(usr_num_name)
    print(f"Your name sum is: {usr_sum_name}")
    


if __name__ == "__main__":
    main()