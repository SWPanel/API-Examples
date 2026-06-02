from app.http.api_client import ApiClient

class SSLService:
    def __init__(self):
        self.api = ApiClient()

    # ====================
    # GET
    # ====================
    def get_ssl(self, ssl_id):

        if ssl_id:
            data = self.api.get(
                f"/ssl/{ssl_id}/"
            )
        
        else:
            data = self.api.get(
                f"/ssl/"
            )

        if not data:
            return []
        
        return data.get("result", [])

    def get_pfx(self, ssl_id):

        data = self.api.get(
            f"/ssl/{ssl_id}/pfx/"
        )

        if not data:
            return []
        
        return data.get("result", [])
    
    def get_tokens_dns(self, ssl_id):

        data = self.api.get(
            f"/ssl/{ssl_id}/tokens/"
        )

        if not data:
            return []
        
        return data.get("result", [])
    

    # ====================
    # POST
    # ====================
    def post_create_ssl(self, body):
        data = self.api.post(
            f"/domains/contact/",
            data=body
        )

        if not data:
            return []
        
        if "Error message" in data:
            return data["Error message"]
        
        if "message" in data:
            return data["message"]
        
        return data
    
    def post_reissue_ssl(self, ssl_id):
        data = self.api.post(
            f"/ssl/{ssl_id}/reissue/"
        )

        if not data:
            return []
        
        if "Error message" in data:
            return data["Error message"]
        
        if "message" in data:
            return data["message"]
        
        return data
    
    def post_renew_ssl(self, ssl_id):
        data = self.api.post(
            f"/ssl/{ssl_id}/renew/"
        )

        if not data:
            return []
        
        if "Error message" in data:
            return data["Error message"]
        
        if "message" in data:
            return data["message"]
        
        return data
