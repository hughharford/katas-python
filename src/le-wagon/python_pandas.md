
# SEE THE CHEATSHEET

# examples with notes:
  1. GROUPBY with COUNT
     1. df.groupby(df['index'])['other_column'].count().reset_index()
        1. group by 'index' and count the 'other column'
        2. reset index as counted output per index will be fewer rows than df
        3. cannot assign immediately back to df!
  2. MAP for df.series - with lambda function to standardise the data
     1. df['series_name'].map(lambda x: (x - var_mean) / var_sigma)
        1. was used in a function
  3. SIMPLE QUERY in PANDAS:
     1. DF_name = 'orders'
     2. DF.series_name = 'number_of_sellers' & 'order_id'
     3. orders.query("number_of_sellers>1")['order_id'].count()




# Map and Apply
```python
## MAP (for Series)
series.map(function)
Series.map({mapping dict})

## APPLY (for DataFrame)
df.apply(lambda col: col.max(), axis = 0)     # default axis
df.apply(lambda row: row[‘A’] + row[‘B’], axis = 1)
df.applymap(my_funct_for_indiv_elements)
    df.applymap(lambda x: '%.2f' % x)
```
