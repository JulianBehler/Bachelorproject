#Openstack Randomoversampler

#calc the mean/avg

auc_accuracy <- c(0.7724, 0.7754, 0.7785, 
                  0.7767, 0.7753, 0.7759, 
                  0.7821, 0.7693, 0.7757, 
                  0.7762, 0.7768, 0.7768, 
                  0.7755, 0.7828, 0.7821, 
                  0.7814)

runtime_accuracy <- c(2002.24,
                      1986.35 ,
                      1997.56,
                      1987.46,
                      1988.35, 
                      1999.33, 
                      1932.40, 
                      1965.69, 
                      2012.67, 
                      1999.23, 
                      1992.832, 
                      1978.942, 
                      1978.644, 
                      1987.33, 
                      2001.32, 
                      1977.834 )
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





mean(auc_scores)

# per class accuracy score
first_values <- c(0.2226, 0.2611, 0.2346, 0.2620, 0.2397,
                  0.1858, 0.2235, 0.2560, 0.1807, 0.2500, 
                  0.1952, 0.2021, 0.2072, 0.2748, 0.3253, 0.2988)

second_values <- c(0.9632, 0.9755, 0.9755, 0.9693, 0.9755, 
                   0.9755, 0.9755, 0.9755, 0.9816, 0.9693,
                   0.9816, 0.9816, 0.9816, 0.9632, 0.9632, 0.9632)



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
