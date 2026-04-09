import pandas as pd

# 1. Load files
current_year = pd.read_csv('2027.csv')
last_year = pd.read_csv('2026.csv')
two_years_ago = pd.read_csv('2025.csv')
three_years_ago = pd.read_csv('2024.csv')
four_years_ago = pd.read_csv('2023.csv')
five_years_ago = pd.read_csv('2022.csv')
six_years_ago = pd.read_csv('2021.csv')
seven_years_ago = pd.read_csv('2020.csv')
eight_years_ago = pd.read_csv('2019.csv')
target_list = pd.read_csv('catalyst.csv')

# Clean headers
current_year.columns = current_year.columns.str.strip()
last_year.columns = last_year.columns.str.strip()
target_list.columns = target_list.columns.str.strip()

# 2. Combine and PRE-CLEAN the UAccess data
combined_dump = pd.concat([current_year, last_year, two_years_ago, three_years_ago, four_years_ago, five_years_ago, six_years_ago, seven_years_ago, eight_years_ago ], ignore_index=True)

# Remove rows where the email is just a hyphen or empty
combined_dump = combined_dump[combined_dump['UA Email Address'] != '-']
combined_dump = combined_dump.dropna(subset=['UA Email Address'])

# 3. Create the clean keys
target_list['email_clean'] = target_list['Email'].astype(str).str.strip().str.lower()
combined_dump['email_clean'] = combined_dump['UA Email Address'].astype(str).str.strip().str.lower()

# 4. Remove duplicates after cleaning
combined_dump_unique = combined_dump.drop_duplicates(subset=['email_clean']).copy()

# 5. The Join
final_report = pd.merge(
    target_list,
    combined_dump_unique,
    on='email_clean',
    how='left'
)

# 6. Export
final_report.to_csv('Demographics_Combined.csv', index=False, encoding='utf-8-sig')

matched_count = final_report['UA Email Address'].notna().sum()
print(f"Match complete! Found {matched_count} out of {len(target_list)} students.")
