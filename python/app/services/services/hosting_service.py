from app.http.api_client import ApiClient

class HostingService:
    def __init__(self):
        self.api = ApiClient()

    
    # ====================
    # POST
    # ====================
    def post_start_hosting(self, service):
        data = self.api.post(
            f"/services/{service}/hosting/start/",
        )

        if not data:
            return []
        
        if "Error message" in data:
            return data["Error message"]
        
        if "message" in data:
            return data["message"]
        
        return data

    def post_stop_hosting(self, service):
        data = self.api.post(
            f"/services/{service}/hosting/stop/",
        )

        if not data:
            return []
        
        if "Error message" in data:
            return data["Error message"]
        
        if "message" in data:
            return data["message"]
        
        return data
