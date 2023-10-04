#Openstack smote

#calc the mean/avg

auc_accuracy <- c(0.7265, 0.7255, 0.7229, 0.7237,
                  0.7024, 0.7280, 0.7213, 0.7138,
                  0.7254, 0.7222, 0.7037, 0.7162,
                  0.7103, 0.7256, 0.7081, 0.7247)

runtime_accuracy <- c(1973.362, 1969.508, 1970.967, 1965.323,
                      1952.32,  1958.745, 1959.125, 1949.589,
                      1960.736, 1963.543, 1961.325, 1953.75,
                      1955.321, 1957.443, 1957.642, 1959.77)

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
first_values <- c(0.7295, 0.9358, 0.9298, 0.9692,
                  0.7748, 0.6558, 0.9084, 0.7646,
                  0.9658, 0.9015, 0.7774, 0.6892,
                  0.6978, 0.8801, 0.7226, 0.8750)

second_values <- c(0.5951, 0.1902, 0.2147, 0.1043,
                   0.4540, 0.6748, 0.2515, 0.5215,
                   0.1043, 0.2577, 0.4540, 0.6012,
                   0.6074, 0.3436, 0.5521, 0.3497)



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
