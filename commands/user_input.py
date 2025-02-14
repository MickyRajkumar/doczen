def get_user_input():
    parameters = []
    while True:
        parameter = {}
        parameter["Parameter"] = input(
            "Enter Parameter name (or type 'done' to finish): "
        )
        if parameter["Parameter"].lower() == "done":
            break
        parameter["Type"] = input("Enter Type (e.g., integer, string): ")
        parameter["Required"] = input("Is it Required? (Yes/No): ")
        parameter["Description"] = input("Enter Description: ")
        parameter["Default"] = input("Enter Default value (or '-' if none): ")
        parameters.append(parameter)
        print("Parameter added!\n")
    return parameters
