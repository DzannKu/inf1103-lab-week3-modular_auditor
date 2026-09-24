current_total = 0
failed_attempts = 0
processed_deliveries = 0

def get_valid_input():
    new_value = input("Enter stock quantity (or 'quit' to stop): ")

    if new_value.lower() == "quit":
        return "quit"

    if not new_value.isdigit():
        print("Error. Invalid input. Please input a positive integer.")
        return None

    return int(new_value)
