#QT SMOTE

#calc the mean/avg

auc_accuracy <- c(0.7456, 0.7450, 0.7425, 0.7423,
                  0.7355, 0.7324, 0.7273, 0.7326,
                  0.7350, 0.7248, 0.7363, 0.7337,
                  0.7360, 0.7375, 0.7204, 0.7221)


runtime_accuracy <- c(4495.945, 4482.432, 4484.675, 4486.12,
                      4462.432, 4450.56,  4458.112, 4478.223,
                      4470.555, 4473.323, 4480.00,  4473.422,
                      4462.265, 4463.90,  4465.677, 4466.689)

# Calculate mean/avg
mean_resulttime = mean(runtime_accuracy)
cat("Mean/Average:", mean_resulttime, "\n")

# Calculate mean/avg
mean_result = mean(auc_accuracy)

# Calculate variance
variance_result <- var(auc_accuracy)

# Calculate minimum
min_result <- min(auc_accuracy)

# Calculate maximum
max_result <- max(auc_accuracy)

# Calculate standard deviation
std_deviation_result <- sd(auc_accuracy)

# Print the results

cat("Minimum:", min_result, "\n")
cat("Maximum:", max_result, "\n")
cat("Mean/Average:", mean_result, "\n")
cat("Variance:", variance_result, "\n")
cat("Standard Deviation:", std_deviation_result, "\n")





# per class accuracy score
first_values <- c(0.8882, 0.8865, 0.8827, 0.9171,
                  0.8886, 0.9229, 0.9347, 0.8957, 
                  0.8861, 0.9363, 0.8920, 0.9079, 
                  0.9246, 0.9087, 0.9560, 0.9527 )

second_values <- c(
    0.4098, 0.4208, 0.4262, 0.3388,
    0.3880, 0.2951, 0.2459, 0.3497, 
    0.3607, 0.2404, 0.3825, 0.3279, 
    0.3060, 0.3224, 0.1913, 0.2022 )


# Calculate standard deviation perclass 0
std_deviation_result_perclass0 <- sd(first_values)

# Calculate standard deviation perclass 1
std_deviation_result_perclass1 <- sd(second_values)

cat("stdp_0",std_deviation_result_perclass0, "\n")

cat("stdp_1:", std_deviation_result_perclass1, "\n")




# Calculate minimum
min_resultfirstvalues <- min(first_values)

max_resultfirstvalues <- max(first_values)

# Calculate maximum

min_resultsecondvalues <- min(second_values)

max_resultsecondvalues <- max(second_values)


zero_label = mean(first_values)

one_label  = mean(second_values)

cat("Zero Label:", zero_label, "\n")

cat("One Label:", one_label, "\n")

cat("Minimum:", min_resultfirstvalues, "\n")

cat("Maximum:", max_resultfirstvalues, "\n")

cat("Minimum:", min_resultsecondvalues, "\n")

cat("Maximum:", max_resultsecondvalues, "\n")