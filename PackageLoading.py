current_package_weight = 0
total_package_sent = 0
total_package_weight = 0
unused_capacity = 0
total_unused_capacity = 0
package_most_unused = 0
number_most_unused = 0
amount_unused_package = 0

total_item = int(input("How many items do you have?"))
for number in range(1, total_item + 1):
    item_weight = int(input(f"\n{number}: What is the weights of the item? "))
    current_package_weight = int(current_package_weight + item_weight)
    total_package_weight = total_package_weight + item_weight

    if item_weight < 1 or item_weight > 10:
        print("Error, item range from 1kg to 10kg only.")
        break

    if 0 < current_package_weight < 20:
        print("Add more item")
        continue

    elif current_package_weight >= 20:
        current_package_weight -= item_weight
        total_package_sent = total_package_sent + 1
        package_number = total_package_sent
        print("\nPackage sent No.:", package_number)
        unused_capacity = 20 - current_package_weight
        total_unused_capacity = package_number * 20 - (total_package_weight - item_weight)
        print("\n Current Package's Weight:", current_package_weight)
        print("\nTotal Unused Capacity:", total_unused_capacity)

        if unused_capacity > package_most_unused:
            package_most_unused = unused_capacity
            number_most_unused = package_number

        current_package_weight = item_weight

if current_package_weight > 0:
    unused_capacity = 20 - current_package_weight
    total_package_sent = total_package_sent + 1
    package_number = total_package_sent
    total_unused_capacity = package_number * 20 - total_package_weight

    if unused_capacity > package_most_unused:
        package_most_unused = unused_capacity
        number_most_unused = package_number

print("\nNumber of package sent:", total_package_sent)
print("\nTotal weight of package sent:", total_package_weight)
print("\nTotal unused capacity:", total_unused_capacity)
print("\nPackage number with most unused weight:", number_most_unused)
print("\nTotal amount of unused capacity in the package", package_most_unused)
