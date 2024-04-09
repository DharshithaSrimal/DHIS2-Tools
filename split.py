import pandas as pd

# Load the CSV file
df = pd.read_csv('wdf_patient_visit_data.csv')

# Split the data into four equal parts
num_records = len(df)
chunk_size = num_records // 4

for i in range(4):
    start_idx = i * chunk_size
    end_idx = start_idx + chunk_size if i < 3 else None
    chunk = df.iloc[start_idx:end_idx]
    chunk.to_csv(f'dataset_{i+1}.csv', index=False)
