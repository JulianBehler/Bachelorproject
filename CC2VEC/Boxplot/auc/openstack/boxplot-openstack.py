import matplotlib.pyplot as plt

# Group 1: SMOTE NI ON
group1 = [
0.7632, 0.7647, 0.7610, 0.7622,
0.7611, 0.7606, 0.7613, 0.7611,
0.7650, 0.7678, 0.7670, 0.7667,
0.7617, 0.7598, 0.7622, 0.7612
]

# Group 2: ros-openstack NI ON
group2 = data = [
    0.7724, 0.7754, 0.7785,
    0.7767, 0.7753, 0.7759,
    0.7821, 0.7693, 0.7757,
    0.7762, 0.7768, 0.7768,
    0.7755, 0.7828, 0.7821,
    0.7814
]

#RUS NI Factors on
group3 = [
    0.7379, 0.7432, 0.7393, 0.7430,
    0.7423, 0.7429, 0.7419, 0.7408,
    0.7422, 0.7375, 0.7369, 0.7366,
    0.7363, 0.7410, 0.7407, 0.7406
]
group4 = [
    0.7265, 0.7255, 0.7229, 0.7237,
    0.7024, 0.7280, 0.7213, 0.7138,
    0.7254, 0.7222, 0.7037, 0.7162,
    0.7103, 0.7256, 0.7081, 0.7247
]
# Boxplot for group1 and group2
# Combine the data into a list
data = [group1, group2, group3, group4]

# Labels for the groups
labels = ['Default', 'ROS', 'RUS','SMOTE']

# Create a side-by-side boxplot
plt.boxplot(data, labels=labels)

# Add title and axis labels
plt.title('AUC-Score')
plt.xlabel('Openstack dataset')
plt.ylabel('')

# Show the plot
plt.grid(True)
plt.show()