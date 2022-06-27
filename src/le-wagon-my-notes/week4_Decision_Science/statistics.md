# CONTENTS


# key properties and their usage/meaning

1. p-value is the indicator of statistical significance
2. F-statistic
   1. high numbers - show a 'solid result'
   2. if = 1, you cannot rule out that the linear regression is not statistically significant
3. std errors
4. t-stats
5.  confidence interval
6. variance
7. std, standard deviation = sqrt(variance)
8. z-score - no. s.d's from the mean (t-score for a t-distribution)
9. ## Linear Regression
   1.  Ordinary Least Square - a model that reduces the L2 distance
   2.  heteroscedasticity
      1. issue: gives smaller than realistic p-values, making the prediction seem more accurate
   3.  R-squared
      2. coefficient of determination or r-squared:
      3. definition: the proportion of the variance in the dependent variable that is predictable from variance of the features.
   4.  inferential analysis
       1. Assumptions for:
          1. Linearity
          2. Independence
          3. Homoscedasticity
             1. variance of the residual, or error term, in a regression model is constant. That is, the error term does not vary much as the value of the predictor variable changes.
             2. If this is not the case, then we will have a biases estimator
          4. Normality
   5.  Residual
       1.  The error term - real v predicted, element wise
10. ## Logistic Regression
    1.  To deal with categorical data, with 0 or 1 data
        1.  in the smf model, use C(column_name) to deal with these
    2.  NOTE: coefficients in a logit space - need to convert back to % probability etc
    3.  Use a 'sigmoid function'
        1.  Classification threshold, default of 0.5 so that >0.5 goes to 1, <0.5 goes to 0
        2.  Likelihood (the Product) is the way of assessing good fit (as opposed to OLS)
            1.  I.e. this is === combined probability
            2.  Closer to 1 is best
            3.  Very sensitive to outliers
        3.  **Logisitic Regression attempts to predict Probabilities**
    4.  Logistic Classifiers are calibrated classifiers
    5.  p - the likelihood:
        1.  p = SigmoidFunction(x) =
    6.  Logit space v proba space
        1.  Logit good for explanation - probably not that important
        2.  Logit space = logit(p/1-p
        3.  Odds: 1 / 1-p
        4.  Logit = log(odds))
    7.  Usage
        1.  Use the np.log() function, then take the intercept as the coefficient
        2.  or use SNS:
            1.  sns.logit()
    8.  N.B:
        1.  Use of R^2 in logistic regression
            1.  It is valid in comparing multiple models trying to predict the same outcome with the same dataset
            2.  It is invalid in comparing different datasets

    9.  Interpretation
        1.  p-values work in a similar way
        2.  t-scores don't apply - binary process, so can use z-score
        3.  Goodness of fit: psuedo R^2
            1.  1-LL(pred)/LL(actual)
        4.  log-likelihood: closer to 0 is better (range: -minus inv to 0)
            1.  not as descriptive as R^2, but good for comparing models
    10. Multicolinearity
        1.  Can't keep all the other variables constant while we look at and vary one
        2.  Matrices of full rank are required - these avoid colinearity
        3.  if colinearity => cannot really trust the p-values and other results
        4.  **How to detect multicolinearity?**
            1.  df.corr() only shows bivariate correlation
            2.  Variance Inflation Factor (VIF) - the higher the less useful
                1.  Measures the level of multicolinearity per feature
            3.  Make sure to scale your data - linear regression is used by VIF
                1.  > 10 means potential cause for concern
                    1.  Take out that feature, and run again (start at the top of the list, go from there)
            4.  **IMPORT STATEMENT**
                1.  from statsmodels.stats.outliers_influence import variance_inflation_factor as vif
    11. # **SUMMARY - REGRESSION CHEAT SHEET**
        1.  Goodness of fit
            1. How well does our y-pred explain the true y
            2. use:
                1.  Linear Regression: R^2
                2.  Logistic Regression: psuedo R^2
        2.  Statistical significance
            1.  Are regression coefficents trustworthy?
            2.  use:
                1.  Linear Regression: p-values and t-tests
                2.  Logistic Regression: p-values and z-tests
        3.  Inference conditions
            1.  Can we trust the p-values?
            2.  use:
                1.  Linear Regression: Residual plots
                2.  (Logistic Regression: not needed)
        4.  Multicolinearity
            1.  use: VIF analysis (for both Linear and Logisitic Regression)

11. ## ML model assessment
    1.  accuracy, precision, recall, F1-score?
