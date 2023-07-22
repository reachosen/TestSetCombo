
import itertools
import pandas as pd

def generate_combinations(factor_dict, output_file):
    # Generate all combinations of factors
    combinations = []
    for r in range(1, len(factor_dict) + 1):
        for subset in itertools.combinations(factor_dict, r):
            combinations.append(subset)

    # Calculate the maximum number of factors in any combination
    max_factors = max(len(comb) for comb in combinations)

    # Generate column names based on the maximum number of factors
    column_names = [f'Factor_{i+1}' for i in range(max_factors)]

    # Create a dataframe to hold the combinations with the correct number of columns
    df = pd.DataFrame(combinations, columns=column_names)

    # Save the dataframe to an Excel file
    df.to_excel(output_file, index=False)


#use template    
# Define the factors and their positive case values
factors = {
    'Age': '85 and over',
    'Comorbidities': 'Two or More',
    'ICU Admission': 'Yes',
    ...
}

output_file = '/path/to/output/file.xlsx'

generate_combinations(factors, output_file)

