#QT Randomundersampler

#calc the mean/avg

auc_accuracy <- c(0.7725, 0.7733, 0.7731, 0.7770,
                  0.7765, 0.7767, 0.7802, 0.7789,
                  0.7761, 0.7730, 0.7759, 0.7727,
                  0.7797, 0.7728, 0.7797, 0.7767)


runtime_accuracy <- c(419.811, 401.485, 402.862, 401.358,
                      406.937, 401.873, 403.752, 404.943,
                      406.66, 403.675, 408.785, 409.55,
                      420.702, 435.204, 408.328, 411.429)

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
first_values <- c(0.8266, 0.5394, 0.5331, 0.6692,
                  0.6779, 0.3153, 0.2596, 0.2668,
                  0.3266, 0.3266, 0.7274, 0.6633,
                  0.7462, 0.7269, 0.2592, 0.7998)

second_values <- c(
  0.5738, 0.8579, 0.8579, 0.7596,
  0.7541, 0.9289, 0.9563, 0.9399,
  0.9289, 0.9289, 0.7049, 0.7650,
  0.6940, 0.7049, 0.9563, 0.6448
  
)


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