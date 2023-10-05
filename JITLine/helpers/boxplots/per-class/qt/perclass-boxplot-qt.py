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

# Separate values into classZero and classOne arrays
smoteClassZero = [pair[0] for pair in data1]
smoteClassOne = [pair[1] for pair in data1]


# Printing the results
print("classZero:", smoteClassZero)
print("classOne:", smoteClassOne)


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

# Separate values into classZero and classOne arrays
rosClassZero = [pair[0] for pair in data2]
rosClassOne = [pair[1] for pair in data2]

# Printing the results
print("classZero:", rosClassZero)
print("classOne:", rosClassOne)

# Boxplot for group1 and group2
# Combine the data into a list
data = [smoteClassZero, smoteClassOne, rosClassZero, rosClassOne]

# Labels for the groups
labels = ['Smote class 0', 'Smote class 1', 'ROS class 0', 'ROS class 1']

# Create a side-by-side boxplot
plt.boxplot(data, labels=labels)

# Add title and axis labels
plt.title('Per-class score')
plt.xlabel('QT dataset')
plt.ylabel('')

# Show the plot
plt.grid(True)
plt.show()