# ======================================================================
# Case Study 42 : Student Marks Matrix Analysis
# Concepts used : variables, operators, conditionals, loops, strings,
#                 lists, nested lists (no functions / dictionaries)
# ======================================================================

MAX_MARKS = 100        # maximum marks per subject
PASS_MARK = 40         # minimum marks to pass a subject
LOW_AVG_LIMIT = 50     # subject average below this is "low performance"

print("=" * 66)
print("         STUDENT MARKS MATRIX ANALYSIS")
print("=" * 66)
print("1. Use sample data")
print("2. Enter data manually")
choice = input("Enter your choice (1/2): ").strip()
while choice != "1" and choice != "2":
    choice = input("Invalid choice. Enter 1 or 2: ").strip()

# ---------------------------------------------------------------- INPUT
if choice == "1":
    names = ["Aarav", "Bhavya", "Charan", "Divya", "Eshwar", "Farhan"]
    subjects = ["Maths", "Physics", "Chemistry", "English", "Python"]
    marks = [
        [78, 65, 70, 82, 90],
        [92, 88, 85, 79, 95],
        [45, 38, 52, 60, 55],
        [92, 70, 66, 74, 88],
        [35, 42, 30, 58, 47],
        [60, 55, 48, 66, 72],
    ]
else:
    text = input("Number of students: ").strip()
    while not text.isdigit() or int(text) < 1:
        text = input("Enter a positive whole number: ").strip()
    n = int(text)

    text = input("Number of subjects: ").strip()
    while not text.isdigit() or int(text) < 1:
        text = input("Enter a positive whole number: ").strip()
    m = int(text)

    subjects = []
    for j in range(m):
        s = input("Name of subject " + str(j + 1) + ": ").strip()
        while s == "":
            s = input("Subject name cannot be empty: ").strip()
        subjects.append(s)

    names = []
    marks = []
    for i in range(n):
        s = input("Name of student " + str(i + 1) + ": ").strip()
        while s == "":
            s = input("Student name cannot be empty: ").strip()
        names.append(s)
        row = []
        for j in range(m):
            t = input("  " + s + " - " + subjects[j] + " marks: ").strip()
            while not t.isdigit() or int(t) > MAX_MARKS:
                t = input("  Invalid. Enter 0-" + str(MAX_MARKS) + ": ").strip()
            row.append(int(t))
        marks.append(row)

rows = len(names)
cols = len(subjects)

# ------------------------------------------------- ROW-WISE STATISTICS
totals = []
averages = []
highest = []
lowest = []
for i in range(rows):
    t = 0
    hi = marks[i][0]
    lo = marks[i][0]
    for j in range(cols):
        t = t + marks[i][j]
        if marks[i][j] > hi:
            hi = marks[i][j]
        if marks[i][j] < lo:
            lo = marks[i][j]
    totals.append(t)
    averages.append(t / cols)
    highest.append(hi)
    lowest.append(lo)

# ---------------------------------------------- COLUMN-WISE STATISTICS
col_totals = []
col_avgs = []
col_highest = []
col_lowest = []
fail_counts = []
for j in range(cols):
    t = 0
    hi = marks[0][j]
    lo = marks[0][j]
    fails = 0
    for i in range(rows):
        t = t + marks[i][j]
        if marks[i][j] > hi:
            hi = marks[i][j]
        if marks[i][j] < lo:
            lo = marks[i][j]
        if marks[i][j] < PASS_MARK:
            fails = fails + 1
    col_totals.append(t)
    col_avgs.append(t / rows)
    col_highest.append(hi)
    col_lowest.append(lo)
    fail_counts.append(fails)

# ------------------------------------------------------------- RANKS
# rank = 1 + number of students with a strictly higher total (ties share rank)
ranks = []
for i in range(rows):
    r = 1
    for k in range(rows):
        if totals[k] > totals[i]:
            r = r + 1
    ranks.append(r)

# =============================================================== OUTPUT
width = 24 + 11 * cols + 24

print()
print("MARKS MATRIX WITH ROW-WISE STATISTICS")
print("-" * width)
line = "Student".ljust(12)
for j in range(cols):
    line = line + subjects[j][:9].rjust(10)
line = line + "Total".rjust(8) + "Avg".rjust(8) + "High".rjust(6) + "Low".rjust(5) + "Rank".rjust(6)
print(line)
print("-" * width)
for i in range(rows):
    line = names[i][:11].ljust(12)
    for j in range(cols):
        line = line + str(marks[i][j]).rjust(10)
    line = (line + str(totals[i]).rjust(8) + f"{averages[i]:.2f}".rjust(8)
            + str(highest[i]).rjust(6) + str(lowest[i]).rjust(5) + str(ranks[i]).rjust(6))
    print(line)
print("-" * width)

print()
print("COLUMN-WISE (SUBJECT) STATISTICS")
print("-" * 66)
print("Subject".ljust(12) + "Total".rjust(8) + "Average".rjust(10)
      + "High".rjust(7) + "Low".rjust(6) + "Fails".rjust(7))
print("-" * 66)
for j in range(cols):
    print(subjects[j][:11].ljust(12) + str(col_totals[j]).rjust(8)
          + f"{col_avgs[j]:.2f}".rjust(10) + str(col_highest[j]).rjust(7)
          + str(col_lowest[j]).rjust(6) + str(fail_counts[j]).rjust(7))
print("-" * 66)

# ------------------------------------------------------ TOP PERFORMERS
best_total = totals[0]
for i in range(rows):
    if totals[i] > best_total:
        best_total = totals[i]

print()
print("TOP PERFORMER(S) OVERALL (highest total = " + str(best_total) + ")")
for i in range(rows):
    if totals[i] == best_total:
        print("  * " + names[i] + "  (Average: " + f"{averages[i]:.2f}" + ")")

print()
print("SUBJECT-WISE TOPPERS")
for j in range(cols):
    toppers = ""
    for i in range(rows):
        if marks[i][j] == col_highest[j]:
            if toppers != "":
                toppers = toppers + ", "
            toppers = toppers + names[i]
    print("  " + subjects[j].ljust(11) + ": " + toppers + " (" + str(col_highest[j]) + ")")

# --------------------------------------------- LOW-PERFORMING SUBJECTS
print()
print("SUBJECTS WITH LOW AVERAGE PERFORMANCE (average < " + str(LOW_AVG_LIMIT) + ")")
found = False
for j in range(cols):
    if col_avgs[j] < LOW_AVG_LIMIT:
        print("  ! " + subjects[j] + " -> average " + f"{col_avgs[j]:.2f}")
        found = True
if not found:
    print("  None. All subject averages are at or above " + str(LOW_AVG_LIMIT) + ".")

# weakest subject overall
weak = 0
for j in range(cols):
    if col_avgs[j] < col_avgs[weak]:
        weak = j
print()
print("Weakest subject overall : " + subjects[weak] + " (" + f"{col_avgs[weak]:.2f}" + ")")

# ---------------------------------------------- STUDENTS WITH FAILURES
print()
print("STUDENTS WITH SUBJECT FAILURES (marks < " + str(PASS_MARK) + ")")
any_fail = False
for i in range(rows):
    failed = ""
    for j in range(cols):
        if marks[i][j] < PASS_MARK:
            if failed != "":
                failed = failed + ", "
            failed = failed + subjects[j]
    if failed != "":
        print("  - " + names[i] + ": " + failed)
        any_fail = True
if not any_fail:
    print("  None. All students passed every subject.")
print("=" * 66)
