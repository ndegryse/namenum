def check_user_input(user_name):
    boolean = True
    print("Testing if we made it here 1")
    if " " in user_name:
        print("Please do not include spaces in input.")
        boolean = False
    for char in user_name:
        if char.isdigit():
            print("Please do not include numbers in input.")
        boolean = False
    print("testing if we made it here 2")
    return boolean
