import pandas as pd
from counselors_processing import process_counselors_data

# Load athletes data
athletes_df = pd.read_csv('path_to_athletes_data.csv')

# Process counselors data
counselors_df = process_counselors_data(athletes_df)

# Now you can use counselors_df for further processing
print(f"Processed {len(counselors_df)} unique counselor records")

# Save to CSV if needed
counselors_df.to_csv('processed_counselors.csv', index=False)
