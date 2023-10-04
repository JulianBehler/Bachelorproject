import matplotlib.pyplot as plt

group1 = [
    0.2165, 0.5155, 0.2240, 0.3518,
    0.2366, 0.3396, 0.2358, 0.3233,
    0.3673, 0.3304, 0.3706, 0.2102,
    0.3040, 0.3702, 0.3748, 0.5549
]


group2 = data = [
    0.2466, 0.2659, 0.3036, 0.3539,
    0.3040, 0.2546, 0.2605, 0.3011,
    0.2487, 0.3254, 0.2588, 0.2701,
    0.2760, 0.2542, 0.2563, 0.2446
]


group3 = [
    0.8266, 0.5394, 0.5331, 0.6692,
    0.6779, 0.3153, 0.2596, 0.2668,
    0.3266, 0.3266, 0.7274, 0.6633,
    0.7462, 0.7269, 0.2592, 0.7998
]
group4 = [
    0.8882, 0.8865, 0.8827, 0.9171,
    0.8886, 0.9229, 0.9347, 0.8957,
    0.8861, 0.9363, 0.8920, 0.9079,
    0.9246, 0.9087, 0.9560, 0.9527
]

data = [group1, group2, group3, group4]


labels = ['Default', 'ROS', 'RUS','SMOTE']

# Create a side-by-side boxplot
plt.boxplot(data, labels=labels)

# Add title and axis labels
plt.title('Per-class score 0')
plt.xlabel('QT dataset')
plt.ylabel('')

# Show the plot
plt.grid(True)
plt.show()