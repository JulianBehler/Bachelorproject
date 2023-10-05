import matplotlib.pyplot as plt

#SMOTE QT NI Factors on
group1 = [0.8167, 0.8100, 0.8093, 0.8110, 0.8055, 0.8132, 0.8208, 0.8152,
          0.8144, 0.8129, 0.8126, 0.8096, 0.8104, 0.8092, 0.8118, 0.8135]

#ROS NI Factors on
group2 = [0.8209, 0.8174, 0.8194, 0.8149, 0.8121, 0.8118, 0.8171, 0.8191,
          0.8173, 0.8207, 0.8197, 0.8169, 0.8163, 0.8096, 0.8224, 0.8162]

#RUS NI Factors on
group3 = [0.8067, 0.8072, 0.8021, 0.8030, 0.8047, 0.8033, 0.8128, 0.8095,
          0.8077, 0.8046, 0.8072, 0.8123,0.8045, 0.8050, 0.8124, 0.8099]

# Boxplot for group1 and group2
# Combine the data into a list
data = [group1, group2, group3]

# Labels for the groups
labels = ['SMOTE', 'RandomOverSampler', 'RandomUnderSampler']

# Create a side-by-side boxplot
plt.boxplot(data, labels=labels)

# Add title and axis labels
plt.title('AUC-Score')
plt.xlabel('QT dataset')
plt.ylabel('')

# Show the plot
plt.grid(True)
plt.show()