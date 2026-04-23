from app.helpers.input import Input

class Helpers:
    @staticmethod
    def ask_int_with_step(message, min_value, max_value, step):
        while True:
            value = Input.ask_int(message)

            if value < min_value or value > max_value:
                print(f"Value must be between {min_value} and {max_value}")
                continue

            if (value - min_value) % step != 0:
                print(f"Value must increase in steps of {step}")
                continue

            return value