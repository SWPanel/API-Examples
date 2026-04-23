from app.helpers.input import Input
from app.services.database_management.database_user_service import DatabaseUserService

class DatabaseUserUI:
    # ====================
    # GET
    # ====================
    @staticmethod
    def get_db_user():
        service = Input.required("\nService ID: ").upper()
        user    = Input.get("Search for user (leave empty for all users): ")

        if user == "":
            user = None

        print("\nLoading FTP accounts...")

        response = DatabaseUserService().get_all(service, user)

        print("Done!\n")

        Input.json_formatter(response)


    
    # ====================
    # POST
    # ====================
    @staticmethod
    def post_create_new_user():
        service = Input.required("\nService ID: ").upper()

        body = {}

        password = Input.required("Password: ")
        body["password"] = password

        ip_host = Input.required("Host IP: ")
        body["ip_host"] = ip_host

        print("Additional:")
        additional = {}
        
        description = Input.get("\tDescription (leave empty to skip): ")
        post_it     = Input.get("\tPost it (leave empty to skip): ")

        if description:
            additional["description"] = description

        if post_it:
            additional["post_it"] = post_it

        body["additional"] = additional 
        
        print("\nCreating new database user...")

        response = DatabaseUserService().post_create_new_user(service, body)

        print("Done!\n")

        Input.json_formatter(response)


    # ====================
    # PUT
    # ====================
    @staticmethod
    def put_update_account():
        service = Input.required("\nService ID: ").upper()
        user    = Input.required("User: ")

        body = {
            "user": user
        }

        password = Input.get("New password (leave empty to skip): ")
        if password:
            body["password"] = password

        ip_host = Input.get("New host IP (leave empty to skip): ")
        if ip_host:
            body["ip_host"] = ip_host

        print("Additional:")
        additional = {}

        description = Input.get("\tNew description (leave empty to skip): ")
        post_it     = Input.get("\tNew post it (leave empty to skip): ")

        if description:
            additional["description"] = description

        if post_it:
            additional["post_it"] = post_it

        if additional:
            body["additional"] = additional


        if not body:
            print("Nothing to update!")
            return
        
        print("\nUpdating database user...")

        response = DatabaseUserService().put_update_user(service, body)

        print("Done!\n")

        Input.json_formatter(response)


    # ====================
    # DELETE
    # ====================
    @staticmethod
    def delete_account():
        service = Input.required("\nService ID: ").upper()
        user    = Input.required("User ID: ").upper()

        print("\nDeleting database user account...")

        response = DatabaseUserService().delete_user(service, user)

        print("Done!\n")

        Input.json_formatter(response)
