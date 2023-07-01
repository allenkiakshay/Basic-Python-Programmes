import pandas as pd
import math

def split_excel_rows(input_file, rows_per_file):
    # Read the Excel data into a pandas DataFrame
    df = pd.read_excel(input_file, engine='openpyxl')

    # Calculate the number of files needed
    total_rows = len(df)
    total_files = math.ceil(total_rows / rows_per_file)

    # Split the data into chunks based on the specified number of rows
    data_chunks = [df[i:i + rows_per_file] for i in range(0, total_rows, rows_per_file)]

    # Create separate Excel files for each data chunk
    for i, chunk in enumerate(data_chunks):
        output_file = f"./youtube_urls_split/file_{i+1}.xlsx"  # Set the output file name
        chunk.to_excel(output_file, index=False, engine='openpyxl')

    print(f"Splitting completed successfully. Total {total_files} files created.")

# Replace 'input.xlsx' with the path to your input Excel file
input_file_path = 'youtube_urls.xlsx'

# Set the desired number of rows per file
rows_per_output_file = 100

split_excel_rows(input_file_path, rows_per_output_file)
