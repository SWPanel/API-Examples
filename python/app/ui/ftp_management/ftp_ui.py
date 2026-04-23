from app.helpers.input import Input
from app.services.ftp_management.ftp_service import FTPService

class FTPUI:
    # ====================
    # GET
    # ====================
    @staticmethod
    def get_ftp_accounts():
        service    = Input.required("\nService ID: ").upper()
        id_account = Input.get("Search for ID account (leave empty for all FTP accounts): ")

        if id_account == "":
            id_account = None

        print("\nLoading FTP accounts...")

        response = FTPService().get_ftp(service, id_account)

        print("Done!\n")

        Input.json_formatter(response)


    # ====================
    # POST
    # ====================
    @staticmethod
    def post_create_new_account():
        service  = Input.required("\nService ID: ").upper()
        login    = Input.required("FTP login account name: ")

        body = {
            "login": login
        }

        password = Input.required("Password: ")
        body["password"] = password


        print("Additional:")
        description = Input.get("\tDescription (leave empty to skip): ")

        if description:
            body["additional"] = {
                "description": description
            }


        print("Access:")
        directory = Input.required("\tDirectory: ")
        read_only = Input.get("\tRead only (Y/N, leave empty to skip): ").lower()

        access = {}

        access["directory"] = directory

        if read_only in ["y", "yes", "true"]:
            access["read_only"] = True
        elif read_only in ["n", "no", "false"]:
            access["read_only"] = False

        if access:
            body["access"] = access

        print("Size:")
        value = Input.get("\tUnlimited (Y/N): ").lower()

        if value in ["y", "yes", "true"]:
            body["size"] = {"unlimited": True}

        elif value in ["n", "no", "false"]:
            body["size"] = {"unlimited": False}

        elif value == "":
            pass

        else:
            print("Option not valid")
        
        print("\nCreating new FTP account...")

        response = FTPService().post_create_new_account(service, body)

        print("Done!\n")

        Input.json_formatter(response)

    @staticmethod
    def post_stop_account():
        service    = Input.required("\nService ID: ").upper()
        id_account = Input.required("Account ID: ").upper()

        print("\nStopping FTP account...")

        response = FTPService().post_stop_account(service, id_account)

        print("Done!\n")

        Input.json_formatter(response)

    @staticmethod
    def post_start_account():
        service    = Input.required("\nService ID: ").upper()
        id_account = Input.required("Account ID: ").upper()

        print("\nStarting FTP account...")

        response = FTPService().post_start_account(service, id_account)

        print("Done!\n")

        Input.json_formatter(response)


    # ====================
    # PUT
    # ====================
    @staticmethod
    def put_update_account():
        service  = Input.required("\nService ID: ").upper()
        id_account = Input.required("Account ID: ").upper()
        # login    = Input.required("Login FTP account: ")

        body = {
            # "login": login
        }

        password = Input.get("New password (leave empty to skip): ")
        if password:
            body["password"] = password


        print("Additional:")
        description = Input.get("\tDescription (leave empty to skip): ")

        if description:
            body["additional"] = {
                "description": description
            }


        print("Access:")
        directory = Input.get("\tDirectory (leave empty to skip): ")
        read_only = Input.get("\tRead only (Y/N, leave empty to skip): ").lower()

        access = {}

        if directory:
            access["directory"] = directory

        if read_only in ["y", "yes", "true"]:
            access["read_only"] = True
        elif read_only in ["n", "no", "false"]:
            access["read_only"] = False

        if access:
            body["access"] = access


        print("Size:")
        value = Input.get("\tUnlimited (Y/N, leave empty to skip): ").lower()

        if value in ["y", "yes", "true"]:
            body["size"] = {"unlimited": True}

        elif value in ["n", "no", "false"]:
            body["size"] = {"unlimited": False}

        elif value == "":
            pass

        else:
            print("Option not valid")
        
        print("\nUpdating FTP account information...")

        response = FTPService().put_update_account(service, id_account, body)

        print("Done!\n")

        Input.json_formatter(response)


    # ====================
    # DELETE
    # ====================
    @staticmethod
    def delete_account():
        service    = Input.required("\nService ID: ").upper()
        id_account = Input.required("Account ID: ").upper()

        print("\nDeleting FTP account...")

        response = FTPService().delete_account(service, id_account)

        print("Done!\n")

        Input.json_formatter(response)
