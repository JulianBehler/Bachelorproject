##########################
#QT with undersampling
##########################

# Create the arc array
auc_scores <- c(0.8067, 0.8072, 0.8021, 0.8030, 0.8047, 0.8033, 0.8128, 0.8095,
                0.8077, 0.8046, 0.8072, 0.8123, 0.8045, 0.8050, 0.8124, 0.8099)

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
## per class accuracy score
#first_values <- c(
#  0.9870, 0.9879, 0.9874, 0.9879, 0.9870, 0.9887, 0.9891, 0.9887,
#  0.9883, 0.9895, 0.9874, 0.9866, 0.9870, 0.9887, 0.9887, 0.9870
#)
#
#second_values <- c(
#  0.1093, 0.1093, 0.1148, 0.1093, 0.1202, 0.1093, 0.1202, 0.1148,
#  0.1148, 0.1148, 0.1093, 0.1148, 0.1202, 0.1148, 0.1202, 0.1038
#)
#
#zero_label = mean(first_values)
#one_label  = mean(second_values)
#cat("Zero Label:", zero_label, "\n")
#cat("One Label:", one_label, "\n")
################################################################################

per_class_acc_score <- matrix(c(
  0.8208, 0.6066,
  0.8271, 0.6011,
  0.8095, 0.6230,
  0.8082, 0.6339,
  0.8304, 0.5956,
  0.8237, 0.5902,
  0.8229, 0.6066,
  0.8229, 0.6011,
  0.8208, 0.6230,
  0.8191, 0.6066,
  0.8245, 0.6120,
  0.8271, 0.6066,
  0.8090, 0.6120,
  0.8187, 0.6066,
  0.8208, 0.6066,
  0.8308, 0.6066
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