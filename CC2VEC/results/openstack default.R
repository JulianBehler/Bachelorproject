#Openstack default

#calc the mean/avg

auc_accuracy <- c(0.7632, 0.7647, 0.7610, 0.7622, 0.7611, 0.7606, 0.7613, 0.7611, 0.7650, 0.7678, 0.7670, 0.7667, 0.7617, 0.7598, 0.7622, 0.7612)

runtime_accuracy <- c(1118.433, 1123.523, 1098.699, 1099.432, 1098.232, 1124.453, 1099.347, 1098.99, 1099.33, 1095.584, 1098.013, 1095.158, 1100.748, 1110.075, 1096.561, 1096.751)


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



# Create the arc array
auc_scores <- c(0.7632, 0.7647, 0.7610, 0.7622, 
                0.7611, 0.7606, 0.7613, 0.7611,
                0.7650, 0.7678, 0.7670, 0.7667, 
                0.7617, 0.7598, 0.7622, 0.7612)

mean(auc_scores)

# per class accuracy score
first_values <- c(0.2988, 0.3048, 0.1909, 0.3570, 0.3408, 
                  0.2012, 0.3707, 0.3408, 0.2988, 0.3108, 
                  0.3305, 0.3228, 0.2885, 0.2526, 0.2603, 0.2757)

second_values <- c(0.9693, 0.9632, 0.9816, 0.9387,
                   0.9509, 0.9816, 0.9325, 0.9509, 
                   0.9632, 0.9693, 0.9571, 0.9632, 
                   0.9693, 0.9755, 0.9693, 0.9693)


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
