import matplotlib.pyplot as plt

# Group 1: SMOTE NI ON
group1 = [
    0.8249, 0.8319, 0.8229, 0.8253, 0.8247, 0.8239, 0.8342, 0.8237,
    0.8269, 0.8217, 0.8243, 0.8274, 0.8231, 0.8233, 0.8210, 0.8289
]

# Group 2: ros-openstack NI ON
group2 = data = [
    0.8279, 0.8300, 0.8276, 0.8261, 0.8230, 0.8300, 0.8313, 0.8253,
    0.8230, 0.8278, 0.8273, 0.8229, 0.8277, 0.8278, 0.8294, 0.8284
]

#RUS NI Factors on
group3 = [
    0.8126, 0.8195, 0.8213, 0.8195, 0.8176, 0.8192,0.8157, 0.8187,
    0.8123, 0.8184, 0.8193, 0.8240,0.8180, 0.8259, 0.8177, 0.8201
]

# Boxplot for group1 and group2
# Combine the data into a list
data = [group1, group2, group3]

# Labels for the groups
labels = ['SMOTE', 'RandomOverSampler', 'RandomUnderSampler']

# Create a side-by-side boxplot
plt.boxplot(data, labels=labels)

# Add title and axis labels
plt.title('AUC-Score')
plt.xlabel('Openstack dataset')
plt.ylabel('')

# Show the plot
plt.grid(True)
plt.show()