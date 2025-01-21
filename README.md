# Assesment

# Multi-Specialty Hospital Data Processor

This project processes patient data for a global hospital chain, splitting records by country and exporting them for further use. It ensures data transformation, validation, and efficient handling of large datasets.

---

## Features
1. **File Parsing**: Reads input files and converts them into structured data.
2. **Data Transformation**: Adds derived columns:
   - `Age`: Calculated from Date of Birth.
   - `Days Since Last Consulted`: Days since the last consultation date.
3. **Country-Based Splitting**: Separates data into country-specific files.
4. **Export**: Saves processed data as CSV files for each country.

---

## Project Structure
```plaintext
project/
├── src/
│   ├── main.py                 # Entry point script
│   ├── file_parser.py          # Handles file parsing
│   ├── data_processor.py       # Data transformation and processing
├── tests/
│   ├── test_file_parser.py     # Unit tests for file parsing
│   ├── test_data_processor.py  # Unit tests for data processing
├── data/
│   ├── sample_input.txt        # Sample input file
│   ├── Table_USA.csv           # Example output for USA
│   ├── Table_IND.csv           # Example output for India
├── README.md                   # Project documentation
├── requirements.txt            # Python dependencies
├── .gitignore                  # Ignore unnecessary files
