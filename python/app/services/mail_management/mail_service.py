from app.http.api_client import ApiClient

class MailService:
    def __init__(self):
        self.api = ApiClient()


    # ====================
    # GET
    # ====================
    def get_all(self, service, mail: None):
        if mail:
            data = self.api.get(
                f"/services/{service}/mail/mailbox/{mail}/"
            )
        else:
            data = self.api.get(
                f"/services/{service}/mail/mailbox/"
            )

        if "Error message" in data:
            return data["Error message"]
        
        if "message" in data:
            return data["message"]
        
        return data
    
    def get_used_space(self, service, mail):
        data = self.api.get(
            f"/services/{service}/mail/mailbox/size/{mail}"
        )

        if "Error message" in data:
            return data["Error message"]
        
        if "message" in data:
            return data["message"]
        
        return data
    
    def get_login_swpanel_info(self, service, mail):
        data = self.api.get(
            f"/services/{service}/mail/mailbox/login_swpanel/{mail}"
        )

        if "Error message" in data:
            return data["Error message"]
        
        if "message" in data:
            return data["message"]
        
        return data


    # ====================
    # POST
    # ====================
    def post_create_new_email(self, service, body):
        data = self.api.post(
            f"/services/{service}/mail/mailbox/",
            data=body
        )

        if not data:
            return []
        
        if "Error message" in data:
            return data["Error message"]
        
        if "message" in data:
            return data["message"]
        
        return data
    
    def post_update_login_swpanel_info(self, service, mail, body):
        data = self.api.post(
            f"/services/{service}/mail/mailbox/login_swpanel/{mail}",
            data=body
        )

        if not data:
            return []
        
        if "Error message" in data:
            return data["Error message"]
        
        if "message" in data:
            return data["message"]
        
        return data
    
    def post_stop_mail(self, service, mail):
        data = self.api.post(
            f"/services/{service}/mail/mailbox/stop/{mail}",
        )

        if not data:
            return []
        
        if "Error message" in data:
            return data["Error message"]
        
        if "message" in data:
            return data["message"]
        
        return data
    
    def post_start_mail(self, service, mail):
        data = self.api.post(
            f"/services/{service}/mail/mailbox/start/{mail}",
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
    def put_update_mail_account(self, service, mail, body):
        data = self.api.put(
            f"/services/{service}/mail/mailbox/{mail}",
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
    def delete_mail_account(self, service, mail):
        data = self.api.delete(
            f"/services/{service}/mail/mailbox/{mail}",
        )

        if not data:
            return []
        
        if "Error message" in data:
            return data["Error message"]
        
        if "message" in data:
            return data["message"]
        
        return data
    
