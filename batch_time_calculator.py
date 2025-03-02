import pandas as pd

# Load the Excel file
file_path = "data.xlsx"  # Update this to your actual file path
print(f"Loading file: {file_path}")
xls = pd.ExcelFile(file_path)

# Load the sheet into a DataFrame
df = pd.read_excel(xls, sheet_name="Sheet1")

# Convert CreatedDate to datetime format
df["CreatedDate"] = pd.to_datetime(df["CreatedDate"])

# Sort the data by IDNumber and CreatedDate in descending order
df_sorted = df.sort_values(by=["IDNumber", "CreatedDate"], ascending=[True, False])

# Compute time difference (in minutes) between each row and the previous one within the same IDNumber
df_sorted["TimeDifferenceMinutes"] = df_sorted.groupby("IDNumber")["CreatedDate"].diff(periods=-1).dt.total_seconds() / 60

# Save the processed DataFrame to an Excel file
output_file_path = "batch_time_difference.xlsx"  # Change this as needed
df_sorted.to_excel(output_file_path, index=False)

print(f"File saved as {output_file_path}")
