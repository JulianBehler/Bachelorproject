import scipy.stats as stats

#SMOTE QT NI Factors on
group1 = [
    0.8249, 0.8319, 0.8229, 0.8253, 0.8247, 0.8239,
    0.8342, 0.8237, 0.8269, 0.8217, 0.8243, 0.8274,
    0.8231, 0.8233, 0.8210, 0.8289
]

#RUS NI Factors on
group2 = [
    0.8126, 0.8195, 0.8213, 0.8195, 0.8176, 0.8192,
    0.8157, 0.8187, 0.8123, 0.8184, 0.8193, 0.8240,
    0.8180, 0.8259, 0.8177, 0.8201
]
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