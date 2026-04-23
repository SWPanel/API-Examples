from app.http.api_client import ApiClient

class AliasService:
    def __init__(self):
        self.api = ApiClient()

    # ====================
    # GET
    # ====================
    def get_all(self, service, mail):

        if mail:
            data = self.api.get(
                f"/services/{service}/mail/alias/{mail}"
            )
        
        else:
            data = self.api.get(
                f"/services/{service}/mail/alias/"
            )

        if not data:
            return []
        
        return data.get("result", [])


    # ====================
    # POST
    # ====================
    def post_create_new_alias(self, service, body):
        data = self.api.post(
            f"/services/{service}/mail/alias/",
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
    def put_update_alias(self, service, alias, body):
        data = self.api.put(
            f"/services/{service}/mail/alias/{alias}",
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
    def delete_alias(self, service, alias):
        data = self.api.delete(
            f"/services/{service}/mail/alias/{alias}",
        )

        if not data:
            return []
        
        if "Error message" in data:
            return data["Error message"]
        
        if "message" in data:
            return data["message"]
        
        return data