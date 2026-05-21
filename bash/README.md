# SWPanel API Bash Client

A minimal Bash client for interacting with the SWPanel API.

This project is intentionally simple and dependency-free.  
It is designed as a lightweight reference implementation and quick start example for developers who want to interact with the API using plain Bash and cURL.

For a complete modular implementation with:
- interactive CLI menus
- dynamic request builders
- advanced abstractions
- scalable architecture
- complex workflows

see the Python client version.

---

## Features

- No dependencies
- No frameworks
- Plain Bash + cURL
- Optional JSON formatting with jq
- Simple API requests
- Minimal and easy to understand
- Quick start examples

---

## Project Structure

```text
├── .env
├── README.md
└── app/
    ├── client.sh
    ├── config.sh
    ├── helpers.sh
    └── examples/
        └── services-list.sh
```

---

## Requirements

- Bash
- cURL

Optional:

- jq (for JSON formatting)

---

## Installation

### Ubuntu / Debian

Install cURL:

```bash
sudo apt install curl
```

Optional jq installation:

```bash
sudo apt install jq
```

---

## Configuration

Create a `.env` file in the project root:

```env
BASE_URL=https://api.swpanel.com/v2026
API_TOKEN=your_token_here
```

---

## Usage

Run the example file directly:

```bash
bash app/examples/services-list.sh
```

---

## Example

```bash
#!/usr/bin/env bash

source "$(dirname "$0")/../client.sh"

api_request "GET" "/services/XX012"
```

---

## Supported Methods

### GET

```bash
api_request "GET" "/services/"
```

### POST

```bash
api_request "POST" "/services/create/" '{
  "name": "Example"
}'
```

### PUT

```bash
api_request "PUT" "/services/update/" '{
  "id": 1
}'
```

### DELETE

```bash
api_request "DELETE" "/services/delete/" '{
  "id": 1
}'
```

---

## JSON Formatting

If `jq` is installed, responses are automatically formatted.

Example:

```json
{
  "success": true,
  "data": []
}
```

Without jq, raw JSON is returned.

---

## Error Handling

The client displays:
- HTTP status codes
- API responses
- cURL errors

Example:

```text
HTTP STATUS: 401
Unauthorized
```

Example API error:

```json
{
  "Error code": "#APIGENE25",
  "Error message": "No existen resultados"
}
```

---

## Philosophy

This project is not intended to be a full SDK.

The goal is to provide:
- a minimal implementation
- quick API interaction examples
- a lightweight starting point
- simple Bash automation utilities

For advanced usage and architecture reference, see the Python implementation.