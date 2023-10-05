import scipy.stats as stats

#SMOTE QT NI Factors on
group1 = [0.8167, 0.8100, 0.8093, 0.8110, 0.8055, 0.8132, 0.8208, 0.8152,
          0.8144, 0.8129, 0.8126, 0.8096, 0.8104, 0.8092, 0.8118, 0.8135]

#ROS NI Factors on
group2 = [0.8209, 0.8174, 0.8194, 0.8149, 0.8121, 0.8118, 0.8171, 0.8191,
          0.8173, 0.8207, 0.8197, 0.8169, 0.8163, 0.8096, 0.8224, 0.8162]

# Perform Mann-Whitney U-test
statistic, p_value = stats.mannwhitneyu(group1, group2)

# Print the results
print("Mann-Whitney U-test Statistic:", statistic)
print("p-value:", p_value)

# Check if the p-value is less than the significance level (e.g., 0.05) to determine significance
alpha = 0.05
if p_value < alpha:
    print("There is a statistically significant difference between the groups.")
else:
    print("There is no statistically significant difference between the groups.")

#