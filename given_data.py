# given_data.py
import numpy as np
import pandas as pd

# Load data from CSV file
data_file = 'Assignment3Data.csv'  # Ensure the CSV file is in the same directory
df = pd.read_csv(data_file)

# Remove unnecessary columns
df = df[['School Year', 'School Name', 'School Code', 'Grade 10', 'Grade 11', 'Grade 12']]

# Extract unique years from the DataFrame
years = df['School Year'].unique()

# Create a dictionary to hold enrollment data for each year
enrollment_data = {year: df[df['School Year'] == year].iloc[:, 3:].values for year in years}

# Create a list for each year
year_2013 = enrollment_data[2013]
year_2014 = enrollment_data[2014]
year_2015 = enrollment_data[2015]
year_2016 = enrollment_data[2016]
year_2017 = enrollment_data[2017]
year_2018 = enrollment_data[2018]
year_2019 = enrollment_data[2019]
year_2020 = enrollment_data[2020]
year_2021 = enrollment_data[2021]
year_2022 = enrollment_data[2022]
