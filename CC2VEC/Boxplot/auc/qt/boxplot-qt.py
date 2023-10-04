import matplotlib.pyplot as plt

group1 = [
    0.8150, 0.8142, 0.8133, 0.8089,
    0.8142, 0.8082, 0.8127, 0.8071,
    0.8132, 0.8134, 0.8135, 0.8122,
    0.8083, 0.8076, 0.8142, 0.8145
]


group2 = data = [
    0.8201, 0.8251, 0.8223, 0.8283,
    0.8197, 0.8229, 0.8140, 0.8230,
    0.8139, 0.8226, 0.8199, 0.8224,
    0.8196, 0.8192, 0.8136, 0.8201
]


group3 = [
    0.7725, 0.7733, 0.7731, 0.7770,
    0.7765, 0.7767, 0.7802, 0.7789,
    0.7761, 0.7730, 0.7759, 0.7727,
    0.7797, 0.7728, 0.7797, 0.7767
]

group4 = [
    0.7456, 0.7450, 0.7425, 0.7423,
    0.7355, 0.7324, 0.7273, 0.7326,
    0.7350, 0.7248, 0.7363, 0.7337,
    0.7360, 0.7375, 0.7204, 0.7221
]

data = [group1, group2, group3, group4]


labels = ['Default', 'ROS', 'RUS','SMOTE']

# Create a side-by-side boxplot
plt.boxplot(data, labels=labels)

# Add title and axis labels
plt.title('AUC-Score')
plt.xlabel('QT dataset')
plt.ylabel('')

# Show the plot
plt.grid(True)
plt.show()