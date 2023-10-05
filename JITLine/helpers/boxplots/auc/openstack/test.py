import matplotlib.pyplot as plt


#SMOTE fixed
group1 = [
    0.8272, 0.8272, 0.8272, 0.8272, 0.8272, 0.8272, 0.8272, 0.8272,
    0.8272, 0.8272, 0.8272, 0.8272, 0.8272, 0.8272, 0.8272, 0.8272
]

# Group 1: SMOTE NI ON
group2 = [
    0.8249, 0.8319, 0.8229, 0.8253, 0.8247, 0.8239, 0.8342, 0.8237,
    0.8269, 0.8217, 0.8243, 0.8274, 0.8231, 0.8233, 0.8210, 0.8289
]



# Boxplot for group1 and group2
# Combine the data into a list
data = [group1, group2]

# Labels for the groups
labels = ['Fixed', 'with NI-Factors']

# Create a side-by-side boxplot
plt.boxplot(data, labels=labels)

# Add title and axis labels
plt.title('AUC-Score')
plt.xlabel('Openstack dataset')
plt.ylabel('')

# Show the plot
plt.grid(True)
plt.show()