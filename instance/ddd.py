import pandas as pd

# Read the SQLite database file into a Pandas DataFrame
df = pd.read_sql_query("SELECT * FROM loan_applications", 'sqlite:///loan_applications.db')

# Print the DataFrame
print(df)