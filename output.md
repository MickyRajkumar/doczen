# API Endpoint

`https://dogapi.dog/api/v2/facts`

## GET

Retrieves the data.

## Headers

| Header | Value |
|--------|-------|
| **Authorization** | `Bearer token` |

## Response Data

```json

{
  "data": [
    {
      "id": "87a86bc0-9dbb-4069-81db-e595e4b1f156",
      "type": "fact",
      "attributes": {
        "body": "A lost Dachshund was found swallowed whole in the stomach of a giant catfish in Berlin on July 2003."
      }
    }
  ]
}

```

## Fields

- **data**: `list`

---

# API Endpoint

`https://dogapi.dog/api/v2/facts`

## GET

Retrieves the data.

## Headers

| Header | Value |
|--------|-------|
| **Authorization** | `Bearer token` |

## Response Data

```json

{
  "data": [
    {
      "id": "52daa494-7fd4-4a44-95c1-128afbfa0ab8",
      "type": "fact",
      "attributes": {
        "body": "The fastest breed, the Greyhound, can run up to 44 miles per hour."
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
| name | string | no | test | - |
