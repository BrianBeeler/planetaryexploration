print("\n Yet it remains unclear, are these differences coincidental?")

print("\n Null hypothesis: There is no statistical difference between Sample 1 and Sample 2")

print("\n\n A Welch's T-test will be utilized: ")



def welch_test_statistic(sample_1, sample_2):
    numerator = np.mean(sample_1) - np.mean(sample_2)
    denominator_sq = (np.var(sample_1) / len(sample_1)) + (np.var(sample_2) / len(sample_2))
    return numerator / np.sqrt(denominator_sq)

test_statistic = welch_test_statistic(sample1, sample2)
print("Welch Test Statistic: {:2.2f}".format(test_statistic))    

def welch_satterhwaithe_df(sample1, sample2):
    ss1 = len(sample1)
    ss2 = len(sample2)
    df = (
        ((np.var(sample1)/ss1 + np.var(sample2)/ss2)**(2.0)) / 
        ((np.var(sample1)/ss1)**(2.0)/(ss1 - 1) + (np.var(sample2)/ss2)**(2.0)/(ss2 - 1))
    )
    return df

df = welch_satterhwaithe_df(sample1, sample2)
print("Degrees of Freedom for Welch's Test: {:2.2f}".format(df))

x = np.linspace(-3, 3, num=250)

fig, ax = plt.subplots(1, figsize=(16, 3))
students = stats.t(df)
ax.plot(x, students.pdf(x), linewidth=2, label="Degree of Freedom: {:2.2f}".format(df))
ax.legend()
ax.set_title("Distribution of Welch's Test Statistic Under the Null Hypothesis")


import numpy as np

x = np.linspace(-10, 10, num=500)

fig, ax = plt.subplots(1, figsize=(16, 3))
students = stats.t(df)
ax.plot(x, students.pdf(x), linewidth=2, label="Degree of Freedom: {:2.2f}".format(df))
_ = ax.fill_between(x, students.pdf(x), where=(x >= -test_statistic), color="red", alpha=0.25)
_ = ax.fill_between(x, students.pdf(x), where=(x <= test_statistic), color="red", alpha=0.25)

plt.text(-8.8,0.25,'Welch Test Statistic: -5.12',rotation=0)
plt.axvline(x=-5.12)

ax.legend()
ax.set_title("p-value Region")


# Get the p value

p_value = 1 - students.cdf(test_statistic)
print("P-value for sample 1 having a greater temperature that sample 2 {:2.3f}".format(p_value))