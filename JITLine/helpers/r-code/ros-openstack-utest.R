# SMOTE NI ON
group1 <- c(
  0.8678, 0.8693, 0.8663, 0.8708, 0.8700, 0.8693, 0.8755,0.8708,
  0.8700, 0.8647, 0.8685, 0.8653, 0.8730, 0.8626,0.8685, 0.8640)

#ros-openstack NI ON
group2 <- c(
  0.8760, 0.8753, 0.8753, 0.8760, 0.8753, 0.8753, 0.8783, 0.8760,
  0.8753, 0.8753, 0.8760, 0.8767, 0.8753, 0.8693, 0.8775, 0.8760
)
# Perform Mann-Whitney U-Test
result <- wilcox.test(group1, group2)

# Print the p-value
print(result$p.value)

# Check if the p-value is less than the significance level (e.g., 0.05)
if (result$p.value < 0.05) {
  print("There is a significant difference between the groups.")
} else {
  print("There is no significant difference between the groups.")
}


################
#Levene
################
#install.packages("car") can be skipped installed
#library(car)

# Perform Levene's Test
resultLevene <- leveneTest(c(group1, group2))

# Check if the p-value is less than the significance level (e.g., 0.05)
if (resultLevene$p.value < 0.05) {
  print("The variances are significantly different.")
} else {
  print("The variances are not significantly different.")
}