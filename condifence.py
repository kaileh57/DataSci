import statsmodels.stats.proportion as ssp

count1, nobs1 = 60, 100
count2, nobs2 = 40, 100

ci_low1, ci_upp1 = ssp.proportion_confint(count1, nobs1, alpha=0.05, method='normal')

ci_low, ci_upp = ssp.confint_proportions_2indep(count1, nobs1, count2, nobs2, compare ='diff', alpha=0.05, method='newcomb')
