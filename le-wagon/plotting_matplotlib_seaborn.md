


# Matplotlib

  1. Basics:
     1. Plot 2 graphs on top of each other and set the x limits
        1. plt.hist(predicted_weights);
        2. plt.hist(orders2.review_score);
        3. plt.xlim([0,5]);


# Seaborn
  import seaborn as sns

  1. Histplot with kernal distribution estimator:
     1. sns.histplot(df.Series, kde=True)

  2. Regplot of a df
     1. sns.regplot(x='review_score', y='delay_vs_expected', data=orders2, ci=95)
        1. with confidence interval
        2. uses df series names as inputs
        3. specify the x,y, and data
     2. to select a sample, use:
        1. sns.regplot(x='review_score', y='delay_vs_expected', data=orders2.sample(10, random_state=6), ci=95)
