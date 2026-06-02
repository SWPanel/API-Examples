from app.http.api_client import ApiClient

class CronsService:
    def __init__(self):
        self.api = ApiClient()

    # ====================
    # GET
    # ====================
    def get_all(self, service, cron_id):
        if cron_id:
            data = self.api.get(
                f"/services/{service}/cron/{cron_id}"
            )

        else:
            data = self.api.get(
                f"/services/{service}/cron/"
            )

        if not data:
            return []
        
        return data.get("result", [])
    
    def get_cron_users(self, service):
        data = self.api.get(
            f"/services/{service}/cron/users/"
        )

        if not data:
            return []
        
        return data.get("result", [])


    # ====================
    # POST
    # ====================
    def post_create_new_cron(self, service, body):
        data = self.api.post(
            f"/services/{service}/cron/",
            data=body
        )

        if not data:
            return []
        
        if "Error message" in data:
            return data["Error message"]
        
        if "message" in data:
            return data["message"]
        
        return data
    
    def post_start_cron(self, service, cron_id):
        data = self.api.post(
            f"/services/{service}/cron/start/{cron_id}",
        )

        if not data:
            return []
        
        if "Error message" in data:
            return data["Error message"]
        
        if "message" in data:
            return data["message"]
        
        return data
    
    def post_stop_cron(self, service, cron_id):
        data = self.api.post(
            f"/services/{service}/cron/stop/{cron_id}",
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
    def put_update_cron(self, service, cron_id, body):
        data = self.api.put(
            f"/services/{service}/cron/{cron_id}",
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
    def delete_cron(self, service, cron_id):
        data = self.api.delete(
            f"/services/{service}/cron/{cron_id}",
        )

        if not data:
            return []
        
        if "Error message" in data:
            return data["Error message"]
        
        if "message" in data:
            return data["message"]
        
        return data