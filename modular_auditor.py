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

def calculate_tax(amount):
    tax_rate = 0.10
    tax = amount * tax_rate
    return tax    

def process_delivery(current_total, new_value):
    current_total += new_value
    print("Inventory total is now:", current_total)
    return current_total

def generate_report(processed_deliveries, failed_attempts):
    print("==================================")
    print("Final Report:")
    print("Total Processed Deliveries:", processed_deliveries)
    print("Number of Failed/Rejected Entries:", failed_attempts)

while True:
    user_input = get_valid_input()

    if user_input == "quit":
        generate_report(processed_deliveries, failed_attempts)
        break

    if user_input is None:
        failed_attempts += 1
        continue

    tax = calculate_tax(user_input)
    current_total = process_delivery(current_total, user_input)
    processed_deliveries += 1
    print("Processed deliveries:", processed_deliveries)
    print("Tax for this delivery:", tax)