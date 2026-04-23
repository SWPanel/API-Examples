from app.http.api_client import ApiClient

class DatabaseUserService:
    def __init__(self):
        self.api = ApiClient()

    # ====================
    # GET
    # ====================
    def get_all(self, service, user):
        if user:
            data = self.api.get(
                f"/services/{service}/db/user/{user}"
            )

        else:
            data = self.api.get(
                f"/services/{service}/db/user/"
            )

        if not data:
            return []
        
        return data.get("result", [])


    # ====================
    # POST
    # ====================
    def post_create_new_user(self, service, body):
        data = self.api.post(
            f"/services/{service}/db/user/",
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
    def put_update_user(self, service, body):
        data = self.api.put(
            f"/services/{service}/db/user/",
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
    def delete_user(self, service, user):
        data = self.api.delete(
            f"/services/{service}/db/user/",
            data={"user": user}
        )

        if not data:
            return []
        
        if "Error message" in data:
            return data["Error message"]
        
        if "message" in data:
            return data["message"]
        
        return data