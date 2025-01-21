import pandas as pd

class FileParser:
    def __init__(self, file_path: str):
        self.file_path = file_path

    def parse_file(self) -> pd.DataFrame:
        try:
            # Read the file
            data = []
            with open(self.file_path, 'r') as file:
                for line in file:
                    if line.startswith("|D|"):
                        data.append(line.strip("|").split("|")[1:])
            # Create DataFrame
            columns = ['Customer_Name', 'Customer_ID', 'Open_Date', 'Last_Consulted_Date',
                       'Vaccination_Id', 'Dr_Name', 'State', 'Country', 'DOB', 'Is_Active']
            df = pd.DataFrame(data, columns=columns)
            return df
        except Exception as e:
            raise ValueError(f"Error parsing file: {e}")
