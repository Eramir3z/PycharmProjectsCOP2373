import functools
# two functions to be used to either determine the highest value or lowest
def highest(a,b):
    if a > b:
        return a
    elif a < b:
        return b
    else:
        return a and b
def lowest(a,b):
    if a < b:
        return a
    elif a > b:
        return b
    else:
        return a and b
# created two empty list to use later
expenses_list = []
cost_list = []
def main():
# made a loop to continually ask two questions, stops after "done" is typed
    while True:
        expense = input("Name of expense (type 'done' to end): ")
        if expense == "done":
            break
        cost = float(input("Cost of expense: "))
        expenses_list.append(expense)
        expenses_list.append(cost)
        cost_list.append(cost)
# used lambda to avoid making a third function for the total
    total_cost = functools.reduce(lambda a, b: a + b, cost_list)
    highest_cost = functools.reduce(highest, cost_list)
    lowest_cost = functools.reduce(lowest, cost_list)
# expense list is in ["str",int,"str",int] and [0,1,2,3] so if I could get the position of a number and subtract 1,
# then I could get the value that number belonged to
    highest_item = expenses_list[expenses_list.index(highest_cost) - 1]
    lowest_item = expenses_list[expenses_list.index(lowest_cost) - 1]
# finally print results
    print(f"Total amount: ${total_cost}")
    print(f"Item that cost the most: {highest_item}-> ${highest_cost}")
    print(f"Item that cost the least: {lowest_item}-> ${lowest_cost}")
# call main
main()