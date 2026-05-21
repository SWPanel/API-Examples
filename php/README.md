# SWPanel API PHP Client

A minimal PHP client for interacting with the SWPanel API.

This project is intentionally simple and dependency-free.  
It is designed as a lightweight reference implementation and quick start example for developers who want to interact with the API using plain PHP.

For a complete modular implementation with:
- interactive CLI menus
- service abstraction
- dynamic request builders
- advanced error handling
- scalable architecture

see the Python client version.

---

## Features

- No dependencies
- No Composer required
- Plain PHP + cURL
- Simple API requests
- Minimal and easy to understand
- Quick start examples

---

## Project Structure

```text
├── .env
└── app/
    ├── client.php
    ├── config.php
    └── examples/
        └── services-list.php
```

---

## Requirements

- PHP 8+
- PHP cURL extension enabled

Check if cURL is enabled:

```bash
php -m
```

You should see:

```text
curl
```

---

## Configuration

Create a `.env` file inside the `php/` directory:

```env
BASE_URL=https://api.swpanel.com/v2026
API_TOKEN=your_token_here
```

---

## Usage

Run the example file directly with PHP:

```bash
php app/examples/services-list.php
```

---

## Example

```php
require_once __DIR__ . '/../client.php';

$client = new Client();

$response = $client->get('/services/XX012');

print_r($response);
```

---

## Supported Methods

### GET

```php
$client->get('/services/');
```

### POST

```php
$client->post('/services/create/', [
    'name' => 'Example',
]);
```

### PUT

```php
$client->put('/services/update/', [
    'id' => 1,
]);
```

### DELETE

```php
$client->delete('/services/delete/', [
    'id' => 1,
]);
```

---

## Error Handling

Errors are returned as arrays.

Example API error:

```php
[
    'Error code' => '#APIGENE25',
    'Error message' => 'No existen resultados'
]
```

Example cURL error:

```php
[
    'error' => 'Connection timed out'
]
```

---

## Philosophy

This project is not intended to be a full SDK.

The goal is to provide:
- a minimal implementation
- quick API interaction examples
- a lightweight starting point

For advanced usage and architecture reference, see the Python implementation.