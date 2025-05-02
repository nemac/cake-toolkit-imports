import csv
import sys

def filter_cake_export(selected_case_studies_file, export_file, output_file):
    # Read the selected case studies to get the titles (only where CRT Status = "Selected")
    selected_titles = set()
    try:
        with open(selected_case_studies_file, 'r', newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                if ('CRT Status' in row and row['CRT Status'] == 'Selected' and 
                    'CAKE Resource Title' in row and row['CAKE Resource Title']):
                    selected_titles.add(row['CAKE Resource Title'])
    except Exception as e:
        print(f"Error reading selected case studies file: {e}")
        sys.exit(1)
    
    # Print the number of selected titles found for debugging
    print(f"Found {len(selected_titles)} titles with CRT Status = 'Selected'")
    
    # Read the export file and filter rows with matching titles
    filtered_rows = []
    try:
        with open(export_file, 'r', newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            headers = reader.fieldnames
            for row in reader:
                if 'title' in row and row['title'] in selected_titles:
                    filtered_rows.append(row)
    except Exception as e:
        print(f"Error reading export file: {e}")
        sys.exit(1)
    
    # Write the filtered rows to the output file
    try:
        with open(output_file, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=headers)
            writer.writeheader()
            writer.writerows(filtered_rows)
        print(f"Successfully created {output_file} with {len(filtered_rows)} matching entries")
    except Exception as e:
        print(f"Error writing to output file: {e}")
        sys.exit(1)

if __name__ == "__main__":
    # Check command line arguments
    if len(sys.argv) != 4:
        print("Usage: python3 filter.py cake_selected_case_studies.csv cake_export.csv cake_case_studies_to_import.csv")
        sys.exit(1)
    
    selected_case_studies_file = sys.argv[1]
    export_file = sys.argv[2]
    output_file = sys.argv[3]
    
    filter_cake_export(selected_case_studies_file, export_file, output_file)
