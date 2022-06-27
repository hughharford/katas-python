# CONTENTS

1. Duplicates
2. Missing data
3. Outliers
4. Scaling
5. Balancing
6. Encoding
7. Discretizing
8. Feature creation
9. Feature selection


## OTHER
  Data Leakage


### 1. Duplicates
  1. To avoid
     1. data leakage
     2. discrediting your model
   ```python
        df.duplicated() # gives Boolean for duplicates
        df.duplicated().sum() # gives the number of duplicated
        df.drop_duplicates() # not inplace - but shows the df without
   ```
    2. Drop duplicates is the only work done before splitting the data into test and train

### 2. Missing data
  1. Common causes
     1. Programming error, random events, measurement failure
  2. Representations - these vary as per dataset
     1. NaN
     2. Large negatives -99, -999
     3. ?
     4. Inf
    ```python
      empty = df.isnull().sum().sort_values(ascending=False)
      empty / len(df)
    ```
  1. Handling missing data
  2. cause?
  3. can we afford it
  4. does missing data indicate data in itself?
  5. etc
    ```python
      df.col.replace(np.nan, 'Replacevalue')
      df.col.value_count()
    ```
    1. Can replace the data with e.g. the mean, so no statistical effect
       1. np.mean() ignores the np.nan values
       2. Other values of course valid based on your data
    2. > 30% of missing data, drop the feature (row - if huge data, or the feature, via column)
    3. Typically replace with mode for categorical data
    4. ISSUES with replacement
       1. Replacing values, creates noise, introduces human bias
       2. Relationships between columns can be changed
    5. Don't replace on the test set!
    6. ..
    7. sklearn has sklearn.SimpleImputer
       1. Learns the metrics, for replapplication
      ```python
        from sklearn import SimpleImputer
        imputer = SimpleImputer(strategy='mean')
        imputer.fit(data[['ColumnName']])
        df['ColumnName'] = imputer.transform(data[['ColumnName']])
        # check with
        df.isnull().sum()
        imputer.statistics_ # shows the mean used
      ```


### 3. Outliers
  1. Error?
     1. Data, measurement, data manipulation and preprocessing error
  2. Can also be a novel data point
  3. Effect
     1. affects distribution, patterns
     2. CLT metrics, mean, sigma etc
     3. ML model performance
  4. Detection
     1. With the boxplot
```python
  df[[col]].boxplot()
```
   1. Considerations
      1. If really an error, then can be dropped e.g. sq metres = -1
      2. Use .argmin() and drop(argmin()).reset_index()

### 4. Scaling
  1. Transforms continuous data into a common smaller range
  2. Some data is NOT continous
  3. Why
     1. So that all the features are on the same scale
        1. Improves computational efficency
        2. Increases interpretability of feature coefficients
  4. DIFFERENT WAYS
     1. Standardising
        1. z-score = (x - mean)/sigma
        2. sklearn has a method for this
        3. About standardisation
           1. No exact common range
           2. sensitive to outliers
           3. Can distort the relative feature between values
     2. Normalisation
        1. Compress into fixed range [0,1]
     3. Min-Max
        1. This ensures a fixed range - crucial for distance based algorithms
        2. Efficent regards of distribution
        3. Still affected by outliers
        4. Doesn't correct skewness
  5. EFFECTS OF SCALING
     1.
```python
  from sklearn.preprocessing import StandardScaler
  scaler = StandardScaler()
  scaler.fit(df[['Col']])
  df = scaler.transform(df[['Col']])
```
   1. But for outliers, we can use from sklearn.preprocessing import RobustScaler
      1. Robust Scaling - uses the median
      2. RobustScaled = (x - median) / IQR
      3.
```python
  from sklearn.preprocessing import RobustScaler
  r_scaler = RobustScaler()
  r_scaler.fit(df[['Col']])

```
### 5. Balancing - good for Ethical AI
  1. Different numbers of datapoints for a class within a dataset can be difficult
  2. Not just labels, but across all features
  3. WHY
     1. ML algorithms learn by example
     2. Will tend to predict the under-represented class poorly
  4. STRATEGIES
     1. Over-sample minority class
        1. Can create leakage between train and test datasets
     2. Under-sampling majority class
     3. Computation of synthetic members of minority class
     4. SMOTE technique
        1. based on vectors between minority set data points
  5. NOTES
     1. Only use balancing on training sets
```python

```

### 6. Encoding
  1. Label Encoding
     1. Transform into numbers, as ML often works only on data
     2. Only use this on the label - target - as it is a single df.Series
     3. For features, this would create a false relationship between feature
  2. Feature Encoding
     1. Create a binary column for each possible category - known as One Hot Encoding
  3. NOTES
     1.
```python
  # LABEL ENCODER
  from sklearn.preprocessing import LabelEncoder
  LabelEncoder()

  from sklearn.preprocessing import OneHotEncoder
  ohe = OneHotEncoder(sparse = False) #Sparse are much more efficient - Sparse = True
  ohe.fit(df[['Col']])
  encoded = ohe.transform(df[['Col']])
  df['Col1'],df['Col2'],df['Col3'] = encoded.T
  df.head() # check


  # can run a drop(drop='if_binary', ...) # if a single option
  ohe.feature_names_ # or similar - will show the binary split
```
### 7. Discretizing
  1. Use pd.cut()
  2. Cut the continous variable into numerical class

```python
  min() - 1
  mean()
  max() + 1
```

### 8. Feature creation
  1. Helps
     1. Model performance
     2. Computational performance
### 9. Feature selection
  1. TYPES
     1. Multivariate
     2. Univariate
  2. Why selection
     1. Garbage in & out
     2. The curse of dimensionality
     3. Reduce complexity
  3. Curse of dimensionality
     1. peak of meaningful relationship is at the lower end of no. features
        1. Based on a static observation set
     2. As you increase features, the number of observations you need to maintain the same resolution increases exponentially
  4. Feature correlation
     1. High correlation = redundant information


# Scaling-induced data leakage
  1. Care needed with this, when scaling across all features

# Feature Permuation
  1. Not simple - can be computationally expensive
  2. Uses shuffling through rows of features to establish if the feature is noise or useful
  3. Gives a score decrease for each feature (to see what contribution that feature makes)
  ```python
   from sklearn.inspection import permutation_importance
  ```
# OVERALL
  4. Reduce features if possible
  5. Make sure to apply the same transforms and scales for predictions
  6.
