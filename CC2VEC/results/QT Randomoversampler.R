#QT Randomoversampler

#calc the mean/avg

auc_accuracy <- c(0.8201, 0.8251, 0.8223, 0.8283,
                  0.8197, 0.8229, 0.8140, 0.8230,
                  0.8139, 0.8226, 0.8199, 0.8224,
                  0.8196, 0.8192, 0.8136, 0.8201)


runtime_accuracy <- c(4645.9180,  4633.2060,  4629.9670,  4483.9510,
                      4435.2520,  4386.1890,  4396.3210,  4383.1260,
                      4401.2130,  4387.2200,  4388.1040,  4642.0430,
                      4553.2350,  4385.0770,  4389.8470,  4498.3200)

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
first_values <- c(0.2466, 0.2659, 0.3036, 0.3539,
                  0.3040, 0.2546, 0.2605, 0.3011,
                  0.2487, 0.3254, 0.2588, 0.2701,
                  0.2760, 0.2542, 0.2563, 0.2446)

second_values <- c(
  0.9781, 0.9781, 0.9672, 0.9781,
  0.9727, 0.9781, 0.9727, 0.9617,
  0.9781, 0.9617, 0.9727, 0.9617,
  0.9727, 0.9727, 0.9781, 0.9727
  
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