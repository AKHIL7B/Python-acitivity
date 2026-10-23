limit = 10
n = int(input("Number of days: "))

over_days = []
total_wastage = 0
valid_days = 0

for day in range(1, n + 1):
    prepared = int(input("Day " + str(day) + " - meals prepared: "))
    served = int(input("Day " + str(day) + " - meals served: "))
    leftover = int(input("Day " + str(day) + " - leftover meals: "))

    if prepared == 0:
        print("Day", day, ": invalid record, no meals prepared")
    elif served + leftover != prepared:
        print("Day", day, ": inconsistent record, served + leftover is not equal to prepared")
    else:
        wastage = leftover / prepared * 100
        total_wastage = total_wastage + wastage
        valid_days = valid_days + 1
        if wastage > limit:
            over_days.append(day)
            print(f"Day {day}: wastage {wastage:.2f}% - EXCEEDS the {limit}% limit")
        else:
            print(f"Day {day}: wastage {wastage:.2f}%")

print("\n--- Summary ---")
if valid_days == 0:
    print("No valid records to analyse.")
else:
    print(f"Average wastage over {valid_days} valid day(s): {total_wastage / valid_days:.2f}%")
    print("Days over the limit:", len(over_days))
    if len(over_days) > 0:
        print("Day numbers:", over_days)