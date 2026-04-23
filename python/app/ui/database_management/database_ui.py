from app.helpers.input import Input
from app.services.database_management.database_service import DatabaseService

class DatabaseUI:
    # ====================
    # GET
    # ====================
    @staticmethod
    def get_db():
        service = Input.required("\nService ID: ").upper()
        db_name = Input.get("Search for database name (leave empty for all databases): ")

        if db_name == "":
            db_name = None

        print("\nLoading FTP accounts...")

        response = DatabaseService().get_all(service, db_name)

        print("Done!\n")

        Input.json_formatter(response)

    
    # ====================
    # POST
    # ====================
    @staticmethod
    def post_create_new_db():
        service = Input.required("\nService ID: ").upper()
        db_name = Input.required("Database name: ")

        new_user = None
        users = None

        while True:
            print("\nAccess user/s:")
            print("1. Create new database user")
            print("2. Use existing database user")

            option = Input.get("\nOption: ")

            # =====================
            # NEW USER
            # =====================
            if option == "1":

                password = Input.required("Password: ")

                print("Privileges:")
                print("\t1. Full control")
                print("\t2. Read only")

                while True:
                    opt = Input.required("Option: ")

                    if opt == "1":
                        privileges = {"fullcontrol": True, "readonly": False}
                        break
                    elif opt == "2":
                        privileges = {"fullcontrol": False, "readonly": True}
                        break
                    else:
                        print("Option not valid")

                new_user = {
                    "create_new": True,
                    "password": password,
                    "privileges": privileges
                }

                break

            # =====================
            # EXISTING USERS
            # =====================
            elif option == "2":

                users = []

                while True:
                    id_user = Input.required("User id: ")

                    print("Privileges:")
                    print("\t1. Full control")
                    print("\t2. Read only")

                    while True:
                        opt = Input.required("Option: ")

                        if opt == "1":
                            privileges = {"fullcontrol": True, "readonly": False}
                            break
                        elif opt == "2":
                            privileges = {"fullcontrol": False, "readonly": True}
                            break
                        else:
                            print("Option not valid")

                    users.append({
                        "id_user": id_user,
                        "privileges": privileges
                    })

                    another = Input.ask_bool("Add another user? (Y/N): ")

                    if not another:
                        break

                break

            elif option == "0":
                return

            else:
                print("Option not valid")


        # =====================
        # BODY
        # =====================
        body = {
            "db_name": db_name
        }

        if new_user:
            body["new_user"] = new_user

        if users:
            body["users"] = users


        print("\nCreating new database...")

        response = DatabaseService().post_create_new_db(service, body)

        print("Done!\n")

        Input.json_formatter(response)


    # ====================
    # PUT
    # ====================
    @staticmethod
    def put_update_db():
        service = Input.required("\nService ID: ").upper()
        db_name = Input.required("Database name to edit: ")

        body = {}

        users = []

        print("Edit/add user:\n")

        while True:
            id_user = Input.get("User id: ")

            print("Privileges:")
            print("\t1. Full control")
            print("\t2. Read only")

            while True:
                opt = Input.required("\nOption: ")

                if opt == "1":
                    privileges = {"fullcontrol": True, "readonly": False}
                    break
                elif opt == "2":
                    privileges = {"fullcontrol": False, "readonly": True}
                    break
                else:
                    print("Option not valid")

            users.append({
                "id_user": id_user,
                "privileges": privileges
            })

            another = Input.ask_bool("Add another user? (Y/N): ")

            if not another:
                break

        body["users"] = users
        
        print("\nUpdating database...")

        response = DatabaseService().put_update_db(service, db_name, body)

        print("Done!\n")

        Input.json_formatter(response)


    # ====================
    # DELETE
    # ====================
    @staticmethod
    def delete_db():
        service = Input.required("\nService ID: ").upper()
        db_name = Input.required("Database name: ")

        print("\nDeleting database...")

        response = DatabaseService().delete_db(service, db_name)

        print("Done!\n")

        Input.json_formatter(response)
