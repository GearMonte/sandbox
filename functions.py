def json_df(json_file_path):
    import pandas as pd
    # Read the JSON file using Pandas
    edi_df = pd.read_json(json_file_path)
    # Return the resulting DF
    return edi_df

"""
Example usage:
Assuming 'data.json' is your JSON file 
in the same directory as your script:

df = json_df('data.json')
print(df)
"""