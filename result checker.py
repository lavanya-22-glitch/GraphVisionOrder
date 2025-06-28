with open("submission.csv") as f1, open("output1.txt") as f2:
    list1 = [line.strip() for line in f1]
    list2 = [line.strip() for line in f2]

if list1 == list2:
    print("✅ The lists are identical.")
else:
    print("❌ The lists are different!")
    for i, (a, b) in enumerate(zip(list1, list2)):
        if a != b:
            print(f"Line {i+1} is different: {a} ≠ {b}")