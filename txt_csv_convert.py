import pandas as pd

with open("output1.txt", "r") as file:
    lines = [line.strip() for line in file]

# Create a DataFrame without column name
df = pd.DataFrame(lines)

# Save as CSV without index and without header
df.to_csv("submission.csv", index=False, header=False)
