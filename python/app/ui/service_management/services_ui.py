from app.helpers.input import Input
from app.helpers.main import Helpers
from app.services.service_management.services_service import ServicesService
from app.services.tools_service import ToolsService

class ServicesUI:
    # ====================
    # GET
    # ====================
    @staticmethod
    def get_services():
        service = Input.get("\nService ID (leave empty for all services): ").upper()

        if service == "":
            params = None

        else:
            params = {
                "id": service
            }

        print("\nLoading services...")

        response = ServicesService().get_all(params)

        print("Done!\n")

        Input.json_formatter(response)

    @staticmethod
    def get_check_status():
        service = Input.required("\nService ID: ").upper()

        print("\nLoading status...")

        response = ServicesService().get_check_status(service)

        print("Done!\n")

        Input.json_formatter(response)


    # ====================
    # POST
    # ====================
    @staticmethod
    def post_create_new_service():
        while True:
            print("\n=== Services ===")
            print("1. Cloud Server")
            print("2. Hosting Standard")
            print("3. RHA Hosting Plan")
            print("4. Hosting from Template")
            print("5. Hosting on my server")
            print("0. Go back")

            option = Input.get("\nOption: ")

            if option == "1":
                NewServices().create_cloud_server()

            elif option == "2":
                NewServices().create_standard_hosting()

            elif option == "3":
                NewServices().create_rha_hosting_plan()
                
            elif option == "4":
                NewServices().create_hosting_from_template()

            elif option == "5":
                NewServices().create_hosting_selfhosted()

            elif option == "0":
                break

            else:
                print("Option not valid")
    

