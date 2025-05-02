import csv
import sys
import re

def update_taxonomy_ids(input_file, output_file):
    # Maps taxonomy IDs for the Toolkit and CAKE case studies
    # key: value = CAKE: Toolkit
    taxonomy_mappings = {
        7311: 56,
        7316: 57,
        7321: 59,
        7326: 60,
        7041: 68,
        7301: 71,
        7346: 69,
        7111: 71,
        7306: 71,
        7161: 63,
        7006: 64,
        7291: "70|71",
        7131: 63,
        6996: 67,
        7201: "62|128",
        7081: 66,
        7026: 70,
        479: 166,
        7226: 171,
        483: 171,
        7231: 172,
        486: 173,
        488: 174,
        492: 175,
        490: 176,
        487: 177,
        480: 177,
        481: 179,
        496: 180,
        494: 181,
        497: 182,
        525: 134,
        7392: 131,
        520: 135,
        541: "135|138",
        542: "136|144",
        7221: 137,
        548: 137,
        515: 137,
        523: 139,
        536: 139,
        544: 140,
        526: 145,
        539: 145,
        535: 145,
        518: 146,
        528: 146,
        521: 148,
        519: 151,
        545: 151,
        516: 154,
        522: 154,
        543: 154,
        537: 155,
        538: 155,
        546: "160|162",
        547: 161,
        517: 165,
    }

    # Convert all keys to strings for easier matching
    string_mappings = {str(k): str(v) for k, v in taxonomy_mappings.items()}
    
    # Columns to update
    columns_to_update = [
        'field_adaptation_phase',
        'field_econ_sector',
        'field_target_impacts'
    ]
    
    rows_processed = 0
    fields_updated = 0
    
    try:
        # Read the input file
        with open(input_file, 'r', newline='', encoding='utf-8') as infile:
            reader = csv.DictReader(infile)
            headers = reader.fieldnames
            
            # Check if target columns exist
            missing_columns = [col for col in columns_to_update if col not in headers]
            if missing_columns:
                print(f"Warning: These columns are missing from the input file: {missing_columns}")
                columns_to_update = [col for col in columns_to_update if col in headers]
            
            rows = list(reader)
        
        # Process each row
        for row in rows:
            rows_processed += 1
            for column in columns_to_update:
                if column in row and row[column]:
                    original_value = row[column]
                    new_value = original_value
                    
                    # Look for integers or numbers that match our keys
                    for old_id, new_id in string_mappings.items():
                        # Use regex to match standalone numbers
                        # This pattern matches the number when it's surrounded by non-digits
                        pattern = r'(?<!\d)' + re.escape(old_id) + r'(?!\d)'
                        if re.search(pattern, new_value):
                            new_value = re.sub(pattern, new_id, new_value)
                            fields_updated += 1
                    
                    row[column] = new_value
        
        # Write to output file
        with open(output_file, 'w', newline='', encoding='utf-8') as outfile:
            writer = csv.DictWriter(outfile, fieldnames=headers)
            writer.writeheader()
            writer.writerows(rows)
            
        print(f"Processing complete! {rows_processed} rows processed, {fields_updated} fields updated.")
        print(f"Updated file saved as: {output_file}")
            
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python taxonomy_mapping.py input_file.csv output_file.csv")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    
    update_taxonomy_ids(input_file, output_file)
