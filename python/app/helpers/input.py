import json

class Input:
    @staticmethod
    def get(message: str) -> str:
        return input(message).strip()
    
    @staticmethod
    def pause():
        input('\nPress ENTER to continue...')

    @staticmethod
    def required(message: str) -> str:
        while True:
            value = Input.get(message)

            if value == "":
                print("This field is required!")
            else:
                return value

    @staticmethod
    def ask_bool(message: str) -> bool:
        while True:
            value = input(message).strip().lower()

            if value in ["y", "yes", "true"]:
                return True
            elif value in ["n", "no", "false"]:
                return False
            else:
                print("Option not valid (Y/N)")

    @staticmethod
    def ask_int(message: str) -> bool:
        while True:
            value = Input.get(message)

            try:
                return int(value)
            except ValueError:
                print("Please enter a valid number")

    @staticmethod
    def json_formatter(message: str):
        print(json.dumps(message, indent=2, ensure_ascii=False))