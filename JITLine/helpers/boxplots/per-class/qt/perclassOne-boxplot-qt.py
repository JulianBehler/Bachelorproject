import matplotlib.pyplot as plt

# per-class score from SMOTE NI On
data1 = [
    [0.9816, 0.1694],
    [0.9849, 0.1475],
    [0.9816, 0.1694],
    [0.9820, 0.1585],
    [0.9824, 0.1585],
    [0.9816, 0.1694],
    [0.9812, 0.1639],
    [0.9820, 0.1639],
    [0.9832, 0.1674],
    [0.9807, 0.1803],
    [0.9828, 0.1639],
    [0.9799, 0.1803],
    [0.9816, 0.1639],
    [0.9816, 0.1694],
    [0.9803, 0.1803],
    [0.9807, 0.1672]
]

# per class data from roandomoversampler
data2 = [
    [0.9870, 0.1093],
    [0.9879, 0.1093],
    [0.9874, 0.1148],
    [0.9879, 0.1093],
    [0.9870, 0.1202],
    [0.9887, 0.1093],
    [0.9891, 0.1202],
    [0.9887, 0.1148],
    [0.9883, 0.1148],
    [0.9895, 0.1148],
    [0.9874, 0.1093],
    [0.9866, 0.1148],
    [0.9870, 0.1202],
    [0.9887, 0.1148],
    [0.9887, 0.1202],
    [0.9870, 0.1038]
]

#randomundersampler
data3 = [
    [0.8208, 0.6066],
    [0.8271, 0.6011],
    [0.8095, 0.6230],
    [0.8082, 0.6339],
    [0.8304, 0.5956],
    [0.8237, 0.5902],
    [0.8229, 0.6066],
    [0.8229, 0.6011],
    [0.8208, 0.6230],
    [0.8191, 0.6066],
    [0.8245, 0.6120],
    [0.8271, 0.6066],
    [0.8090, 0.6120],
    [0.8187, 0.6066],
    [0.8208, 0.6066],
    [0.8308, 0.6066]
]

# Separate values into classZero
smoteClassZero      = [pair[1] for pair in data1]
rosClassZero        = [pair[1] for pair in data2]
rusClassZero        = [pair[1] for pair in data3]


# Boxplot for group1 and group2
# Combine the data into a list
data = [smoteClassZero, rosClassZero, rusClassZero]

# Labels for the groups
labels = ['Smote', 'ROS', 'RUS']

# Create a side-by-side boxplot
plt.boxplot(data, labels=labels)

# Add title and axis labels
plt.title('Per-class score 1')
plt.xlabel('QT dataset')
plt.ylabel('')

# Show the plot
plt.grid(True)
plt.show()