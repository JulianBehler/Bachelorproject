import scipy.stats as stats
import matplotlib.pyplot as plt

# Group 1: SMOTE NI ON
group1 = [
    0.8249, 0.8319, 0.8229, 0.8253, 0.8247, 0.8239, 0.8342, 0.8237,
    0.8269, 0.8217, 0.8243, 0.8274, 0.8231, 0.8233, 0.8210, 0.8289
]

# Group 2: ros-openstack NI ON
group2 = data = [
    0.8279, 0.8300, 0.8276, 0.8261, 0.8230, 0.8300, 0.8313, 0.8253,
    0.8230, 0.8278, 0.8273, 0.8229, 0.8277, 0.8278, 0.8294, 0.8284
]

# Perform Levene's test
statistic, p_value = stats.levene(group1, group2, center="median")
# Print the results
print("Levene's Test Statistic:", statistic)
print("p-value:", p_value)

# Check if the p-value is less than the significance level (e.g., 0.05)
alpha = 0.05
if p_value < alpha:
    print("There is a statistically significant difference between the groups.")
else:
    print("There is no statistically significant difference between the groups.")
