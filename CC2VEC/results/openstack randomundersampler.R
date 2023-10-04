#Openstack Randomundersampler

#calc the mean/avg

auc_accuracy <- c(0.7379, 0.7432, 0.7393, 0.7430,
                  0.7423, 0.7429, 0.7419, 0.7408, 
                  0.7422, 0.7375, 0.7369, 0.7366, 
                  0.7363, 0.7410, 0.7407, 0.7406)

runtime_accuracy <- c(294.823, 294.166, 297.177, 298.197, 
                      294.565, 296.374, 291.951, 293.687, 
                      293.742, 291.846, 292.426, 295.571, 
                      295.668, 290.422, 296.369, 298.521)
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
first_values <- c(0.4435, 0.3750, 0.5188, 0.3211, 
                  0.4401, 0.3433, 0.4341, 0.4401, 
                  0.0402, 0.6747, 0.6652, 0.6601, 
                  0.6730, 0.4024, 0.3955, 0.4084)

second_values <- c(0.9202, 0.9448, 0.8712, 0.9509, 
                   0.9202, 0.9509, 0.9202, 0.9202, 
                   0.9939, 0.6626, 0.7117, 0.7178, 
                   0.6810, 0.9325, 0.9387, 0.9202)


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
