import pandas as pd

# Load the CSV file
file_path = "data.csv"  # Update this to your actual CSV file path
print(f"Loading file: {file_path}")

df = pd.read_csv(file_path)  # Load CSV directly

# Convert CreatedDate to datetime format
df["CreatedDate"] = pd.to_datetime(df["CreatedDate"])

# Sort the data by IDNumber and CreatedDate in descending order
df_sorted = df.sort_values(by=["IDNumber", "CreatedDate"], ascending=[True, False])

# Compute time difference (in minutes) between each row and the previous one within the same IDNumber
df_sorted["TimeDifferenceMinutes"] = df_sorted.groupby("IDNumber")["CreatedDate"].diff(periods=-1).dt.total_seconds() / 60

# Save the processed DataFrame to a new CSV file
output_file_path = "batch_time_difference.csv"  # Change this as needed
df_sorted.to_csv(output_file_path, index=False)

print(f"File saved as {output_file_path}")
