#Openstack

#calc the mean/avg

ros_openstack <- c(
  0.8760, 0.8753, 0.8753, 0.8760, 0.8753, 0.8753, 0.8783, 0.8760,
  0.8753, 0.8753, 0.8760, 0.8767, 0.8753, 0.8693, 0.8775, 0.8760
)

# Calculate mean/avg
mean_result = mean(ros_openstack)

# Calculate variance
variance_result <- var(ros_openstack)

# Calculate minimum
min_result <- min(ros_openstack)

# Calculate maximum
max_result <- max(ros_openstack)

# Calculate standard deviation
std_deviation_result <- sd(ros_openstack)

# Print the results

cat("Minimum:", min_result, "\n")
cat("Maximum:", max_result, "\n")
cat("Mean/Average:", mean_result, "\n")
cat("Variance:", variance_result, "\n")
cat("Standard Deviation:", std_deviation_result, "\n")

auc_scores = c(0.8279, 0.8300, 0.8276, 0.8261, 0.8230, 0.8300, 0.8313, 0.8253, 0.8230, 0.8278, 0.8273, 0.8229, 0.8277, 0.8278, 0.8294, 0.8284)
mean(auc_scores)

# per class accuracy score
first_values <- c(
  0.9606, 0.9598, 0.9632, 0.9615, 0.9598, 0.9598, 0.9615, 0.9589,
  0.9598, 0.9606, 0.9606, 0.9598, 0.9615, 0.9589, 0.9623, 0.9606
)

second_values <- c(
  0.2699, 0.2699, 0.2454, 0.2638, 0.2699, 0.2699, 0.2822, 0.2822,
  0.2699, 0.2761, 0.2515, 0.2822, 0.2577, 0.2270, 0.2699, 0.2699
)

zero_label = mean(first_values)
one_label  = mean(second_values)
cat("Zero Label:", zero_label, "\n")
cat("One Label:", one_label, "\n")


#Here are the U_Test and the levene Test



