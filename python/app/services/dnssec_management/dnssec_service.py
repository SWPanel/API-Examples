from app.http.api_client import ApiClient

class DNSSECService:
    def __init__(self):
        self.api = ApiClient()

    # ====================
    # GET
    # ====================
    def get_all(self, service):

        data = self.api.get(
            f"/services/{service}/dnssec/"
        )

        if not data:
            return []
        
        return data.get("result", [])


    # ====================
    # POST
    # ====================
    def post_create_new_dnssec_record(self, service, body):
        data = self.api.post(
            f"/services/{service}/dnssec/",
            data=body
        )

        if not data:
            return []
        
        if "Error message" in data:
            return data["Error message"]
        
        if "message" in data:
            return data["message"]
        
        return data
    

    # ====================
    # PUT
    # ====================
    def put_update_dnssec_record(self, service, body):
        data = self.api.put(
            f"/services/{service}/dnssec/",
            data=body
        )

        if not data:
            return []
        
        if "Error message" in data:
            return data["Error message"]
        
        if "message" in data:
            return data["message"]
        
        return data
    

    # ====================
    # DELETE
    # ====================
    def delete_dnssec_record(self, service, body):
        data = self.api.delete(
            f"/services/{service}/dnssec/",
            data=body
        )

        if not data:
            return []
        
        if "Error message" in data:
            return data["Error message"]
        
        if "message" in data:
            return data["message"]
        
        return data