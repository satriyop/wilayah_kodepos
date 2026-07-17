import os
import re
import json

def convert_sql_to_json():
    sql_file_path = os.path.join('db', 'wilayah_kodepos.sql')
    output_dir = 'json'
    
    # Ensure output directory exists
    os.makedirs(output_dir, exist_ok=True)
    
    # Regular expression to match SQL INSERT row pattern: ('11.01.01.2001', '23773')
    # It allows for spaces, single quotes, or double quotes, and matches valid codes/postal codes.
    row_pattern = re.compile(r"\(\s*['\"]([\d\.]+)['\"]\s*,\s*['\"](\d{5})['\"]\s*\)")
    
    data = {}
    
    print(f"Reading SQL file from: {sql_file_path}")
    if not os.path.exists(sql_file_path):
        print(f"Error: SQL file not found at {sql_file_path}")
        return

    with open(sql_file_path, 'r', encoding='utf-8') as f:
        for line in f:
            # We are only interested in line parts that might contain the data records
            # Standard row starts with '(' and ends with ')' followed by comma or semicolon
            line = line.strip()
            if not line.startswith('('):
                continue
            
            matches = row_pattern.findall(line)
            for code, kodepos in matches:
                data[code] = kodepos
                
    total_records = len(data)
    print(f"Successfully parsed {total_records} records.")
    
    # Save combined data to wilayah_kodepos.json
    combined_json_path = os.path.join(output_dir, 'wilayah_kodepos.json')
    with open(combined_json_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f"Saved combined JSON to: {combined_json_path}")
    
    # Save a minified version as well
    minified_json_path = os.path.join(output_dir, 'wilayah_kodepos.min.json')
    with open(minified_json_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, separators=(',', ':'))
    print(f"Saved minified JSON to: {minified_json_path}")

if __name__ == '__main__':
    convert_sql_to_json()
