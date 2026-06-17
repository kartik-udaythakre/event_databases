import pandas as pd
# Define data using a dictionary
data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "City": ["New York", "London", "Paris"]
}

# Create the DataFrame
df = pd.DataFrame(data)

# Display the DataFrame
print(df)