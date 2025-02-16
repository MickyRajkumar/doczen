import json

from commands.user_input import get_user_input


def generate_markdown(
    api_url,
    api_data,
    output_file,
    method,
    headers=None,
    append=False,
    request_data=None,
):
    """Generate Markdown documentation from the API response."""
    markdown = []

    # If appending to an existing file, add a separator
    if append:
        markdown.append("\n---\n")

    # API Endpoint
    markdown.append("# API Endpoint\n")
    markdown.append(f"`{api_url}`\n")

    # Method Documentation
    markdown.append(f"## {method.upper()}\n")
    if method.upper() == "GET":
        markdown.append("Retrieves the data.\n")
    elif method.upper() == "POST":
        markdown.append("Creates a new resource.\n")
    elif method.upper() == "PATCH":
        markdown.append("Updates an existing resource partially.\n")
    elif method.upper() == "DELETE":
        markdown.append("Deletes a resource.\n")

    # Headers (if provided)
    if headers:
        markdown.append("## Headers\n")
        markdown.append(generate_headers_table(headers))

    # Response Data
    markdown.append("## Response Data\n")
    markdown.append("```json\n")
    markdown.append(json.dumps(api_data, indent=2))
    markdown.append("\n```\n")

    # Fields and Descriptions (if available)
    # if isinstance(api_data, dict):
    #     markdown.append("## Fields\n")
    #     for key, value in api_data.items():
    #         markdown.append(f"- **{key}**: `{type(value).__name__}`\n")
    #         if isinstance(value, dict):
    #             for sub_key, sub_value in value.items():
    #                 markdown.append(
    #                     f"  - **{sub_key}**: `{type(sub_value).__name__}`\n"
    #                 )

    # Query Parameters (if applicable)
    if method.upper() in ["GET", "DELETE"]:
        have_query = input(
            f"Does {method.upper()} have any query parameters? (yes/no): "
        )
        if have_query.lower() in ["yes", "y"]:
            headers = ["Parameter", "Type", "Required", "Description", "Default"]
            print(
                "Enter the details for each query parameter. Type 'done' when finished.\n"
            )
            parameters = get_user_input()
            if parameters:
                markdown_table = generate_markdown_table(parameters, headers)
                markdown.append("## Query Parameters\n")
                markdown.append(markdown_table)

    # Request Body (if applicable)
    if request_data and method in ["POST", "PATCH"]:
        markdown.append("## Fields\n")
        markdown.append(generate_request_fields_table(request_data))

    # Write to output file
    mode = "a" if append else "w"
    with open(output_file, mode) as file:
        file.write("\n".join(markdown))


def generate_headers_table(headers):
    """Generate a Markdown table for headers."""
    table = "| Header | Value |\n"
    table += "|--------|-------|\n"
    for key, value in headers.items():
        masked_value = (
            "`your token`" if "authorization" in key.lower() else f"`{value}`"
        )
        table += f"| **{key}** | {masked_value} |\n"
    return table


def generate_markdown_table(parameters, headers):
    """Generate a Markdown table for query parameters."""
    markdown_table = "| " + " | ".join(headers) + " |\n"
    markdown_table += (
        "| " + " | ".join([":---", ":---:", ":---:", ":---", ":---"]) + " |\n"
    )
    for param in parameters:
        row = "| " + " | ".join([param[header] for header in headers]) + " |"
        markdown_table += row + "\n"
    return markdown_table


def generate_request_fields_table(fields):
    """Generate a Markdown table for request fields."""
    headers = ["Field", "Type", "Required", "Description"]
    table = "| " + " | ".join(headers) + " |\n"
    table += "| " + " | ".join([":---", ":---", ":---:", ":---"]) + " |\n"
    for field in fields:
        row = (
            "| "
            + " | ".join(
                [
                    field["Field"],
                    field["Type"],
                    "Yes" if field["Required"] else "No",
                    field["Description"],
                ]
            )
            + " |"
        )
        table += row + "\n"
    return table
