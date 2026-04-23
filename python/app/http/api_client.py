import requests
from dotenv import load_dotenv
import os

load_dotenv()

class ApiClient:
    BASE_URL = os.getenv('BASE_URL')
    TOKEN    = os.getenv('API_TOKEN')

    def get_headers(self):
        return {
            "Authorization": f"Bearer {self.TOKEN}",
            "Content-Type": "application/json"
        }

    def get(self, endpoint: str, params=None):
        try:
            response = requests.get(
                self.BASE_URL + endpoint,
                headers=self.get_headers(),
                params=params,
            )

            try:
                data = response.json()
            except ValueError:
                print("Invalid JSON response")
                return None

            if response.status_code >= 400:
                return data

            return data

        except requests.exceptions.Timeout:
            print("API Timeout")
        except requests.exceptions.ConnectionError:
            print("Connection Error")
        except Exception as e:
            print(f"Unexpected Error: {e}")

        return None
    
    def post(self, endpoint: str, data: dict = None):
        if data is None:
            data = {}

        try:
            response = requests.post(
                self.BASE_URL + endpoint, 
                json=data,
                headers=self.get_headers()
            )

            if not response.text.strip():
                return {"success": True}

            try:
                result = response.json()
            except ValueError:
                print("Response is not JSON:")
                print(response.text)
                return None

            if response.status_code >= 400:
                return result

            return result

        except requests.exceptions.Timeout:
            print("API Timeout")
        except requests.exceptions.ConnectionError:
            print("Connection Error")
        except Exception as e:
            print(f"Unexpected Error: {e}")

        return None
    
    def put(self, endpoint: str, data: dict):
        try:
            response = requests.put(
                self.BASE_URL + endpoint, 
                json=data,
                headers=self.get_headers()
            )

            try:
                data = response.json()
            except ValueError:
                print("Invalid JSON response")
                return None

            if response.status_code >= 400:
                return data

            return data
        
        except requests.exceptions.Timeout:
            print("API Timeout")
        except requests.exceptions.ConnectionError:
            print("Connection Error")
        except requests.exceptions.HTTPError as e:
            print(f"HTTP Error: {e}")
        except Exception as e:
            print(f"Unexpected Error: {e}")
        return None
    
    def delete(self, endpoint: str, data: dict = None):
        if data is None:
            data = {}
            
        try:
            response = requests.delete(
                self.BASE_URL + endpoint, 
                json=data,
                headers=self.get_headers()
            )

            try:
                data = response.json()
            except ValueError:
                print("Invalid JSON response")
                return None

            if response.status_code >= 400:
                return data

            return data
        
        except requests.exceptions.Timeout:
            print("API Timeout")
        except requests.exceptions.ConnectionError:
            print("Connection Error")
        except requests.exceptions.HTTPError as e:
            print(f"HTTP Error: {e}")
        except Exception as e:
            print(f"Unexpected Error: {e}")
        return None