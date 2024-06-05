# school_data.py
# AUTHOR NAME
#
# A terminal-based application for computing and printing statistics based on given input.
# You must include the main listed below. You may add your own additional classes, functions, variables, etc. 
# You may import any modules from the standard Python library.
# Remember to include docstrings and comments.

import numpy as np
import pandas as pd
from given_data import year_2013, year_2014, year_2015, year_2016, year_2017, year_2018, year_2019, year_2020, year_2021, year_2022

# Load the CSV to get school names and codes
data_file = 'Assignment3Data.csv'  # Ensure the CSV file is in the same directory
df = pd.read_csv(data_file)

# Remove unnecessary columns
df = df[['School Year', 'School Name', 'School Code', 'Grade 10', 'Grade 11', 'Grade 12']]

# Replace NaN values with 0 in the 2021 and 2022 data
year_2021 = np.nan_to_num(year_2021, nan=0)
year_2022 = np.nan_to_num(year_2022, nan=0)

# Create a 3D array for enrollment data with shape (10 years, 20 schools, 3 grades)
enrollment_data = np.array([
    year_2013, year_2014, year_2015, year_2016, year_2017, 
    year_2018, year_2019, year_2020, year_2021, year_2022
]).reshape(10, 20, 3)

# Create a dictionary to map school codes to school names
school_dict = df.set_index('School Code')['School Name'].to_dict()

def get_school_code_index(school_input):
    """
    Returns the index of the school based on user input (name or code).
    
    Parameters:
    school_input (str): The school name or code entered by the user
    
    Returns:
    int: Index of the school in the enrollment data
    """
    try:
        # Try to convert the input to an integer (school code)
        school_code = int(school_input)
        if school_code in school_dict:
            # Find the index of the school code in the dictionary
            school_index = list(school_dict.keys()).index(school_code)
            return school_index
        else:
            raise ValueError
    except ValueError:
        # If input is not a valid code, check if it matches a school name
        for code, name in school_dict.items():
            if name.lower() == school_input.lower():
                school_index = list(school_dict.keys()).index(code)
                return school_index
        # Raise an error if the input is neither a valid school code nor a name
        raise ValueError("You must enter a valid school name or code.")

def print_school_stats(school_index):
    """
    Prints statistics for a specific school based on its index.
    
    Parameters:
    school_index (int): Index of the school in the enrollment data
    """
    # Get the school code and name based on the index
    school_code = list(school_dict.keys())[school_index]
    school_name = school_dict[school_code]
    # Get the data for the specific school across all years and grades
    school_data = enrollment_data[:, school_index, :]
    
    print(f"School Name: {school_name}")
    print(f"School Code: {school_code}")
    
    # Calculate mean enrollment for each grade across all years
    mean_grade_10 = np.mean(school_data[:, 0])
    mean_grade_11 = np.mean(school_data[:, 1])
    mean_grade_12 = np.mean(school_data[:, 2])
    # Find the highest and lowest enrollment numbers
    highest_enrollment = np.max(school_data)
    lowest_enrollment = np.min(school_data)
    # Calculate total enrollment for each year
    total_yearly_enrollment = np.sum(school_data, axis=1)
    # Calculate total enrollment over ten years and mean yearly enrollment
    total_ten_year_enrollment = np.sum(total_yearly_enrollment)
    mean_total_yearly_enrollment = np.mean(total_yearly_enrollment)
    
    # Find enrollments over 500
    enrollments_over_500 = school_data[school_data > 500]
    
    # Print calculated statistics
    print(f"Mean enrollment for Grade 10 across all years: {int(mean_grade_10)}")
    print(f"Mean enrollment for Grade 11 across all years: {int(mean_grade_11)}")
    print(f"Mean enrollment for Grade 12 across all years: {int(mean_grade_12)}")
    print(f"Highest enrollment for a single grade within the entire time period: {int(highest_enrollment)}")
    print(f"Lowest enrollment for a single grade within the entire time period: {int(lowest_enrollment)}")
    
    for year, total in enumerate(total_yearly_enrollment, 2013):
        print(f"Total enrollment for {year}: {int(total)}")
    
    print(f"Total ten-year enrollment: {int(total_ten_year_enrollment)}")
    print(f"Mean total yearly enrollment over 10 years: {int(mean_total_yearly_enrollment)}")
    
    # Print median of enrollments over 500 or a message if none exist
    if enrollments_over_500.size > 0:
        median_over_500 = np.median(enrollments_over_500)
        print(f"Median enrollment value for enrollments over 500: {int(median_over_500)}")
    else:
        print("No enrollments over 500.")

def print_general_stats():
    """
    Prints general statistics for all schools.
    """
    # Calculate mean enrollment for 2013 and 2022
    mean_enrollment_2013 = np.mean(enrollment_data[0, :, :])
    mean_enrollment_2022 = np.nanmean(enrollment_data[9, :, :])  # Use nanmean to ignore NaNs
    # Calculate total graduating class of 2022 across all schools
    total_graduating_class_2022 = np.nansum(enrollment_data[9, :, 2])  # Use nansum to ignore NaNs
    # Find the highest and lowest enrollment numbers across all schools and years
    highest_enrollment_all_time = np.nanmax(enrollment_data)  # Use nanmax to ignore NaNs
    lowest_enrollment_all_time = np.nanmin(enrollment_data)  # Use nanmin to ignore NaNs
    
    # Print general statistics
    print(f"Mean enrollment in 2013: {int(mean_enrollment_2013)}")
    print(f"Mean enrollment in 2022: {int(mean_enrollment_2022)}")
    print(f"Total graduating class of 2022 across all schools: {int(total_graduating_class_2022)}")
    print(f"Highest enrollment for a single grade within the entire time period (across all schools): {int(highest_enrollment_all_time)}")
    print(f"Lowest enrollment for a single grade within the entire time period (across all schools): {int(lowest_enrollment_all_time)}")

def main():
    """
    Main function to run the school enrollment statistics program.
    """
    print("ENSF 692 School Enrollment Statistics")
    
    # Stage 1: Array Creation
    print("\n***Array Information***\n")
    print(f"Shape of the array: {enrollment_data.shape}")
    print(f"Dimensions of the array: {enrollment_data.ndim}")
    
    # Stage 2: School Stats
    while True:
        print("\n***Requested School Statistics***\n")
        user_input = input("Enter the school name or numerical code: ")
        try:
            school_index = get_school_code_index(user_input)
            print_school_stats(school_index)
            break
        except ValueError as e:
            print(e)
    
    # Stage 3: General Stats
    print("\n***General Statistics for All Schools***\n")
    print_general_stats()

if __name__ == '__main__':
    main()