from app.helpers.input import Input
from app.services.mail_management.mailing_list_service import MailingListService

class MailingListUI:
    # ====================
    # GET
    # ====================
    @staticmethod
    def get_mailing_lists():
        service      = Input.required("\nService UI: ")
        mailing_list = Input.get("Mailing list (leave empty to list all): ")

        print("\nLoading mailing lists information...")

        response = MailingListService().get_mailing_lists(service, mailing_list)

        print("Done!\n")

        Input.json_formatter(response)


    # ====================
    # POST
    # ====================
    @staticmethod
    def post_create_new_mailing_list():
        service      = Input.required("\nService UI: ")
        mailing_list = Input.required("Mailing list: ")
        sender_name  = Input.required("Sender name: ")

        print("Administrator:")
        administrator_email = Input.required("\tEmail: ")

        print("Destination:")
        destination_email = Input.get("Emails (leave empty to skip): ")

        post_it = Input.get("Post it (leave empty to skip): ")

        body = {
            "mailing_list": mailing_list,
            "sender_name": sender_name,
            "administrator": {
                "email": administrator_email
            },
            "destination": {
                "emails": destination_email
            },
            "post_it": post_it
        }

        print("\nCreating new mailing list...")

        response = MailingListService().post_create_new_mailing_list(service, body)

        print("Done!\n")

        Input.json_formatter(response)

    @staticmethod
    def post_add_remove_emails_mailing_list():
        service      = Input.required("\nService UI: ")
        mailing_list = Input.required("Mailing list: ")

        print("\n=== Options ===")
        print("1. Add emails")
        print("2. Delete emails")                

        option = Input.get("\nOption: ")

        if option == "1":
            emails    = Input.required("Emails (separated by ';'): ")
            overwrite = Input.ask_bool("Overwrite? (Y/N): ")

            body = {
                "add": {
                    "email": emails,
                    "overwrite": overwrite
                }
            }

        elif option == "2":
            emails = Input.required("Emails (separated by ';'): ")

            body = {
                "delete": {
                    "emails": emails
                }
            }

        else:
            print("Option not valid")
            return
        
        print(f"\nAdding/removing emails from {mailing_list} mailing_list...")

        response = MailingListService().post_add_remove_emails_mailing_list(service, mailing_list, body)

        print("Done!\n")

        Input.json_formatter(response)


    # ====================
    # PUT
    # ====================
    @staticmethod
    def put_update_mailing_list():
        service      = Input.required("\nService UI: ")
        mailing_list = Input.required("Mailing list: ")
        sender_name  = Input.get("Sender name (leave empty to skip): ")

        print("Administrator:")
        administrator_email = Input.get("\tNew email (leave empty to skip): ")

        post_it = Input.get("Post it (leave empty to skip): ")

        body = {
            "sender_name": sender_name,
            "administrator": {
                "email": administrator_email
            },
            "post_it": post_it
        }

        print(f"\nUpdating {mailing_list} mailing_list...")

        response = MailingListService().put_update_mailing_list(service, mailing_list, body)

        print("Done!\n")

        Input.json_formatter(response)


    # ====================
    # DELETE
    # ====================
    @staticmethod
    def delete_mailing_list():
        service      = Input.required("\nService UI: ")
        mailing_list = Input.required("Mailing list: ")
        
        print(f"\nDeleting {mailing_list} list...")

        response = MailingListService().delete_mailing_list(service, mailing_list)

        print("Done!\n")

        Input.json_formatter(response)