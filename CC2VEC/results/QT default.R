#QT default

#calc the mean/avg

auc_accuracy <- c(0.8150, 0.8142, 0.8133, 0.8089,
                  0.8142, 0.8082, 0.8127, 0.8071,
                  0.8132, 0.8134, 0.8135, 0.8122,
                  0.8083, 0.8076, 0.8142, 0.8145)


runtime_accuracy <- c(2356.63  , 2343.832  , 2340.653  ,  2342.59,
                      2347.238 , 2343.174   , 2339.322   , 2345.854,
                      2344.674 , 2343.765  ,  2345.33  ,   2350.723,
                      2345.561 ,   2349.221   , 2350.007   , 2344.555)

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
first_values <- c(0.2165,0.5155,0.2240, 0.3518,
                  0.2366,0.3396,0.2358,0.3233,
                  0.3673,0.3304, 0.3706,0.2102,
                  0.3040,0.3702,0.3748,0.5549
)

second_values <- c(
  0.9836,   0.8962,   0.9727,   0.9508,
  0.9727 ,  0.9563,   0.9727 ,  0.9563,
  0.9508,   0.9617   ,0.9563  , 0.9781,
  0.9672  , 0.9508  , 0.9563 ,  0.8634
)


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