import matplotlib.pyplot as plt

group1 = [
    0.9836, 0.8962, 0.9727, 0.9508,
    0.9727, 0.9563, 0.9727, 0.9563,
    0.9508, 0.9617, 0.9563, 0.9781,
    0.9672, 0.9508, 0.9563, 0.8634
]


group2 = data = [
    0.9781, 0.9781, 0.9672, 0.9781,
    0.9727, 0.9781, 0.9727, 0.9617,
    0.9781, 0.9617, 0.9727, 0.9617,
    0.9727, 0.9727, 0.9781, 0.9727
]


group3 = [
    0.5738, 0.8579, 0.8579, 0.7596,
    0.7541, 0.9289, 0.9563, 0.9399,
    0.9289, 0.9289, 0.7049, 0.7650,
    0.6940, 0.7049, 0.9563, 0.6448
]
group4 = [
    0.4098, 0.4208, 0.4262, 0.3388,
    0.3880, 0.2951, 0.2459, 0.3497,
    0.3607, 0.2404, 0.3825, 0.3279,
    0.3060, 0.3224, 0.1913, 0.2022
]

data = [group1, group2, group3, group4]


labels = ['Default', 'ROS', 'RUS','SMOTE']

# Create a side-by-side boxplot
plt.boxplot(data, labels=labels)

# Add title and axis labels
plt.title('Per-class score 1')
plt.xlabel('QT dataset')
plt.ylabel('')

# Show the plot
plt.grid(True)
plt.show()