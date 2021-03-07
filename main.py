import pandas as pd
from pandas_profiling import ProfileReport

df = pd.read_csv('covid_19_data.csv')

# Generating a report
profile = ProfileReport(df)
profile.to_file(output_file='covid_19_analysis1.html')

# Generating a minimal report
profile = ProfileReport(df, minimal=True)
profile.to_file(output_file='covid_19_analysis_minimal.html')