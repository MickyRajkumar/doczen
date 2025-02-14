def process_data(data):
    if isinstance(data, list):
        return [data[0]] if data else []
    elif isinstance(data, dict):
        return {key: process_data(value) for key, value in data.items()}
    else:
        return data
