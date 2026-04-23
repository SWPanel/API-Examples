from app.http.api_client import ApiClient

class DatabaseService:
    def __init__(self):
        self.api = ApiClient()

    # ====================
    # GET
    # ====================
    def get_all(self, service, db_name):
        if db_name:
            data = self.api.get(
                f"/services/{service}/db/{db_name}"
            )

        else:
            data = self.api.get(
                f"/services/{service}/db/"
            )

        if not data:
            return []
        
        return data.get("result", [])


    # ====================
    # POST
    # ====================
    def post_create_new_db(self, service, body):
        data = self.api.post(
            f"/services/{service}/db/",
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
    def put_update_db(self, service, db_name, body):
        data = self.api.put(
            f"/services/{service}/db/{db_name}",
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
    def delete_db(self, service, db_name):
        data = self.api.delete(
            f"/services/{service}/db/{db_name}",
        )

        if not data:
            return []
        
        if "Error message" in data:
            return data["Error message"]
        
        if "message" in data:
            return data["message"]
        
        return data