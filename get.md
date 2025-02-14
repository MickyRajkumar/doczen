# API Endpoint

`https://dogapi.dog/api/v2/facts`

## GET

Retrieves the data.

## Response Data

```json

{
  "data": [
    {
      "id": "2af0f6b4-5078-4c72-8b20-a6be363d7820",
      "type": "fact",
      "attributes": {
        "body": "The phrase \"raining cats and dogs\" originated in 17th century England when it is believed that many cats and dogs drowned during heavy periods of rain."
      }
    }
  ]
}

```

## Fields

- **data**: `list`

## Query Parameters

| Parameter | Type | Required | Description | Default |
| :--- | :---: | :---: | :--- | :--- |
| title | string | no | this is docs  | - |
