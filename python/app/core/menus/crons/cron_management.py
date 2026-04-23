from app.helpers.input import Input
from app.ui.cron_management.cron_ui import CronUI

class CronsManagementMenu:
    def run(self):
        while True:
            print("\n=== Crons MANAGEMENT ===")
            print("1. Get crons")
            print("2. Get cron users")
            print("3. Create new cron")
            print("4. Start cron")
            print("5. Stop cron")
            print("6. Modify cron")
            print("7. Delete cron")
            print("0. Back")

            option = Input.get("\nOption: ")

            if option == "1":
                CronUI().get_crons()

            elif option == "2":
                CronUI().get_cron_users()

            elif option == "3":
                CronUI().post_create_new_cron()

            elif option == "4":
                CronUI().post_start_cron()

            elif option == "5":
                CronUI().post_stop_cron()

            elif option == "6":
                CronUI().put_update_cron()

            elif option == "7":
                CronUI().delete_cron()

            elif option == "0":
                break

            else:
                print("Option not valid")

