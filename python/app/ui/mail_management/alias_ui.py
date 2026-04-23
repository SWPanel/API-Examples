from app.helpers.input import Input
from app.services.mail_management.alias_service import AliasService

class AliasUI:
    # ====================
    # GET
    # ====================
    @staticmethod
    def get_alias():
        service = Input.required("\nService ID: ").upper()
        alias   = Input.get("Search for alias (leave empty for all aliases): ")

        if alias == "":
            alias = None

        print("\nLoading aliases information...")

        response = AliasService().get_all(service, alias)

        print("Done!\n")

        Input.json_formatter(response)


    # ====================
    # POST
    # ====================
    @staticmethod
    def post_create_new_alias():
        service = Input.required("\nService ID: ").upper()
        alias   = Input.required("Email alias: ")
        
        print("Destination emails:")
        destination_emails = Input.required("\tEmails (separated with semicolons ';'): ")
        post_it            = Input.get("Post it (leave empty to skip): ")

        body = {
            "email_alias": alias,
            "destination": {
                "emails": destination_emails
            },
            "post_it": post_it
        }
        
        print("\nCreating new alias...")

        response = AliasService().post_create_new_alias(service, body)

        print("Done!\n")

        Input.json_formatter(response)


    # ====================
    # PUT
    # ====================
    @staticmethod
    def put_update_alias():
        service = Input.required("\nService ID: ")
        alias   = Input.required("Alias: ")
        
        print("Destination: ")
        destination_emails = Input.get("\tEmails (separated with semicolons ';'): ")
        post_it            = Input.get("Post it (leave empty to skip): ")

        body = {
            "destination": {
                "emails": destination_emails
            },
            "post_it": post_it
        }

        print(f"\nUpdating {alias} alias...")

        response = AliasService().put_update_alias(service, alias, body)

        print("Done!\n")

        Input.json_formatter(response)


    # ====================
    # DELETE
    # ====================
    @staticmethod
    def delete_alias():
        service = Input.required("\nService ID: ")
        alias   = Input.required("Alias: ")
        
        print(f"\nDeleting {alias} alias...")

        response = AliasService().delete_alias(service, alias)

        print("Done!\n")

        Input.json_formatter(response)