from datetime import datetime
import pandas as pd

class DataProcessor:
    @staticmethod
    def transform_data(df: pd.DataFrame) -> pd.DataFrame:
        # Convert dates
        df['Open_Date'] = pd.to_datetime(df['Open_Date'], format='%Y%m%d')
        df['Last_Consulted_Date'] = pd.to_datetime(df['Last_Consulted_Date'], format='%Y%m%d')
        df['DOB'] = pd.to_datetime(df['DOB'], format='%d%m%Y')

        # Add derived columns
        df['Age'] = df['DOB'].apply(lambda x: (datetime.now() - x).days // 365)
        df['Days_Since_Last_Consulted'] = (datetime.now() - df['Last_Consulted_Date']).dt.days
        return df

    @staticmethod
    def split_by_country(df: pd.DataFrame) -> dict:
        return {country: group for country, group in df.groupby('Country')}

    @staticmethod
    def export_country_data(country_data: dict, output_dir: str):
        for country, data in country_data.items():
            file_path = f"{output_dir}/Table_{country}.csv"
            data.to_csv(file_path, index=False)
