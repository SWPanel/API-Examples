from app.helpers.input import Input
from app.services.mail_management.mail_service import MailService

class MailUI:
    # ====================
    # GET
    # ====================
    @staticmethod
    def get_emails_accounts():
        service = Input.required("\nService ID: ").upper()
        mail    = Input.get("Search for email (leave empty for all emails): ")

        if mail != "":
            print(f"\nLoading {mail} mail account information...")
        else:
            mail = None
            print("Loading mail accounts information...")

        response = MailService().get_all(service, mail)

        print("Done!\n")

        Input.json_formatter(response)

    @staticmethod
    def get_used_space_mail_account():
        service = Input.required("\nService ID: ").upper()
        mail    = Input.required("Email: ")
        
        print(f"\nLoading mail space for {mail}...")

        response = MailService().get_used_space(service, mail)

        print("Done!\n")

        Input.json_formatter(response)

    @staticmethod
    def get_login_swpanel_info():
        service = Input.required("\nService ID: ").upper()
        mail    = Input.required("Email: ")
        
        print(f"\nLoading SWPanel login information for {mail}...")

        response = MailService().get_login_swpanel_info(service, mail)

        print("Done!\n")

        Input.json_formatter(response)


    # ====================
    # POST
    # ====================
    @staticmethod
    def post_create_new_email():
        service  = Input.required("Service ID: ").upper()
        email    = Input.required("Email: ")
        password = Input.required("Password: ")

        print("Size: ")
        unlimited = Input.ask_bool("\tUnlimited (Y/N): ")
        
        size = {
            "unlimited": unlimited
        }

        if not unlimited:
            size["mb"] = Input.get("\tMB: ")

        print("Forward: ")
        activateForward = Input.ask_bool("\tActivate (Y/N): ")

        forward = {
            "activate": activateForward
        }

        if activateForward:
            forward["to"] = Input.get("\tTo: ")
            forward["copy"] = Input.ask_bool("\tCopy (Y/N): ")


        print("Notify use:")
        activateNotify =  Input.ask_bool("\tActivate (Y/N): ")

        notify = {
            "activate": activateNotify
        }

        if activateNotify:
            notify["percent"] = Input.ask_int("\tPercent: ")

        post_it = Input.get("Post it (it can be empty): ")

        body = {
            "email": email,
            "password": password,
            "size": size,
            "forward": forward,
            "notify_user": notify,
            "post_it": post_it
        }

        print(f"\nCreating new email...")

        response = MailService().post_create_new_email(service, body)

        print("Done!\n")

        Input.json_formatter(response)

    @staticmethod
    def post_update_login_swpanel_info():
        service        = Input.required("Service ID: ")
        mail           = Input.required("Email: ")
        activate_login = Input.ask_bool("Activate login to SWPanel (Y/N)? ")
        access_profile = Input.ask_int("Access profile ID: ")

        body = {
            "swpanel_login": {
                "activate": activate_login,
                "access_profile": access_profile
            }
        }

        print(f"\nUpdating login SWPanel information on {mail}...")

        response = MailService().post_update_login_swpanel_info(service, mail, body)

        print("Done!\n")

        Input.json_formatter(response)

    @staticmethod
    def post_stop_mail():
        service = Input.required("Service ID: ")
        mail    = Input.required("Email: ")
        
        print(f"\nStopping {mail}...")

        response = MailService().post_stop_mail(service, mail)

        print("Done!\n")

        Input.json_formatter(response)

    @staticmethod
    def post_start_mail():
        service = Input.required("Service ID: ")
        mail    = Input.required("Email: ")
        
        print(f"\nStarting {mail}...")

        response = MailService().post_start_mail(service, mail)

        print("Done!\n")

        Input.json_formatter(response)


    # ====================
    # PUT
    # ====================
    @staticmethod
    def put_update_mail_account():
        service  = Input.required("Service ID: ").upper()
        mail    = Input.required("Email: ")

        body = {}

        password = Input.get("New password (leave empty to skip): ")
        if password != "":
            body["password"] = password


        print("Size:")
        change_size = Input.ask_bool("\tChange size? (Y/N): ")

        if change_size:
            unlimited = Input.ask_bool("\tUnlimited (Y/N): ")

            size = {
                "unlimited": unlimited
            }

            if not unlimited:
                size["mb"] = Input.ask_int("\tMB: ")

            body["size"] = size


        print("Forward:")
        change_forward = Input.ask_bool("\tChange forward? (Y/N): ")

        if change_forward:
            activateForward = Input.ask_bool("\tActivate (Y/N): ")

            forward = {
                "activate": activateForward
            }

            if activateForward:
                forward["to"] = Input.get("\tTo: ")
                forward["copy"] = Input.ask_bool("\tCopy (Y/N): ")

            body["forward"] = forward


        print("Notify user:")
        change_notify = Input.ask_bool("\tChange notify? (Y/N): ")

        if change_notify:
            activateNotify = Input.ask_bool("\tActivate (Y/N): ")

            notify = {
                "activate": activateNotify
            }

            if activateNotify:
                notify["percent"] = Input.ask_int("\tPercent: ")

            body["notify_user"] = notify


        post_it = Input.get("New post it (leave empty to skip): ")
        if post_it != "":
            body["post_it"] = post_it


        print(f"\nUpdating {mail} account...")

        response = MailService().put_update_mail_account(service, mail, body)

        print("Done!\n")

        Input.json_formatter(response)


    # ====================
    # DELETE
    # ====================
    @staticmethod
    def delete_mail_account():
        service = Input.required("Service ID: ")
        mail    = Input.required("Email: ")
        
        print(f"\nDeleting {mail} account...")

        response = MailService().delete_mail_account(service, mail)

        print("Done!\n")

        Input.json_formatter(response)
