import argparse
import json
import os

from commands.fetch_data import fetch_api_data
from commands.generate_markdown import generate_markdown
from utils.process_data import process_data


def main():
    parser = argparse.ArgumentParser(
        description="Generate Markdown documentation from an API response."
    )
    parser.add_argument("api_url", help="URL of the API endpoint.")
    parser.add_argument(
        "--method",
        type=str,
        choices=["GET", "POST", "PATCH", "DELETE"],
        default="GET",
        help="HTTP method",
    )
    parser.add_argument(
        "--headers",
        help="JSON string for custom headers.",
        default=None,
    )
    parser.add_argument(
        "--body", type=str, help="Request body in JSON format (for POST/PATCH)"
    )

    args = parser.parse_args()

    try:
        # Parse headers if provided
        headers = json.loads(args.headers) if args.headers else None
        body = json.loads(args.body) if args.body else None
        method = (
            args.method
            if args.method
            else input("Enter the HTTP method (GET, POST, PATCH, DELETE): ").upper()
        )

        # Ask user for the HTTP method
        if method not in ["GET", "POST", "PATCH", "DELETE"]:
            raise ValueError(
                "Invalid HTTP method. Please choose from GET, POST, PATCH, DELETE."
            )
        type_mapping = {
            "string": str,
            "integer": int,
            "float": float,
            "bool": lambda x: x.lower() == "true" if isinstance(x, str) else bool(x),
        }
        request_fields = None
        if method in ["POST", "PATCH"]:
            try:
                if body:
                    request_fields = get_user_input_for_body(body)
                    if input("Wanna add other fields? (yes/no): ").strip().lower() in [
                        "yes",
                        "y",
                    ]:
                        request_fields += get_request_fields()
                else:
                    request_fields = get_request_fields()
                    body_data = {
                        field["Field"]: type_mapping.get(field["Type"], str)(
                            field["Value"]
                        )
                        for field in request_fields
                    }
                    if isinstance(body_data, str):
                        body = json.loads(body_data)
            except json.JSONDecodeError:
                raise ValueError("Invalid JSON format for request body.")

        # Ask user if they want to append to an existing file
        output_file = "output.md"
        append = False
        if os.path.exists(output_file):
            append = input(
                f"Do you want to append to the existing '{output_file}'? (yes/no): "
            ).lower() in ["yes", "y"]

        # Fetch API data
        api_data = fetch_api_data(args.api_url, method, headers=headers, data=body)
        processed_data = process_data(api_data)

        request_title = input("Title of this Request (get a user): ")

        # Generate Markdown
        generate_markdown(
            args.api_url,
            processed_data,
            output_file,
            method,
            headers,
            append,
            request_title,
            request_data=request_fields,
        )
        print(f"Documentation generated successfully: {output_file}")

    except Exception as e:
        print(f"Error: {e}")


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


if __name__ == "__main__":
    main()