class NewServices:

    def create_cloud_server(self):
        print("\n=== CLOUD SERVER ===\n")

        id_os = None
        id_app = None

        # =====================
        # OS / APP SELECTION
        # =====================
        while True:
            print("--- Choose what you want in your Cloud ---")
            print("1. Operating System")
            print("2. Application")

            option = Input.get("\nOption: ")

            if option == "1":
                print("\nLoading operating systems...\n")
                items = ToolsService().get_os()
                key = "id_os"

            elif option == "2":
                print("\nLoading applications...\n")
                items = ToolsService().get_apps()
                key = "id_cloud_app"

            else:
                print("Option not valid\n")
                continue

            for i, item in enumerate(items, 1):
                print(f"{i}. {item['values']['description']}")

            while True:
                choice = Input.ask_int("\nSelect: ")

                if 1 <= choice <= len(items):
                    selected = items[choice - 1]

                    if option == "1":
                        id_os = selected[key]
                    else:
                        id_app = selected[key]

                    break
                else:
                    print("Option not valid")

            break


        # =====================
        # CLOUD TYPE
        # =====================
        while True:
            print("\n--- Select Cloud Type ---")
            print("1. Cloud Standard")
            print("2. Cloud Xtreme")

            option = Input.get("\nOption: ")

            if option == "1":
                id_service_type = "23-CL01"
                id_cloud_pack   = "105"
                break

            elif option == "2":
                id_service_type = "25-CL01"
                id_cloud_pack   = "110"
                break

            else:
                print("Option not valid")


        # =====================
        # CUSTOMIZATION
        # =====================
        print("\n--- Customize your Cloud ---")

        if id_service_type == "23-CL01":
            vcores = Helpers.ask_int_with_step("vCores (1...24): ", 1, 24, 1)
            ram    = Helpers.ask_int_with_step("RAM (2...64): ", 2, 64, 2)
            hd     = Helpers.ask_int_with_step("GB Disk (20...2000): ", 20, 2000, 20)

        elif id_service_type == "25-CL01":
            vcores = Helpers.ask_int_with_step("vCores (2...24): ", 2, 24, 2)
            ram    = Helpers.ask_int_with_step("RAM (4...128): ", 4, 128, 4)
            hd     = Helpers.ask_int_with_step("GB Disk (50...2000): ", 50, 2000, 50)

        cloud_server = {
            "id_service_type": id_service_type,
            "id_cloud_pack": id_cloud_pack,
            "customize": {
                "specifications": {
                    "vcores": vcores,
                    "GB": {
                        "ram": ram,
                        "hd": hd
                    }
                }
            }
        }

        if id_os:
            cloud_server["customize"]["OS"] = {"id": id_os}

        if id_app:
            cloud_server["id_cloud_app"] = id_app


        body = {
            "cloud_server": cloud_server,
            "datacenter": "01"
        }

        print("\nCreating new cloud server...")

        response = ServicesService().post_create_new_service(body)

        print("Done!\n")

        Input.json_formatter(response)

    
    def create_standard_hosting(self):
        print("\n=== STANDARD HOSTING ===")

        # =====================
        # HOSTING PLAN
        # =====================
        print("\nLoading hosting plans...\n")

        hosting_plans = ToolsService().get_hosting()

        for i, plan in enumerate(hosting_plans, 1):
            print(f"{i}. {plan['values']['description']}")

        print("\nFor more information see: https://www.swhosting.com/hosting#plans")

        choice = Input.ask_int("\nSelect Hosting: ")

        if choice < 1 or choice > len(hosting_plans):
            print("Option not valid")
            return

        selected = hosting_plans[choice - 1]
        id_type  = selected["id_type"]


        # =====================
        # CUSTOMIZATION
        # =====================
        customize = {
            "add_disc_space": 0,
            "add_mailboxes": 0,
            "add_databases": 0,
            "php_version": "18-HP06"
        }

        if id_type != "25-H101":
            print("\n--- Customize Hosting ---\n")

        PLANS = {
            "25-H102": {
                "disk": (40, 60, 1),
                "mail": (10, 20, 1),
                "db":   (5, 50, 1),
            },
            "25-H103": {
                "disk": (60, 100, 1),
                "mail": (15, 20, 1),
                "db":   (10, 50, 1),
            },
            "25-H104": {
                "disk": (100, 160, 1),
                "mail": (20, 20, 1),
                "db":   (25, 50, 1),
            }
        }

        plan = PLANS.get(id_type)

        if not plan:
            print("Cannot customize!")
        else:
            disk_min, disk_max, disk_step = plan["disk"]
            mail_min, mail_max, mail_step = plan["mail"]
            db_min, db_max, db_step       = plan["db"]

            add_disc_space_total = Helpers.ask_int_with_step(
                f"SSD Disk GB ({disk_min}...{disk_max}): ",
                disk_min, disk_max, disk_step
            )

            add_mailboxes_total = Helpers.ask_int_with_step(
                f"Email accounts ({mail_min}...{mail_max}): ",
                mail_min, mail_max, mail_step
            )

            add_databases_total = Helpers.ask_int_with_step(
                f"Databases ({db_min}...{db_max}): ",
                db_min, db_max, db_step
            )

            customize["add_disc_space"] = add_disc_space_total - disk_min
            customize["add_mailboxes"]  = add_mailboxes_total - mail_min
            customize["add_databases"]  = add_databases_total - db_min


        # =====================
        # DOMAIN
        # =====================
        domain = Input.required("\nDomain: ")


        # =====================
        # MAIL ACCOUNT
        # =====================
        create_mail_account = Input.ask_bool("\nActivate first email to hosting (Y/N): ")

        if create_mail_account:
            mailbox = {
                "create_new": True,
                "email": Input.required("Email (example@domain.com): "),
                "password": Input.required("Password: ")
            }
        else:
            mailbox = {
                "create_new": False
            }
        

        # =====================
        # DATACENTER
        # =====================
        print("\n--- Select datacenter ---")

        print("\nLoading datacenters...\n")

        dcs = ToolsService().get_dc()

        for i, dc in enumerate(dcs, 1):
            print(f"{i}. {dc['values']['description']}")

        choice = Input.ask_int("\nSelect datacenter ubication: ")

        if choice < 1 or choice > len(dcs):
            print("Option not valid")
            return

        selected   = dcs[choice - 1]
        datacenter = selected["id_dc"]


        # =====================
        # BODY
        # =====================
        body = {
            "hosting": {
                "id_service_type": id_type,
                "customize": customize,
                "redirect": {
                    "activate": False,
                },
                "mailbox": mailbox
            },
            "domain": {
                "name": domain,
                "register": False,
                "transfer": False,
            },
            "datacenter": datacenter
        }

        print("\nCreating new hosting...")

        response = ServicesService().post_create_new_service(body)

        print("Done!\n")

        Input.json_formatter(response)

    
    def create_rha_hosting_plan(self):
        print("\n=== RHA HOSTING PLAN ===\n")

        print("Loading RHA hostings plans...\n")

        rha_hosting_plans = ToolsService().get_rha_hosting_plans()

        for i, rha in enumerate(rha_hosting_plans, 1):
            print(f"{i}. {rha["values"]["name"]}")

        choice = Input.ask_int("\nSelect RHA Hosting plan: ")

        if choice < 1 or choice > len(rha_hosting_plans):
            print("Option not valid.")
            return
        
        selected = rha_hosting_plans[choice - 1]
        id_rha   = selected["id"]


        # =====================
        # DOMAIN
        # =====================
        domain = Input.required("\nDomain: ")


        # =====================
        # MAIL ACCOUNT
        # =====================
        create_mail_account = Input.ask_bool("\nActivate first email to hosting (Y/N): ")

        if create_mail_account:
            mailbox = {
                "create_new": True,
                "email": Input.required("Email (example@domain.com): "),
                "password": Input.required("Password: ")
            }
        else:
            mailbox = {
                "create_new": False
            }


        # =====================
        # BODY
        # =====================
        body = {
            "hosting": {
                "RHA_id_plan": id_rha,
                "mailbox": mailbox
            },
            "domain": {
                "name": domain,
                "register": False,
                "transfer": False,
            },
        }

        print("\nCreating new RHA service...")

        response = ServicesService().post_create_new_service(body)

        print("Done!\n")

        Input.json_formatter(response)


    def create_hosting_from_template(self):
        print("\n=== CREATE HOSTING FROM TEMPLATE ===\n")

        print("Loading hosting templates...")

        templates = ToolsService().get_hosting_templates()

        for i, template in enumerate(templates, 1):
            print(f"{i}. {template["id_hosting_template"]}")

        choice = Input.ask_int("\nSelect hosting template: ")

        if choice < 1 or choice > len(templates):
            print("Option not valid")
            return
        
        selected    = templates[choice - 1]
        id_template = selected["id_hosting_template"]


        # =====================
        # MAIL ACCOUNT
        # =====================
        create_mail_account = Input.ask_bool("\nActivate first email to hosting (Y/N): ")

        if create_mail_account:
            mailbox = {
                "create_new": True,
                "email": Input.required("Email (example@domain.com): "),
                "password": Input.required("Password: ")
            }
        else:
            mailbox = {
                "create_new": False
            }


        # =====================
        # DOMAIN
        # =====================
        domain = Input.required("\nDomain: ")


        # =====================
        # BODY
        # =====================
        body = {
            "hosting": {
                "templates": {
                    "hosting": id_template
                },
                "swpanel_login": False,
                "mailbox": mailbox
            },
            "domain": {
                "name": domain,
                "register": False,
                "transfer": False,
            },
        }

        print("\nCreating new hosting from template...")

        response = ServicesService().post_create_new_service(body)

        print("Done!\n")

        Input.json_formatter(response)
        

    def create_hosting_selfhosted(self):
        print("\n=== HOSTING ON MY SERVER ===\n")

        print("Loading hosting on server templates...\n")

        hostings = ToolsService().get_hosting_selfhosted()

        for i, hosting in enumerate(hostings, 1):
            print(f"{i}. {hosting["id_resources_limit_template"]}")
            print(f"\tMax Cores: {hosting["values"]["limitations"]["cores"]["values"]}")
            print(f"\tMax RAM: {hosting["values"]["limitations"]["ram"]["values"]}")
            print(f"\tMax IOPS: {hosting["values"]["limitations"]["iops"]["values"]}")

        choice = Input.ask_int("\nSelect hosting template: ")

        if choice < 1 or choice > len(hostings):
            print("Option not valid")
            return
        
        selected    = hostings[choice - 1]
        id_template = selected["id_resources_limit_template"]
        
        
        # =====================
        # SERVER
        # =====================
        print("\n--- Server Especifications ---\n")

        web      = Input.required("\nWeb server ID: ")
        mail     = Input.required("Mail server ID: ")
        database = Input.required("Database server ID: ")
        dns1     = Input.required("Name of the first DNS server: ")
        dns2     = Input.required("Name of the second DNS server: ")

        servers = {
            "web": web,
            "mail": mail,
            "database": database,
            "dns1": dns1,
            "dns3": dns2
        }


        backup = Input.ask_bool("Activate backup (Y/N): ")


        # =====================
        # MAIL ACCOUNT
        # =====================
        create_mail_account = Input.ask_bool("\nActivate first email to hosting (Y/N): ")

        if create_mail_account:
            mailbox = {
                "create_new": True,
                "email": Input.required("Email (example@domain.com): "),
                "password": Input.required("Password: ")
            }
        else:
            mailbox = {
                "create_new": False
            }


        # =====================
        # DOMAIN
        # =====================
        domain = Input.required("\nDomain: ")


        # =====================
        # BODY
        # =====================
        body = {
            "hosting": {
                "templates": {
                    "id_resouces_limitation": id_template
                },
                "servers": servers,
                "backup": {
                    "activate": backup
                },
                "swpanel_login": {
                    "activate": False
                },
                "redirect": {
                    "activate": False
                },
                "mailbox": mailbox
            },
            "domain": {
                "name": domain,
                "register": False,
                "transfer": False,
            },
        }

        print("\nCreating new hosting on my server...")

        response = ServicesService().post_create_new_service(body)

        print("Done!\n")

        Input.json_formatter(response)