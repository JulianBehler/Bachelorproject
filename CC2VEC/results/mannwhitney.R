#install.packages("exactRankTests")
#library(exactRankTests)


gruppe1 <- c(0.7632, 0.7647, 0.7610, 0.7622, 
             0.7611, 0.7606, 0.7613, 0.7611,
             0.7650, 0.7678, 0.7670, 0.7667, 
             0.7617, 0.7598, 0.7622, 0.7612)
gruppe2 <- c(0.7724, 0.7754, 0.7785, 
             0.7767, 0.7753, 0.7759, 
             0.7821, 0.7693, 0.7757, 
             0.7762, 0.7768, 0.7768, 
             0.7755, 0.7828, 0.7821, 
             0.7814)

# Mann-Whitney U-Test durchführen
result <- wilcox.exact(gruppe1, gruppe2)

# Ausgabe der Testergebnisse
cat("Mann-Whitney U-Test Ergebnisse:\n")
cat("Teststatistik U:", result$statistic, "\n")
cat("P-Wert:", result$p.value, "\n")

# Interpretation des P-Werts
if (result$p.value < 0.05) {
  cat("Es gibt einen signifikanten Unterschied zwischen den Gruppen.\n")
} else {
  cat("Es gibt keinen signifikanten Unterschied zwischen den Gruppen.\n")
}