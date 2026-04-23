# SWPanel API Python Client  
  
A structured Python CLI client for interacting with the SWPanel API.  
  
This project provides a modular and scalable way to manage services such as:  
- Hosting  
- Cloud  
- DNS  
- Mail  
- Databases  
- FTP  
  
It is designed for both learning and real-world usage, with a clean separation between:  
- Input (CLI)  
- Business logic (Services)  
- API communication (ApiClient)  
 
---  
  
## Features  
  
- Interactive CLI menus  
- Modular architecture (services, UI, core)  
- Dynamic request building (only sends required fields)  
- Error handling with API response support  
- Support for multiple service types (Cloud, Hosting, Mail, etc.)  
- Easy to extend  
  
---  
  
## Project Structure  

app/  
├── core/  
│ ├── input.py # User input helpers (ask_int, ask_bool, etc.)  
│ ├── menus/ # CLI menus  
│ └── app.py # Main application flow  
│  
├── services/ # Business logic (API wrappers)  
│ ├── service_service.py  
│ ├── mail_service.py  
│ ├── dns_service.py  
│ └── ...  
│  
├── http/  
│ └── api_client.py # HTTP client (GET, POST, PUT, DELETE)  
│  
├── ui/ # UI layer (formatting, output)  
│ └── ...  
│  
└── helpers/ # Utility functions

  
---  
  
## Installation  
  
### 1. Create virtual environment  
  
**Linux / Mac**
```bash  
python3 -m venv venv  
source venv/bin/activate
```

**Windows**

```bash
python -m venv venv  
venv\Scripts\activate
```

---

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

---

## Configuration

Create a `.env` file in the root directory using .env.example as prototype:

```env
BASE_URL=https://api.swpanel.com/v2026  
API_TOKEN=your_token_here
```

Make sure your `ApiClient` loads these values correctly.

---

##  Usage

Run the CLI:

```bash
python main.py
```

You will see an interactive menu:

```bash
=== Menu ===  
1. Service Management  
2. Mail Management  
...  
0. Exit
```

Navigate through menus to:

- List services
    
- Create resources
    
- Update configurations
    
- Manage DNS, mail, databases, etc.
    
---

## How It Works

### Flow

User Input → UI → Service → ApiClient → API

### Example

```python
response = MailService().get_all(service_id)
```

- `UI` handles input/output
    
- `Service` builds logic
    
- `ApiClient` makes HTTP request
    

---

## Request Handling

### GET

```python
self.api.get("/services/", params={})
```

### POST

```python
self.api.post("/services/create/", data=body)
``` 

### PUT

```python
self.api.put("/services/update/", data=body)
```

---

## Error Handling

The client is designed to handle API errors gracefully.

Example API error:

```json
{  
  "Error code": "#APIGENE25",  
  "Error message": "No existen resultados"  
}
```

Handled as:

```python
if "Error message" in response:  
    print(response["Error message"])
```

---

## Dynamic Payloads

The client only sends fields that the user provides.

Example:

```python
body = {}  
  
if password:  
    body["password"] = password  
  
if additional:  
    body["additional"] = additional
```

This avoids sending empty or invalid data.