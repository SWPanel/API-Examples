from app.http.api_client import ApiClient

class MailingListService:
    def __init__(self):
        self.api = ApiClient()

    # ====================
    # GET
    # ====================
    def get_mailing_lists(self, service, mailing_list):
        data = self.api.get(
            f"/services/{service}/mail/mailing_list/{mailing_list}"
        )

        if not data:
            return []
        
        return data.get('result', [])


    # ====================
    # POST
    # ====================
    def post_create_new_mailing_list(self, service, body):
        data = self.api.post(
            f"/services/{service}/mail/mailing_list/",
            data=body
        )

        if not data:
            return []
        
        if "Error message" in data:
            return data["Error message"]
        
        if "message" in data:
            return data["message"]
        
        return data
    
    def post_add_remove_emails_mailing_list(self, service, mailing_list, body):
        data = self.api.post(
            f"/services/{service}/mail/mailing_list/emails/{mailing_list}",
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
    def put_update_mailing_list(self, service, mailing_list, body):
        data = self.api.put(
            f"/services/{service}/mail/mailing_list/{mailing_list}",
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
    def delete_mailing_list(self, service, mailing_list):
        data = self.api.delete(
            f"/services/{service}/mail/mailing_list/{mailing_list}",
        )

        if not data:
            return []
        
        if "Error message" in data:
            return data["Error message"]
        
        if "message" in data:
            return data["message"]
        
        return data