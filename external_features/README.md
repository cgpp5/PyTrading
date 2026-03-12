Place the daily CSV files for the McClellan features in this folder.

Expected files:
- McClellanOsc.csv
- McClellanSumOsc.csv

Expected format:

Date,Value
2007.09.28,37.70000000
2007.09.29,63.46500000

The loader also accepts the same two-column shape with standard CSV parsing.

Optional override:
- Set FEATURE_ENGINE_EXTERNAL_CSV_DIR to point somewhere else.