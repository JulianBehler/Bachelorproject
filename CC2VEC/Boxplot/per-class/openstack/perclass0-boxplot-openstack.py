import matplotlib.pyplot as plt



group1 = [
    0.2988, 0.3048, 0.1909, 0.3570, 0.3408,
    0.2012, 0.3707, 0.3408, 0.2988, 0.3108,
    0.3305, 0.3228, 0.2885, 0.2526, 0.2603, 0.2757
]


group2 = data = [
    0.2226, 0.2611, 0.2346, 0.2620, 0.2397,
    0.1858, 0.2235, 0.2560, 0.1807, 0.2500,
    0.1952, 0.2021, 0.2072, 0.2748, 0.3253, 0.2988
]


group3 = [
    0.4435, 0.3750, 0.5188, 0.3211,
    0.4401, 0.3433, 0.4341, 0.4401,
    0.0402, 0.6747, 0.6652, 0.6601,
    0.6730, 0.4024, 0.3955, 0.4084
]
group4 = [
    0.7295, 0.9358, 0.9298, 0.9692,
    0.7748, 0.6558, 0.9084, 0.7646,
    0.9658, 0.9015, 0.7774, 0.6892,
    0.6978, 0.8801, 0.7226, 0.8750
]

data = [group1, group2, group3, group4]


labels = ['Default', 'ROS', 'RUS','SMOTE']

# Create a side-by-side boxplot
plt.boxplot(data, labels=labels)

# Add title and axis labels
plt.title('Per-class score 0')
plt.xlabel('Openstack dataset')
plt.ylabel('')

# Show the plot
plt.grid(True)
plt.show()