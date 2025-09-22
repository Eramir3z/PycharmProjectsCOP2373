def get_ticket_purchase():
    while True:
        try:
            t = int(input("Hello, how many tickets will you be buying today?: "))
            if 1 <= t <= 4:
                return t
            else:
                print("You may only purchase at most four tickets.")
        except ValueError:
            print("Invalid input. Please enter a number.")


def ticket_accumulator():
    total_tickets = 10
    remaining_tickets = total_tickets
    total_purchased = 0

    while remaining_tickets > 0:
        print(f"\nRemaining tickets: {remaining_tickets}")

        tickets_to_buy = get_ticket_purchase()

        if tickets_to_buy <= remaining_tickets:
            remaining_tickets -= tickets_to_buy
            total_purchased += 1
            print(f"You purchased {tickets_to_buy} tickets.")
            print(f"Remaining tickets after purchase: {remaining_tickets}")
        else:
            print(f"Not enough tickets available. Only {remaining_tickets} tickets left.")

    print("\nAll tickets have been sold!")
    print(f"Total number of buyers: {total_purchased}")


ticket_accumulator()
