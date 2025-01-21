from src.file_parser import FileParser
from src.data_processor import DataProcessor
import os

def main():
    # File path
    input_file = "data/sample_input.txt"
    output_dir = "data"

    # Parse the file
    parser = FileParser(input_file)
    raw_data = parser.parse_file()

    # Process the data
    processor = DataProcessor()
    transformed_data = processor.transform_data(raw_data)

    # Split by country
    country_data = processor.split_by_country(transformed_data)

    # Export data
    processor.export_country_data(country_data, output_dir)
    print("Data processed and exported successfully!")

if __name__ == "__main__":
    main()
