import requests


def fetch_api_data(api_url, method="GET", data=None, headers=None):
    """Fetch data from the API endpoint."""
    print(f"requested data {data}")
    try:
        if method.upper() == "GET":
            response = requests.get(api_url, headers=headers)
        elif method.upper() == "POST":
            response = requests.post(api_url, json=data, headers=headers)
        elif method.upper() == "PATCH":
            response = requests.patch(api_url, json=data, headers=headers)
        elif method.upper() == "DELETE":
            response = requests.delete(api_url, headers=headers)
        else:
            raise ValueError(f"Unsupported HTTP method: {method}")

        response.raise_for_status()  # Raise an error for bad status codes
        return response.json()  # Parse JSON response
    except requests.exceptions.RequestException as e:
        raise Exception(f"Failed to fetch data from API: {e}")
