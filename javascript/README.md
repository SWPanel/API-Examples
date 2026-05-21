# SWPanel API JavaScript Client

A minimal JavaScript client for interacting with the SWPanel API.

This project is intentionally simple and lightweight.  
It is designed as a quick start example for developers who want to interact with the API using plain Node.js and native fetch.

For a complete modular implementation with:
- interactive CLI menus
- advanced abstractions
- scalable architecture
- dynamic request builders
- advanced error handling

see the Python client version.

---

## Features

- Minimal setup
- Native fetch API
- Simple API requests
- Lightweight structure
- JSON formatted responses
- Easy to understand
- Quick start examples

---

## Project Structure

```text
├── .env
├── package.json
├── README.md
└── app/
    ├── client.js
    ├── config.js
    └── examples/
        └── services-list.js
```

---

## Requirements

- Node.js 18+

Check your version:

```bash
node -v
```

---

## Installation

Install dependencies:

```bash
npm install
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

Run the example script:

```bash
node app/examples/services-list.js
```

or using npm scripts:

```bash
npm run services:list
```

---

## Example

```js
import { apiRequest } from '../client.js';

await apiRequest('GET', 'services/');
```

---

## Supported Methods

### GET

```js
await apiRequest('GET', 'services/');
```

### POST

```js
await apiRequest('POST', 'services/create/', {
    name: 'Example',
});
```

### PUT

```js
await apiRequest('PUT', 'services/update/', {
    id: 1,
});
```

### DELETE

```js
await apiRequest('DELETE', 'services/delete/', {
    id: 1,
});
```

---

## Response Formatting

Responses are automatically formatted as JSON when possible.

Example:

```json
{
  "success": true,
  "data": []
}
```

If the response is not valid JSON, the raw response body is displayed.

---

## Error Handling

The client displays:
- HTTP status codes
- API responses
- fetch/network errors

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
- a simple Node.js API utility

For advanced usage and architecture reference, see the Python implementation.