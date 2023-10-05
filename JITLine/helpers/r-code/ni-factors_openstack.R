##########################
#Openstack with NI-Factors
##########################

#auc score
auc_scores <- c(0.8249, 0.8319, 0.8229, 0.8253, 0.8247, 0.8239, 0.8342, 0.8237,
                   0.8269, 0.8217, 0.8243, 0.8274, 0.8231, 0.8233, 0.8210, 0.8289)


# Calculate mean/avg
mean_result = mean(auc_scores)

# Calculate variance
variance_result <- var(auc_scores)

# Calculate minimum
min_result <- min(auc_scores)

# Calculate maximum
max_result <- max(auc_scores)

# Calculate standard deviation
std_deviation_result <- sd(auc_scores)

# Print the results
cat("Minimum:", min_result, "\n")
cat("Maximum:", max_result, "\n")
cat("Mean/Average:", mean_result, "\n")
cat("Variance:", variance_result, "\n")
cat("Standard Deviation:", std_deviation_result, "\n")

################################################################################
# per class accuracy score
#first_values <- c(0.7406, 0.7440, 0.7432, 0.7483, 0.7432,
#                  0.7534, 0.7474, 0.7483, 0.7483, 0.7466,
#                  0.7286, 0.7483, 0.7329, 0.7432, 0.7483, 0.7663)
#
#second_values <- c(0.7178, 0.7423, 0.7730, 0.7239, 0.7546, 0.7301,
#                   0.7178, 0.7485, 0.6871, 0.7423, 0.7239, 0.7546,
#                   0.7546, 0.7301, 0.6933, 0.7117)
#
#zero_label = mean(first_values)
#one_label  = mean(second_values)
#cat("Zero Label:", zero_label, "\n")
#cat("One Label:", one_label, "\n")
################################################################################

per_class_acc_score <- matrix(c(
  0.9452, 0.3129,
  0.9486, 0.3006,
  0.9478, 0.2822,
  0.9503, 0.3006,
  0.9503, 0.2945,
  0.9503, 0.2883,
  0.9495, 0.2775,
  0.9521, 0.2883,
  0.9503, 0.3252,
  0.9435, 0.3006,
  0.9562, 0.2761,
  0.9491, 0.2627,
  0.9529, 0.3006,
  0.9453, 0.3074,
  0.9512, 0.2761,
  0.9478, 0.2638
), ncol = 2, byrow = TRUE)

# Find the minimum and maximum values for the first column
min_first_col <- min(per_class_acc_score[, 1])
max_first_col <- max(per_class_acc_score[, 1])

# Find the minimum and maximum values for the second column
min_second_col <- min(per_class_acc_score[, 2])
max_second_col <- max(per_class_acc_score[, 2])

# Print the results
cat("Minimum value for the first column:", min_first_col, "\n")
cat("Maximum value for the first column:", max_first_col, "\n")
cat("Minimum value for the second column:", min_second_col, "\n")
cat("Maximum value for the second column:", max_second_col, "\n")
##############################MEAN##############################################

# Calculate the mean for the first and second column
mean_first_col <- mean(per_class_acc_score[, 1])
mean_second_col <- mean(per_class_acc_score[, 2])

# Print the result
cat("Mean of the first column:", mean_first_col, "\n")
cat("Mean of the second column:", mean_second_col, "\n")

###########################VARIANCE AND MEAN####################################

# Calculate the variance and standard deviation for both columns
variance_first_col <- var(per_class_acc_score[, 1])
std_deviation_first_col <- sd(per_class_acc_score[, 1])

variance_second_col <- var(per_class_acc_score[, 2])
std_deviation_second_col <- sd(per_class_acc_score[, 2])

# Print the results
cat("For the first column:\n")
cat("  Variance:", variance_first_col, "\n")
cat("  Standard Deviation:", std_deviation_first_col, "\n")

cat("For the second column:\n")
cat("  Variance:", variance_second_col, "\n")
cat("  Standard Deviation:", std_deviation_second_col, "\n")