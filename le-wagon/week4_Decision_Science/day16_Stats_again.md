# z-score to scale a value
  i.e. how many SDs away from the mean the value is
  Z-score important for hyposesis testing

  Further away from mean $\mu$ is less likely

# The different means
  $\mu$ is the population mean, the mean
  x-bar is the sample mean

# NOTATION
  1. Standard Deviation = $\sigma$
  2. Population mean = $\mu$
  3. Sample mean = $\bar x$

# Scaling the data => results in
  Variance = 1, => SD is also 1

# Statistical logic
  Uniformly randomly distributed (Central Limit Theorum)
  Because n, the number of samples is large enough (Law of Large Numbers)

The distribution of sample means also follows the normal distribution

MLE - Maximum Likelihood Estimate
We say at X-bar n, the sample mean is the MLE for the \mu

# Sample size considerations
  - ?? when is n large enough for the CLT to apply
  - n > 30 then CLT applies
  - n > 10, observations 'non-skewed', without outliers => CLT applies
  - If the global population is known to be normal, then CLT applies
  -

# Hypotheses!
  - Null hypothesis $H_0$: the 'effect' we are investigating is none - there is no change
  - Alternative hypothesis $H_a$: that something has changed, e.g. $\bar x$ has moved
  - Type 1 and Type 2 errors
    - Type 1 error: reject the null hypothesis, when we shouldn't
    - Type 2 error: don't reject a null hypothesis, when you should

# Power of the test
  - Power = the probability that we will correctly reject the null hypothesis
  - Power = 1 - P(type 2 error)

# Normal distribution, $\normal $ therefore:
  95% of values within 2x SD from the mean
  99.7% of values within 3x SD from the mean

# WHEN sample size is not large enough...
  - We can always calculate the T-statistics
  - DEGREES OF FREEDOM - sample size minus 1 = **n-1**
  - The T- or Student distribution with n-1 degrees of freedom
  - Now:
    - We use t-tests (not z-scores)
  - Student t-distribution
    - Has fatter tails c.f. normal
    - as the degrees of freedom increases, more like Normal
