import pandas as pd

# 1. Load your lists (assuming they are CSVs, but works for Excel too)
target_list = pd.read_csv('your_4000_students.csv') 
uaccess_dump = pd.read_csv('uaccess_giant_export.csv')

# 2. Normalize and Clean (Lowercase + Strip whitespace)
target_list['email_clean'] = target_list['Email Column'].str.strip().str.lower()
uaccess_dump['email_clean'] = uaccess_dump['UA Email Address'].str.strip().str.lower()

# 3. Drop duplicates from UAccess data (one row per student)
uaccess_dump_unique = uaccess_dump.drop_duplicates(subset=['email_clean'])

# 4. The Join (Match your list to the demographics)
final_report = pd.merge(
    target_list, 
    uaccess_dump_unique, 
    on='email_clean', 
    how='left'
)

# 5. Output to a NEW CSV file
# 'index=False' prevents an extra column of numbers from being added
# 'encoding='utf-8-sig'' ensures it opens perfectly in Excel
final_report.to_csv('Matched_Student_Demographics.csv', index=False, encoding='utf-8-sig')

print("Success! 'Matched_Student_Demographics.csv' has been created.")
