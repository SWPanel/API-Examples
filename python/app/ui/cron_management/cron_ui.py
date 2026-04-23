import datetime
from app.helpers.input import Input
from app.services.crons_management.crons_service import CronsService

class CronUI:
    # ====================
    # GET
    # ====================
    @staticmethod
    def get_crons():
        service = Input.required("\nService ID: ").upper()
        cron_id = Input.get("Cron ID (leave empty for all databases): ")

        if cron_id == "":
            cron_id = None

        print("\nLoading crons...")

        response = CronsService().get_all(service, cron_id)

        print("Done!\n")

        Input.json_formatter(response)

    @staticmethod
    def get_cron_users():
        service = Input.required("\nService ID: ").upper()

        print("Loading cron users...")
    
        response = CronsService().get_cron_users(service)

        print("Done!\n")

        Input.json_formatter(response)

    # ====================
    # POST
    # ====================
    @staticmethod
    def post_create_new_cron():
        service       = Input.required("\nService ID: ").upper()
        name          = Input.required("Cron name: ")
        user_execuion = Input.required("User ID execution: ")
        content       = Input.required("Content: ")

        print("Timer: ")
        minutes  = Input.ask_int("\tMinutes (0...59): ")
        hours    = Input.ask_int("\tHour (0...23): ")
        days     = Input.ask_int("\tDays (1...31): ")
        month    = Input.get("\tMonths (1...12, separated by a coma): ")
        week_day = Input.get("\tWeek day (1...7, separated by a coma): ")

        scheduler = {
            "customize": {
                "minutes": {
                    "every": {
                        "number": minutes
                    },
                    "odd": False,
                    "even": False
                },
                "hours": {
                    "every": {
                        "number": hours
                    },
                    "odd": False,
                    "even": False
                },
                "days": {
                    "every": {
                        "number": days
                    },
                    "odd": False,
                    "even": False
                },
                "weekday": {
                    "every": {
                        "number": week_day
                    },
                    "odd": False,
                    "even": False
                },
                "months": {
                    "every": {
                        "number": month
                    },
                    "odd": False,
                    "even": False
                },
            }
        }

        body = {
            "additional": {
                "name": name
            },
            "user_execution": user_execuion,
            "date": {
                "start": datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            },
            "content": content,
            "scheduler": scheduler
        }

        print("\nCreating new cron...")

        response = CronsService().post_create_new_cron(service, body)

        print("Done!\n")

        Input.json_formatter(response)

    @staticmethod
    def post_start_cron():
        service = Input.required("\nService ID: ").upper()
        cron_id = Input.required("Cron ID: ")

        print("\nStarting cron...")

        response = CronsService().post_start_cron(service, cron_id)

        print("Done!\n")

        Input.json_formatter(response)

    @staticmethod
    def post_stop_cron():
        service = Input.required("\nService ID: ").upper()
        cron_id = Input.required("Cron ID: ")

        print("\nStopping cron...")

        response = CronsService().post_stop_cron(service, cron_id)

        print("Done!\n")

        Input.json_formatter(response)


    # ====================
    # PUT
    # ====================
    @staticmethod
    def put_update_cron():
        service       = Input.required("\nService ID: ").upper()
        id_cron       = Input.required("Cron ID: ")
        name          = Input.get("Cron name: ")
        user_execuion = Input.get("User ID execution: ")
        content       = Input.get("Content: ")

        print("Timer: ")
        minutes  = Input.ask_int("\tMinutes (0...59): ")
        hours    = Input.ask_int("\tHour (0...23): ")
        days     = Input.ask_int("\tDays (1...31): ")
        month    = Input.get("\tMonths (1...12, separated by a coma): ")
        week_day = Input.get("\tWeek day (1...7, separated by a coma): ")
        
        scheduler = {
            "customize": {
                "minutes": {
                    "every": {
                        "number": minutes
                    },
                    "odd": False,
                    "even": False
                },
                "hours": {
                    "every": {
                        "number": hours
                    },
                    "odd": False,
                    "even": False
                },
                "days": {
                    "every": {
                        "number": days
                    },
                    "odd": False,
                    "even": False
                },
                "weekday": {
                    "every": {
                        "number": week_day
                    },
                    "odd": False,
                    "even": False
                },
                "months": {
                    "every": {
                        "number": month
                    },
                    "odd": False,
                    "even": False
                },
            }
        }

        body = {
            "additional": {
                "name": name
            },
            "user_execution": user_execuion,
            "date": {
                "start": datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            },
            "content": content,
            "scheduler": scheduler
        }

        print("\nCreating new cron...")

        response = CronsService().put_update_cron(service, id_cron, body)

        print("Done!\n")

        Input.json_formatter(response)


    # ====================
    # DELETE
    # ====================
    @staticmethod
    def delete_cron():
        service = Input.required("\nService ID: ").upper()
        cron_id = Input.required("Cron ID: ")

        print("\nDeleting cron...")

        response = CronsService().delete_cron(service, cron_id)

        print("Done!\n")

        Input.json_formatter(response)