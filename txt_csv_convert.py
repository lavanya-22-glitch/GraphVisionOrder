import pandas as pd

# ===== Configuration =====
input_txt = "output1.txt"
output_csv = "submission.csv"
delimiter = ","

# ===== TXT to CSV Conversion =====
def txt_to_csv(input_txt, output_csv, delimiter=","):
    df = pd.read_csv(input_txt, delimiter=delimiter, header=None)
    df.to_csv(output_csv, index=False)
    print(f"✅ Successfully converted '{input_txt}' to '{output_csv}'")

# ===== Run =====
txt_to_csv(input_txt, output_csv, delimiter)
