from app.http.api_client import ApiClient

class ToolsService:
    def __init__(self):
        self.api = ApiClient()

    # ====================
    # GET
    # ====================
    def get_os(self):
        params = {
            "order": "description",
            "descent": False
        }

        data = self.api.get(
            "/tools/so/",
            params=params
        )

        if not data:
            return []

        filtered = []

        for item in data.get("result"):
            if item.get("values", {}).get("type") != "":
                filtered.append(item)
        
        return filtered
    

    def get_apps(self):
        params = {
            "order": "description",
            "descent": False    
        }

        data = self.api.get(
            f"/tools/cloud_app/",
            params=params
        )

        if not data:
            return []
        
        return data.get("result", [])


    def get_dc(self):
        params = {
            "order": "description",
            "descent": False
        }

        data = self.api.get(
            "/tools/dc/",
            params=params
        )

        if not data:
            return []
        
        return data.get("result", [])
    

    def get_hosting(self):
        data = self.api.get(
            "/tools/hosting_type/"
        )

        if not data:
            return []
        
        filtered = []

        for item in data.get("result"):
            if item.get("category", {}).get("id") == "6":
                filtered.append(item)

        return filtered
    
    
    def get_rha_hosting_plans(self):
        data = self.api.get(
            "/RHA/services/hosting_plans/"
        )

        if not data:
            return []
        
        return data.get("result", [])
    

    def get_hosting_templates(self):
        data = self.api.get(
            "/tools/templates/hosting/"
        )

        if not data:
            return []
        
        return data.get("result", [])
    

    def get_hosting_selfhosted(self):
        data = self.api.get(
            "/tools/templates/resources_limit/"
        )

        if not data:
            return []
        
        return data.get("result", [])