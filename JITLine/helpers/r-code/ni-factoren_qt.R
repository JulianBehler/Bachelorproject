##########################
#QT with NI-Factors
##########################

#auc score
auc_scores <- c(0.8167,0.8100,0.8093,0.8110,0.8055,0.8132,0.8208,0.8152,
                0.8144,0.8129,0.8126,0.8096,0.8104,0.8092,0.8118,0.8135)


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
  0.9816, 0.1694,
  0.9849, 0.1475,
  0.9816, 0.1694,
  0.9820, 0.1585,
  0.9824, 0.1585,
  0.9816, 0.1694,
  0.9812, 0.1639,
  0.9820, 0.1639,
  0.9832, 0.1674,
  0.9807, 0.1803,
  0.9828, 0.1639,
  0.9799, 0.1803,
  0.9816, 0.1639,
  0.9816, 0.1694,
  0.9803, 0.1803,
  0.9807, 0.1672
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