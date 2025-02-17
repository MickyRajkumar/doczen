def get_request_fields():
    """Get request fields from the user."""
    fields = []
    while True:
        field = {}
        field["Field"] = input("Enter field name (or type 'done' to finish): ")
        if field["Field"].lower() == "done":
            break
        field["Value"] = input("Enter field value: ")
        field["Type"] = input("Enter field type (e.g., string, integer): ")
        field["Required"] = input("Is this field required? (yes/no): ").lower() in [
            "yes",
            "y",
        ]
        field["Description"] = input("Enter field description: ")
        fields.append(field)
        print("Field added!\n")
    return fields
