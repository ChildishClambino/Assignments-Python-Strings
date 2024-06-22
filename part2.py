def user_input_data_processor():
    firstName = input("pls enter your first name, input must be at least 2 chracters long: ")
    lastName = input("pls enter your last name, input must be at least 2 characters long: ")
    if len(firstName) < 2:
        print("error fisrt name must be at least 2 characters long")
    else:
        print("Hello ", firstName)
    if len(lastName) < 2:
        print("error last name must be at least 2 characters long")
    else:
        print("hello ", lastName)
user_input_data_processor()
