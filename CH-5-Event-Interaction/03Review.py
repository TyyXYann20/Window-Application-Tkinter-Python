import pandas as pd

# Create a dictionary with the data
data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
    'Sales': [82000, 6000, 12394, 21212, 2120, 9893, 999, 1000, 87000, 79800, 12123, 23232]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Save to Excel file
df.to_excel('sales_data.xlsx', index=False)