import os
import re

def validate_sql_syntax():
    sql_file_path = os.path.join('db', 'wilayah_kodepos.sql')
    
    print(f"Validating SQL file syntax: {sql_file_path}")
    if not os.path.exists(sql_file_path):
        print(f"Error: SQL file not found at {sql_file_path}")
        return False

    errors = []
    
    # Flags to verify essential blocks
    has_create_table = False
    has_disable_keys = False
    has_enable_keys = False
    has_start_transaction = False
    has_commit = False
    
    # We want to check matching parens and quotes for the values block
    in_values_block = False
    row_count = 0
    
    # Regex to match values block items: ('11.01.01.2001', '23773') followed by a comma or a semicolon
    row_pattern = re.compile(r"^\(\s*['\"]([\d\.]+)['\"]\s*,\s*['\"](\d{5})['\"]\s*\)([,;])$")

    with open(sql_file_path, 'r', encoding='utf-8') as f:
        for idx, line in enumerate(f, 1):
            line_str = line.strip()
            
            # 1. Structural Checks
            if "CREATE TABLE wilayah_kodepos" in line_str:
                has_create_table = True
            elif "DISABLE KEYS" in line_str:
                has_disable_keys = True
            elif "ENABLE KEYS" in line_str:
                has_enable_keys = True
            elif "START TRANSACTION" in line_str:
                has_start_transaction = True
            elif "COMMIT;" in line_str:
                has_commit = True
            
            # 2. Values Insert Validation
            if line_str.startswith("INSERT INTO wilayah_kodepos"):
                in_values_block = True
                continue
            
            if in_values_block:
                if line_str.upper().startswith("VALUES"):
                    continue
                
                # Check formatting of the insert rows
                match = row_pattern.match(line_str)
                if match:
                    row_count += 1
                    delimiter = match.group(3)
                    
                    # Validate administrative code structure
                    code = match.group(1)
                    if not re.match(r"^\d{2}\.\d{2}\.\d{2}\.\d{4}$", code):
                        errors.append(f"Line {idx}: Invalid administrative code format '{code}'. Expected format: xx.xx.xx.xxxx")
                    
                    if delimiter == ';':
                        # Semicolon marks the end of the values block
                        in_values_block = False
                elif line_str == "":
                    continue
                else:
                    errors.append(f"Line {idx}: Unexpected syntax or malformed row inside INSERT block: {line_str}")
                    # Safety break to avoid cascading errors if format is completely off
                    if len(errors) > 10:
                        errors.append("Too many syntax errors inside INSERT block. Stopping validation.")
                        break

    # 3. Final structural verifications
    if not has_create_table:
        errors.append("Missing CREATE TABLE wilayah_kodepos statement.")
    if not has_start_transaction:
        errors.append("Missing START TRANSACTION; statement (import speed optimization).")
    if not has_commit:
        errors.append("Missing COMMIT; statement.")
    if not has_disable_keys:
        errors.append("Missing DISABLE KEYS statement (import speed optimization).")
    if not has_enable_keys:
        errors.append("Missing ENABLE KEYS statement.")

    # Output results
    if errors:
        print("\n[ERROR] Validation Failed! Syntax errors or missing optimizations found:")
        for err in errors:
            print(f"- {err}")
        return False
    else:
        print(f"\n[OK] Validation Succeeded! Successfully verified {row_count} data rows.")
        print("- Table definition checks passed.")
        print("- All bulk transaction optimizations (TRANSACTION, DISABLE/ENABLE KEYS) verified.")
        return True

if __name__ == '__main__':
    validate_sql_syntax()
