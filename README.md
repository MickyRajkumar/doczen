# API Documentation Generator

![Python](https://img.shields.io/badge/Python-3.7%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Contributions Welcome](https://img.shields.io/badge/Contributions-Welcome-brightgreen)

A Python-based tool to generate Markdown documentation for API endpoints. It supports `GET`, `POST`, `PATCH`, and `DELETE` methods, and dynamically collects API details such as headers, query parameters, request fields, and response data to create a well-structured `output.md` file.

---

## Features

- **Supports Multiple HTTP Methods**: `GET`, `POST`, `PATCH`, and `DELETE`.
- **Interactive Input**: Collects request fields, query parameters, and headers interactively.
- **Markdown Output**: Generates a clean and structured `output.md` file.
- **Append Mode**: Option to append documentation to an existing `output.md` file.
- **Custom Headers**: Allows specifying custom headers for API requests.

---

## example 

Check the `output.md` file in the root directory for an example of the generated output

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/MickyRajkumar/doczen.git 
cd doczen
```

### 2. Install Dependencies

This project requires Python 3.7+ and the `requests` library. Install it using:

```bash
pip3 install requests
```

---

## Usage

### Basic Usage

Run the script with the API endpoint URL:

```bash
python3 main.py https://api.example.com/data
```

### Custom Headers

Provide custom headers as a JSON string using the `--headers` argument:

```bash
python3 main.py https://api.example.com/data --headers '{"Authorization": "Bearer token"}'
```

### Example Workflow

1. Run the script:

   ```bash
   python main.py https://api.example.com/data
   ```

2. Choose the HTTP method (`GET`, `POST`, `PATCH`, or `DELETE`).
3. For `POST` and `PATCH`, provide request fields (name, type, required, description).
4. For `GET` and `DELETE`, provide query parameters (if applicable).
5. Optionally append to an existing `output.md` file.
6. The script generates a Markdown file (`output.md`) with the API documentation.

---

## Example Output

### For `POST` Method

```markdown
# API Endpoint
`https://api.example.com/data`

## POST
Creates a new resource.

## Request Fields
| Field | Type    | Required | Description           |
|-------|---------|----------|-----------------------|
| name  | string  | Yes      | The name of the user. |
| age   | integer | No       | The age of the user.  |

## Response Data
```json
{
  "id": 1,
  "name": "John Doe",
  "age": 30
}
```

## Fields
- `id`: int
- `name`: str
- `age`: int
```


## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

### Steps to Contribute

1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add your message here"
   ```
4. Push to the branch:
   ```bash
   git push origin feature/your-feature-name
   ```
5. Open a pull request.

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## Author

- **Micky Rajkumar**  
  Email: [pathourajkumar@gmail.com](mailto:pathourajkumar@gmail.com)

---
