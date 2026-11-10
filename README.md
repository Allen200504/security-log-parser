# Security Log Parser

A Python script that counts failed logins by username from `sample_logs.csv`.
The sample data is synthetic. The script uses Python 3 and its standard library.

## Run on Windows

Open PowerShell in the project folder and run:

```powershell
py .\parser.py
```

The sample should show three failed logins, with two for `alice` and one for `bob`.

## Run the tests

```powershell
py -m unittest -v
```

The five tests cover the sample counts, successful logins only, a header-only
file, a missing result column, and an invalid login result.
