import scipy.stats as stats

# Updated example data for group1 and group2
group1 = [0.827789012, 0.822234568, 0.823378901, 0.827687726, 0.823840239, 0.822700437, 0.822143668, 0.827811161, 0.822295991, 0.826560928, 0.821745671, 0.824325679, 0.828765432, 0.826987654, 0.823123457, 0.82656789]
group2 = [0.827687726, 0.823840239, 0.826038496, 0.825633982, 0.826324691, 0.823572359, 0.824312967, 0.82261848, 0.826159213, 0.821133928, 0.825172898, 0.828410961, 0.823391035, 0.823548803, 0.820637995, 0.825959639]

# Perform Mann-Whitney U-test
statistic, p_value = stats.mannwhitneyu(group1, group2)

# Print the results
print("Mann-Whitney U-test Statistic:", statistic)
print("p-value:", p_value)

# Check if the p-value is less than the significance level (e.g., 0.05) to determine significance
alpha = 0.05
if p_value < alpha:
    print("Reject the null hypothesis: The two groups have significantly different distributions.")
else:
    print("Fail to reject the null hypothesis: No significant difference between the two groups' distributions.")
