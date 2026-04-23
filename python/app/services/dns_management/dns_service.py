from app.http.api_client import ApiClient

class DNSService:
    def __init__(self):
        self.api = ApiClient()

    # ====================
    # GET
    # ====================
    def get_all(self, service):

        data = self.api.get(
            f"/services/{service}/dns/"
        )

        if not data:
            return []
        
        return data.get("result", [])


    # ====================
    # POST
    # ====================
    def post_create_new_dns_record(self, service, body):
        data = self.api.post(
            f"/services/{service}/dns/",
            data=body
        )

        if not data:
            return []
        
        if "Error message" in data:
            return data["Error message"]
        
        if "message" in data:
            return data["message"]
        
        return data
    
    def post_create_advanced_dns_record(self, service, dns_zone):
        data = self.api.post(
            f"/services/{service}/dns/advanced/{dns_zone}"
        )

        if not data:
            return []
        
        if "Error message" in data:
            return data["Error message"]
        
        if "message" in data:
            return data["message"]
        
        return data
    
    def post_recreate_dns_zone(self, service, dns_zone):
        data = self.api.post(
            f"/services/{service}/dns/recreate/{dns_zone}"
        )

        if not data:
            return []
        
        if "Error message" in data:
            return data["Error message"]
        
        if "message" in data:
            return data["message"]
        
        return data
    
    def post_change_ttl_dns_zone(self, service, dns_zone, body):
        data = self.api.post(
            f"/services/{service}/dns/ttl/{dns_zone}",
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
    def put_update_dns_record(self, service, record_id, body):
        data = self.api.put(
            f"/services/{service}/dns/{record_id}",
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
    def delete_dns_record(self, service, record_id):
        data = self.api.delete(
            f"/services/{service}/dns/{record_id}",
        )

        if not data:
            return []
        
        if "Error message" in data:
            return data["Error message"]
        
        if "message" in data:
            return data["message"]
        
        return data