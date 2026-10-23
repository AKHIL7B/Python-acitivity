reorder_level = 10
n = int(input("Number of products: "))

catalogue = []
invalid_count = 0

for i in range(1, n + 1):
    pid = input("Product " + str(i) + " - id: ")
    price = float(input("Product " + str(i) + " - price: "))
    stock = int(input("Product " + str(i) + " - stock quantity: "))

    duplicate = False
    for item in catalogue:
        if item[0] == pid:
            duplicate = True

    if pid == "":
        print("Record", i, "invalid: empty product id")
        invalid_count = invalid_count + 1
    elif duplicate:
        print("Record", i, "invalid: duplicate product id", pid)
        invalid_count = invalid_count + 1
    elif price <= 0:
        print("Record", i, "invalid: price must be greater than 0")
        invalid_count = invalid_count + 1
    elif stock < 0:
        print("Record", i, "invalid: stock cannot be negative")
        invalid_count = invalid_count + 1
    else:
        catalogue.append((pid, price, stock))

print("\n--- Valid Catalogue ---")
print(f"{'ID':<8}{'Price':>10}{'Stock':>8}{'Value':>12}")

total_value = 0
reorder = []
for pid, price, stock in catalogue:
    value = price * stock
    total_value = total_value + value
    print(f"{pid:<8}{price:>10.2f}{stock:>8}{value:>12.2f}")
    if stock < reorder_level:
        reorder.append(pid)

print("\n--- Summary ---")
print("Valid records  :", len(catalogue))
print("Invalid records:", invalid_count)
print(f"Total inventory value: {total_value:.2f}")
if len(reorder) > 0:
    print("Items to replenish (stock below", reorder_level, "):", reorder)
else:
    print("No items need replenishment.")