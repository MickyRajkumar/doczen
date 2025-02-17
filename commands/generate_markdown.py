import json


def generate_markdown(
    api_url,
    api_data,
    output_file,
    method,
    headers=None,
    append=False,
    request_title=None,
    request_data=None,
):
    """Generate Markdown documentation from the API response."""
    markdown = []

    if append:
        markdown.append("\n---\n")

    markdown.append("# API Endpoint\n")
    markdown.append(f"`{api_url}`\n")

    markdown.append(f"## {method.upper()}\n")
    markdown.append(f"### {request_title}\n")

    if headers:
        markdown.append("## Headers\n")
        markdown.append(generate_headers_table(headers))

    markdown.append("## Response Data\n")
    markdown.append("```json\n")
    markdown.append(json.dumps(api_data, indent=2))
    markdown.append("\n```\n")

    if request_data and method in ["POST", "PATCH"]:
        markdown.append("## Fields\n")
        markdown.append(generate_request_fields_table(request_data))

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
