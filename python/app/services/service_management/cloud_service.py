from app.http.api_client import ApiClient

class CloudService:
    def __init__(self):
        self.api = ApiClient()

    
    # ====================
    # POST
    # ====================
    def post_start_cloud(self, service):
        data = self.api.post(
            f"/services/{service}/cloud/start/",
        )

        if not data:
            return []
        
        if "Error message" in data:
            return data["Error message"]
        
        if "message" in data:
            return data["message"]
        
        return data

    def post_stop_cloud(self, service):
        data = self.api.post(
            f"/services/{service}/cloud/stop/",
        )

        if not data:
            return []
        
        if "Error message" in data:
            return data["Error message"]
        
        if "message" in data:
            return data["message"]
        
        return data
    
    def post_park_cloud(self, service):
        data = self.api.post(
            f"/services/{service}/cloud/park/",
        )

        if not data:
            return []
        
        if "Error message" in data:
            return data["Error message"]
        
        if "message" in data:
            return data["message"]
        
        return data
    
    def post_unkpark_cloud(self, service):
        data = self.api.post(
            f"/services/{service}/cloud/unpark/",
        )

        if not data:
            return []
        
        if "Error message" in data:
            return data["Error message"]
        
        if "message" in data:
            return data["message"]
        
        return data
    
    def post_clone_cloud(self, service):
        data = self.api.post(
            f"/services/{service}/cloud/clone/",
        )

        if not data:
            return []
        
        if "Error message" in data:
            return data["Error message"]
        
        if "message" in data:
            return data["message"]
        
        return data
    
    def post_white_clone_cloud(self, service):
        data = self.api.post(
            f"/services/{service}/cloud/clone/white/",
        )

        if not data:
            return []
        
        if "Error message" in data:
            return data["Error message"]
        
        if "message" in data:
            return data["message"]
        
        return data