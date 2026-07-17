# wilayah_kodepos
Kodepos berdasarkan kode wilayah Indonesia Kepmendagri No 300.2.2-2138 Tahun 2025   
Data wilayah sesuai Kepmendagri No 300.2.2-2138 Tahun 2025 bisa di dapat di tautan https://github.com/cahyadsn/wilayah 

[![GitHub license](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![GitHub issues](https://img.shields.io/github/issues/cahyadsn/wilayah_kodepos.svg)](https://github.com/cahyadsn/wilayah_kodepos/issues)
[![GitHub forks](https://img.shields.io/github/forks/cahyadsn/wilayah_kodepos.svg)](https://github.com/cahyadsn/wilayah_kodepos/network)
[![GitHub stars](https://img.shields.io/github/stars/cahyadsn/wilayah_kodepos.svg)](https://github.com/cahyadsn/wilayah_kodepos/stargazers)
[![GitHub last commit](https://img.shields.io/github/last-commit/google/skia.svg?style=flat)]()
[![Donate](https://img.shields.io/badge/$-support-ff69b4.svg?style=flat)](https://paypal.me/cahyadwiana)

![screenshot](https://github.com/cahyadsn/wilayah_kodepos/blob/main/img/apps.png?raw=true)

## TAUTAN TERKAIT
- Data kode wilayah administrasi pemerintahan Indonesia : https://github.com/cahyadsn/wilayah
- Data referensi Kode dan Data Wilayah Administrasi Pemerintahan dan Pulau Indonesia : https://github.com/cahyadsn/wilayah_ref
- Data boundaries/polygon berdasarkan kode wilayah administrasi pemerintahan Indonesia : https://github.com/cahyadsn/wilayah_boundaries
- Data logo/lambang berdasarkan kode wilayah administrasi pemerintahan Indonesia (prov,kab/kota) : https://github.com/cahyadsn/wilayah_logo


## DATA
Data wilayah vs kodepos ada di `db/wilayah_kodepos.sql`, mencakup data kodepos **83.762 desa/kelurahan (level 4)** di seluruh Indonesia.

| File | Keterangan |
|------|-----------|
| `db/wilayah_kodepos.sql` | Data kodepos terkini, sesuai Kepmendagri No 300.2.2-2138 Tahun 2025 |
| `db/archive/wilayah_kodepos_2023.sql` | Data kodepos lama, sesuai Kepmendagri No 100.1.1-6117 Tahun 2022 |
| `src/pos-data.csv` | Data sumber kodepos dalam format CSV |
| `json/wilayah_kodepos.json` | Mappings hasil konversi dalam format JSON |
| `json/wilayah_kodepos.min.json` | Mappings hasil konversi dalam format minified JSON |
| `tools/sql_to_json.py` | Skrip Python untuk konversi data SQL ke JSON |
| `tools/README.md` | Panduan penggunaan skrip pendukung |


## STRUKTUR DATABASE

```sql
CREATE TABLE wilayah_kodepos (
  kode     varchar(13) NOT NULL,   -- kode wilayah (format: xx.xx.xx.xxxx)
  kodepos  varchar(5)  DEFAULT NULL, -- kode pos 5 digit
  PRIMARY KEY (kode)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
```

Kolom `kode` menggunakan format kode wilayah level 4 (desa/kelurahan) sesuai Kepmendagri, contoh:
- `11.01.01.2001` → Provinsi `11`, Kabupaten/Kota `11.01`, Kecamatan `11.01.01`, Desa/Kelurahan `11.01.01.2001`


## PENGGUNAAN / IMPORT

File SQL sudah dioptimasi untuk import yang cepat. Gunakan salah satu cara berikut:

**Via command line (direkomendasikan):**
```bash
mysql -u root -p nama_database < db/wilayah_kodepos.sql
```

**Via MySQL Workbench / phpMyAdmin:**  
Import file `db/wilayah_kodepos.sql` langsung ke database yang diinginkan.

**Contoh query setelah import:**
```sql
-- Cari kodepos berdasarkan kode wilayah
SELECT kode, kodepos FROM wilayah_kodepos WHERE kode = '11.01.02.2001';

-- Cari semua desa/kelurahan dalam satu kecamatan beserta kodeposnya
SELECT kode, kodepos FROM wilayah_kodepos WHERE kode LIKE '11.01.02.%';

-- Join dengan tabel wilayah (dari repo wilayah)
SELECT w.nama, wk.kodepos
FROM wilayah w
JOIN wilayah_kodepos wk ON w.kode = wk.kode
WHERE wk.kodepos = '23771';
```

> **Catatan:** File SQL menggunakan `START TRANSACTION` / `COMMIT`, `DISABLE KEYS`, dan batch insert 1.000 baris per statement untuk mempercepat proses import secara signifikan.


## ARCHIVE
- `db/archive/wilayah_kodepos_2023.sql` — data kodepos vs kode wilayah sesuai Kepmendagri No 100.1.1-6117 Tahun 2022


## CHANGE LOG
- [2026-07-17] Menambahkan skrip python `tools/sql_to_json.py` untuk konversi data SQL ke JSON dan `tools/README.md`
- [2026-07-13] optimasi file SQL: batch insert 1.000 baris, `START TRANSACTION/COMMIT`, `DISABLE/ENABLE KEYS`, `ENGINE=InnoDB`, `utf8mb4`
- [2026-02-16] menambahkan tautan terkait
- [2025-11-12] update README.md
- [2025-06-30] update data kode wilayah sesuai Kepmendagri No 300.2.2-2138 Tahun 2025
- [2025-05-28] update kodepos untuk desa-desa di kecamatan Wlingi (66184) dan Garum (66181)
- [2025-04-xx] update kodepos untuk desa-desa di kecamatan Sungai Kakap (78381), Kab. Kubu Raya, Prov. Kalimantan Barat


## TODO
- Menambahkan data kodepos per pulau di Indonesia, kode pulau vs kodepos
- Verifikasi dan validasi kelengkapan data

## DONATION
- untuk donasi via transfer
    - Bank Jago (542) 5003 5796 1022
    - Bank BCA Digital (Blu) (501) 000 576 776 186
    - Bank Sinarmas (153) 005 462 4719
    - Bank Syariah Indonesia (BSI) 821-342-5550
- untuk donasi via PayPal : [https://paypal.me/cahyadwiana](https://paypal.me/cahyadwiana)
- untuk donasi via QRIS CAHYADSN ID1022183125288 :

![QRIS](https://github.com/cahyadsn/wilayah/blob/master/docs/qr_code.cahyadsn.png?raw=true 'Donasi via QRIS CAHYADSN')


## CONTACT
- facebook : [https://m.facebook.com/cahya.dsn](https://m.facebook.com/cahya.dsn)
- email : [cahyadsn@gmail.com](mailto:cahyadsn@gmail.com)
- source code : [https://github.com/cahyadsn/wilayah_kodepos](https://github.com/cahyadsn/wilayah_kodepos)
