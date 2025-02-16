# API Endpoint

`https://jsonplaceholder.typicode.com/posts/`

## GET

Retrieves the data.

## Headers

| Header | Value |
|--------|-------|
| **Authorization** | `Bearer token` |

## Response Data

```json

[
  {
    "userId": 1,
    "id": 1,
    "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",
    "body": "quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto"
  }
]

```

---

# API Endpoint

`https://jsonplaceholder.typicode.com/posts/`

## POST

Creates a new resource.

## Headers

| Header | Value |
|--------|-------|
| **Authorization** | `Bearer token` |

## Response Data

```json

{
  "id": 101
}

```

## Fields

| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| userid | integer | Yes | foriegn key |
| title | string | Yes | title of post |
| body | string | No | body of article |

---

# API Endpoint

`https://jsonplaceholder.typicode.com/posts/1`

## PATCH

Updates an existing resource partially.

## Headers

| Header | Value |
|--------|-------|
| **Authorization** | `Bearer token` |

## Response Data

```json

{
  "userId": 1,
  "id": 1,
  "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",
  "body": "quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto"
}

```

## Fields

| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| body | string | Yes | body of article |
