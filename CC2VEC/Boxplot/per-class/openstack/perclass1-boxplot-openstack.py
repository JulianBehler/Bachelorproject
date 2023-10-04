import matplotlib.pyplot as plt

# per-class score from SMOTE NI On
# Group 1: SMOTE NI ON
group1 = [
    0.9693, 0.9632, 0.9816, 0.9387,
    0.9509, 0.9816, 0.9325, 0.9509,
    0.9632, 0.9693, 0.9571, 0.9632,
    0.9693, 0.9755, 0.9693, 0.9693
]

# Group 2: ros-openstack NI ON
group2 = data = [
    0.9632, 0.9755, 0.9755, 0.9693, 0.9755,
    0.9755, 0.9755, 0.9755, 0.9816, 0.9693,
    0.9816, 0.9816, 0.9816, 0.9632, 0.9632, 0.9632

]

#RUS NI Factors on
group3 = [
    0.9202, 0.9448, 0.8712, 0.9509,
    0.9202, 0.9509, 0.9202, 0.9202,
    0.9939, 0.6626, 0.7117, 0.7178,
    0.6810, 0.9325, 0.9387, 0.9202
]
group4 = [
    0.5951, 0.1902, 0.2147, 0.1043,
    0.4540, 0.6748, 0.2515, 0.5215,
    0.1043, 0.2577, 0.4540, 0.6012,
    0.6074, 0.3436, 0.5521, 0.3497
]
# Boxplot for group1 and group2
# Combine the data into a list
data = [group1, group2, group3, group4]

# Labels for the groups
labels = ['Default', 'ROS', 'RUS','SMOTE']
# Create a side-by-side boxplot
plt.boxplot(data, labels=labels)

# Add title and axis labels
plt.title('Per-class score 1')
plt.xlabel('Openstack dataset')
plt.ylabel('')

# Show the plot
plt.grid(True)
plt.show()