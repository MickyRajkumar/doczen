def get_user_input_for_body(data):
    """Ask the user for type, required flag, and description for each field in the JSON body."""
    fields = []
    print("Define all the posible fields types, required, description: \n")

    for key, value in data.items():
        print(f"Field: {key}")

        # Ask user for field type (default to Python-detected type)
        detected_type = type(value).__name__
        field_type = input(f"Enter type [{detected_type}]: ") or detected_type

        # Ask if the field is required (default: Yes if value is not None)
        required_default = "Yes" if value is not None else "No"
        required = (
            input(f"  Is this field required? (Yes/No) [{required_default}]: ")
            or required_default
        )

        # Ask for description
        description = input("  Enter description: ") or "N/A"

        fields.append(
            {
                "Field Name": key,
                "Type": field_type,
                "Required": required,
                "Description": description,
            }
        )

    return fields
