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
        "--headers",
        help="JSON string for custom headers.",
        default=None,
    )
    args = parser.parse_args()

    try:
        # Parse headers if provided
        headers = json.loads(args.headers) if args.headers else None

        # Ask user for the HTTP method
        method = input("Enter the HTTP method (GET, POST, PATCH, DELETE): ").upper()
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
        request_data = None
        request_fields = None
        if method in ["POST", "PATCH"]:
            try:
                request_fields = get_request_fields()
                body_data = {
                    field["Field"]: type_mapping.get(field["Type"], str)(field["Value"])
                    for field in request_fields
                }
                if isinstance(body_data, str):
                    request_data = json.loads(body_data)
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
        api_data = fetch_api_data(
            args.api_url, method, headers=headers, data=request_data
        )
        processed_data = process_data(api_data)

        # Generate Markdown
        generate_markdown(
            args.api_url,
            processed_data,
            output_file,
            method,
            headers,
            append,
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


if __name__ == "__main__":
    main()
