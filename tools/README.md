# Wilayah Kodepos Tools

This directory contains utility scripts to process, convert, and manage the Indonesian administrative division and postal code datasets.

## 🛠️ Scripts

### 1. `sql_to_json.py`
This script parses the primary MySQL database dump of the mappings and exports it into JSON formats for application use.

* **Source File:** `db/wilayah_kodepos.sql` (based on Kepmendagri No 300.2.2-2138 Tahun 2025)
* **Outputs Created:**
  * `json/wilayah_kodepos.json` - Pretty-printed, indented JSON mapping database entries.
  * `json/wilayah_kodepos.min.json` - Minified JSON object designed for fast browser and backend ingestion.
* **Format:**
  ```json
  {
    "11.01.01.2001": "23773",
    "11.01.01.2002": "23773"
  }
  ```

#### Usage
Run the script using Python 3:
```bash
python tools/sql_to_json.py
```

### 2. `validate_sql.py`
This script checks the formatting and syntax of `db/wilayah_kodepos.sql` to prevent parsing or import errors.

* **Checks Performed:**
  * Validates that standard administrative codes format (`xx.xx.xx.xxxx`) matches expected standard syntax.
  * Verifies primary table structure definition existence (`CREATE TABLE wilayah_kodepos`).
  * Assures database loading optimizations are in place (`START TRANSACTION`, `COMMIT`, `DISABLE KEYS`, `ENABLE KEYS`).

#### Usage
Run the validation script using Python 3:
```bash
python tools/validate_sql.py
```
