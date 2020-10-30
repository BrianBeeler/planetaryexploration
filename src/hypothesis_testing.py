print("\n Yet it remains unclear, are these differences coincidental?")

print("\n Null hypothesis: There is no difference between the temperatures of planet 1 and of planet 2.")

print("\n Sample 1 mean: ", sample1.mean())

print("\n Sample 2 mean: ", sample2.mean())

print("\n Sample 1 varience: ", sample1.var())

print("\n Sample 2 varience: ", sample2.var())

print("\n\n A Welch's T-test will be utilized: ")


def welch_test_statistic(sample_1, sample_2):
    numerator = np.mean(sample_1) - np.mean(sample_2)
    denominator_sq = (np.var(sample_1) / len(sample_1)) + (np.var(sample_2) / len(sample_2))
    return numerator / np.sqrt(denominator_sq)

test_statistic = welch_test_statistic(sample1, sample2)
print("\n\n Welch Test Statistic: {:2.2f}".format(test_statistic))    

def welch_satterhwaithe_df(sample1, sample2):
    ss1 = len(sample1)
    ss2 = len(sample2)
    df = (
        ((np.var(sample1)/ss1 + np.var(sample2)/ss2)**(2.0)) / 
        ((np.var(sample1)/ss1)**(2.0)/(ss1 - 1) + (np.var(sample2)/ss2)**(2.0)/(ss2 - 1))
    )
    return df

df = welch_satterhwaithe_df(sample1, sample2)
print("\n\n Degrees of Freedom for Welch's Test: {:2.2f}".format(df))

x = np.linspace(-10, 10, num=250)

fig, ax = plt.subplots(1, figsize=(16, 3))
students = stats.t(df)
ax.plot(x, students.pdf(x), linewidth=2, label="Degree of Freedom: {:2.2f}".format(df))
ax.legend()
ax.axvline(x=test_statistic)
ax.axvline(x=-test_statistic)
ax.set_title("Distribution of Welch's Test Statistic Under the Null Hypothesis")


# Get the p value
results = stats.ttest_ind(sample2, sample1, equal_var=False)

print('\n Alpha is : 0.01')
print('\n P-Value is : ', results.pvalue)
print('\n\n Thus, the null hypothesis can be rejected very safely.')
print('\n The number of suns the a plant has, specific to single planet systems')
print('\n is clearly correlated with higher temperatures. ')
print("\n Binary sytems with one planet have a statistically higher temperature.")

