import pandas as pd
import numpy as np

# Load your existing data
data = pd.read_csv('sample_house_data.csv')

# Create a synthetic 'Price' column based on features + random noise
data['Price'] = (
    data['LotArea'] * 0.5 + 
    data['OverallQual'] * 10000 + 
    data['GrLivArea'] * 50 + 
    np.random.normal(0, 10000, size=len(data))
).astype(int)

# Save the new CSV with target
data.to_csv('sample_house_data_with_price.csv', index=False)

print("Synthetic target column 'Price' added and saved as 'sample_house_data_with_price.csv'.")
