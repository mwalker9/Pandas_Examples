## 1. Introduction ##

import pandas as pd
# read the data set into a pandas dataframe
f500 = pd.read_csv("f500.csv", index_col=0)
f500.index.name = None

# replace 0 values in the "previous_rank" column with NaN
f500.loc[f500["previous_rank"] == 0, "previous_rank"] = np.nan

f500_selection = f500[['rank', 'revenues', 'revenue_change']].head(5)

## 2. Reading CSV files with pandas ##

f500 = pandas.read_csv('f500.csv')

f500.loc[f500['previous_rank'] == 0, 'previous_rank'] = np.nan

## 3. Using iloc to select by integer position ##

fifth_row = f500.iloc[4]
company_value = f500.iloc[0, f500.columns.get_loc('company')]

## 4. Using iloc to select by integer position continued ##

first_three_rows = f500[:3]
first_seventh_row_slice = f500.iloc[[0,6], :5]

## 5. Using pandas methods to create boolean masks ##

null_previous_rank = f500.loc[f500['previous_rank'].isnull(), ['company', 'rank', 'previous_rank']]

## 6. Working with Integer Labels ##

null_previous_rank = f500[f500["previous_rank"].isnull()]
top5_null_prev_rank = null_previous_rank.iloc[:5]

## 7. Pandas Index Alignment ##

previously_ranked = f500[f500['previous_rank'].notnull()]
rank_change = previously_ranked['previous_rank'] - previously_ranked['rank']
f500['rank_change'] = rank_change


## 8. Using Boolean Operators ##

large_revenue = f500['revenues'] > (1000 * 100)
negative_profits = f500['profits'] < 0
combined = large_revenue & negative_profits
big_rev_neg_profit = f500.loc[combined]

## 9. Using Boolean Operators Continued ##

brazil_venezuela = f500.loc[(f500['country'] == 'Brazil') | (f500['country'] == 'Venezuela')]
tech_outside_usa = f500.loc[(f500['sector'] == 'Technology') & ~(f500['country'] == 'USA')].head(5)

## 10. Sorting Values ##

top_japanese_employer = f500.loc[f500['country'] == 'Japan'].sort_values(by='employees', ascending=False).iloc[0, 0]

## 11. Using Loops with pandas ##

top_employer_by_country = {}
for country in f500['country'].unique():
    current_country_companies = f500[f500['country'] == country]
    current_country_companies = current_country_companies.sort_values(by='employees', ascending=False)
    company_name = current_country_companies.iloc[0,0]
    top_employer_by_country[country] = company_name
    

## 12. Challenge: Calculating Return on Assets by Country ##

f500['roa'] = f500['profits'] / f500['assets']
top_roa_by_sector = {}
for sector in f500['sector'].unique():
    highest_roa_comp = f500[f500['sector'] == sector].sort_values(by='roa', ascending=False).iloc[0,0]
    top_roa_by_sector[sector] = highest_roa_comp
    