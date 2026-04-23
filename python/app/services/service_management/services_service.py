from app.http.api_client import ApiClient

class ServicesService:
    def __init__(self):
        self.api = ApiClient()

    # ====================
    # GET
    # ====================
    def get_all(self, params):

        if params:
            data = self.api.get(
                f"/services/",
                params=params
            )
        
        else:
            data = self.api.get(
                "/services/"
            )

        if not data:
            return []
        
        return data.get("result", [])
    
    def get_check_status(self, service):
        data = self.api.get(
            f"/services/{service}/status/"
        )

        if not data:
            return []
        
        return data


    # ====================
    # POST
    # ====================
    def post_create_new_service(self, body):
        data = self.api.post(
            f"/services/create/",
            data=body
        )

        if not data:
            return []
        
        if "Error message" in data:
            return data["Error message"]
        
        return data
