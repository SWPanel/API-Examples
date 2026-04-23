from app.http.api_client import ApiClient

class FTPService:
    def __init__(self):
        self.api = ApiClient()

    # ====================
    # GET
    # ====================
    def get_ftp(self, service, ftp_account):

        if ftp_account:
            data = self.api.get(
                f"/services/{service}/ftp/{ftp_account}"
            )
        
        else:
            data = self.api.get(
                f"/services/{service}/ftp/"
            )

        if not data:
            return []
        
        return data.get("result", [])


    # ====================
    # POST
    # ====================
    def post_create_new_account(self, service, body):
        data = self.api.post(
            f"/services/{service}/ftp/",
            data=body
        )

        if not data:
            return []
        
        if "Error message" in data:
            return data["Error message"]
        
        if "message" in data:
            return data["message"]
        
        return data
    
    def post_stop_account(self, service, ftp_account):
        data = self.api.post(
            f"/services/{service}/ftp/stop/{ftp_account}",
        )

        if not data:
            return []
        
        if "Error message" in data:
            return data["Error message"]
        
        if "message" in data:
            return data["message"]
        
        return data
    
    def post_start_account(self, service, ftp_account):
        data = self.api.post(
            f"/services/{service}/ftp/start/{ftp_account}",
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
    def put_update_account(self, service, ftp_account, body):
        data = self.api.put(
            f"/services/{service}/ftp/{ftp_account}",
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
    def delete_account(self, service, ftp_account):
        data = self.api.delete(
            f"/services/{service}/ftp/{ftp_account}",
        )

        if not data:
            return []
        
        if "Error message" in data:
            return data["Error message"]
        
        if "message" in data:
            return data["message"]
        
        return data