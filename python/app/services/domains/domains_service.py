from app.http.api_client import ApiClient

class DomainsService:
    def __init__(self):
        self.api = ApiClient()

    # ====================
    # GET
    # ====================
    def get_domains(self, domain_id):

        if domain_id:
            data = self.api.get(
                f"/domains/{domain_id}/"
            )
        
        else:
            data = self.api.get(
                f"/domains/"
            )

        if not data:
            return []
        
        return data.get("result", [])
    
    def get_extensions(self, extension):

        if extension:
            data = self.api.get(
                f"/domains/prices/{extension}/"
            )
        
        else:
            data = self.api.get(
                f"/domains/prices/"
            )

        if not data:
            return []
        
        return data.get("result", [])
    
    def get_availibility(self, domain):

        data = self.api.get(
            f"/domains/{domain}/available/"
        )

        if not data:
            return []
        
        return data.get("result", [])

    def get_whois(self, domain):

        data = self.api.get(
            f"/domains/{domain}/whois/"
        )

        if not data:
            return []
        
        return data.get("result", [])
    
    def get_contacts(self, contact_id):

        if contact_id:
            data = self.api.get(
                f"/domains/contact/{contact_id}/"
            )

        else:
            data = self.api.get(
                f"/domains/contact/"
            )

        if not data:
            return []
        
        return data.get("result", [])
    
    def get_hostnames(self, hostname_id):

        if hostname_id:
            data = self.api.get(
                f"/domains/host/{hostname_id}/"
            )

        else:
            data = self.api.get(
                f"/domains/host/"
            )

        if not data:
            return []
        
        return data.get("result", [])

    # ====================
    # POST
    # ====================
    def post_register_domain(self, body):
        data = self.api.post(
            f"/domains/register/",
            data=body
        )

        if not data:
            return []
        
        if "Error message" in data:
            return data["Error message"]
        
        if "message" in data:
            return data["message"]
        
        return data
    
    def post_transfer_domain(self, body):
        data = self.api.post(
            f"/domains/transfer/",
            data=body
        )

        if not data:
            return []
        
        if "Error message" in data:
            return data["Error message"]
        
        if "message" in data:
            return data["message"]
        
        return data
    
    def post_renew_domain(self, body):
        data = self.api.post(
            f"/domains/renew/",
            data=body
        )

        if not data:
            return []
        
        if "Error message" in data:
            return data["Error message"]
        
        if "message" in data:
            return data["message"]
        
        return data

    def post_create_contact(self, body):
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
    
    def post_create_hostname(self, body):
        data = self.api.post(
            f"/domains/host/",
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
    def put_update_contact(self, contact_id, body):

        data = self.api.put(
            f"/domains/contact/{contact_id}",
            data=body
        )

        if not data:
            return []
        
        if "Error message" in data:
            return data["Error message"]
        
        if "message" in data:
            return data["message"]
        
        return data
    
    def put_update_hostname(self, hostname_id, body):

        data = self.api.put(
            f"/domains/host/{hostname_id}",
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
    def delete_contact(self, contact_id):

        data = self.api.delete(
            f"/domains/contact/{contact_id}",
        )

        if not data:
            return []
        
        if "Error message" in data:
            return data["Error message"]
        
        if "message" in data:
            return data["message"]
        
        return data
    
    def delete_hostname(self, hostname_id):

        data = self.api.delete(
            f"/domains/host/{hostname_id}",
        )

        if not data:
            return []
        
        if "Error message" in data:
            return data["Error message"]
        
        if "message" in data:
            return data["message"]
        
        return data
    