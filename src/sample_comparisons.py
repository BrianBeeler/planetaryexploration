#%matplotlib inline
#%config InlineBackend.figure_format = 'retina'

import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

plt.style.use('ggplot')

plt.figure(figsize=(8,6))
plt.hist(sample1, bins=100, alpha=0.5, label="data1")
plt.hist(sample2, bins=100, alpha=0.5, label="data2")

plt.show()


print("\n\n Because of the disparity in sample size, it is difficult to compare the samples with a histogram.")
print("\n Instead, a scatter plot, may be more useful.")

fig, ax = plt.subplots(1, figsize=(16, 3))

ax.scatter(sample1, np.repeat(0, len(sample1)) + np.random.normal(0, 0.1, len(sample1)), s=45, color='red')
ax.scatter(sample2, np.repeat(1, len(sample2)) + np.random.normal(0, 0.1, len(sample2)), s=45, color='blue')
ax.set_yticks([0, 1])
ax.set_yticklabels(["Sample 1", "Sample 2"])

print(sample1.mean())
print(sample2.mean())