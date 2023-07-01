def excel_to_csv(input_file, output_file):
    # Read the Excel file into a DataFrame
    df = pd.read_excel(input_file)

    # Convert DataFrame to CSV
    df.to_csv(output_file, index=False)

# Replace 'input_file.xlsx' and 'output_file.csv' with your actual file names
input_file = './Excel_sheets/' + sys.argv[1] + '.xlsx'
output_file = './csv_files/'+ sys.argv[1] + '.csv'

excel_to_csv(input_file, output_file)