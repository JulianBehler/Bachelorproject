import matplotlib.pyplot as plt

# per-class score from SMOTE NI On
data1 = [
    [0.9452, 0.3129],
    [0.9486, 0.3006],
    [0.9478, 0.2822],
    [0.9503, 0.3006],
    [0.9503, 0.2945],
    [0.9503, 0.2883],
    [0.9495, 0.2775],
    [0.9521, 0.2883],
    [0.9503, 0.3252],
    [0.9435, 0.3006],
    [0.9562, 0.2761],
    [0.9491, 0.2627],
    [0.9529, 0.3006],
    [0.9453, 0.3074],
    [0.9512, 0.2761],
    [0.9478, 0.2638]
]

# per class data from roandomoversampler
data2 = [
    [0.9606, 0.2699],
    [0.9598, 0.2699],
    [0.9632, 0.2454],
    [0.9615, 0.2638],
    [0.9598, 0.2699],
    [0.9598, 0.2699],
    [0.9615, 0.2822],
    [0.9589, 0.2822],
    [0.9598, 0.2699],
    [0.9606, 0.2761],
    [0.9606, 0.2515],
    [0.9598, 0.2822],
    [0.9615, 0.2577],
    [0.9589, 0.2270],
    [0.9623, 0.2699],
    [0.9606, 0.2699]
]

#RandomUnderSampler
data3 = [
    [0.7406, 0.7178],
    [0.7440, 0.7423],
    [0.7432, 0.7730],
    [0.7483, 0.7239],
    [0.7432, 0.7546],
    [0.7534, 0.7301],
    [0.7474, 0.7178],
    [0.7483, 0.7485],
    [0.7483, 0.6871],
    [0.7466, 0.7423],
    [0.7286, 0.7239],
    [0.7483, 0.7546],
    [0.7329, 0.7546],
    [0.7432, 0.7301],
    [0.7483, 0.6933],
    [0.7663, 0.7117]
]


# Separate values into classZero
smoteClassOne  = [pair[1] for pair in data1]
rosClassOne   = [pair[1] for pair in data2]
rusClassOne    = [pair[1] for pair in data3]

# Boxplot for group1 and group2
# Combine the data into a list
data = [smoteClassOne, rosClassOne, rusClassOne]

# Labels for the groups
labels = ['Smote', 'ROS', 'RUS']

# Create a side-by-side boxplot
plt.boxplot(data, labels=labels)

# Add title and axis labels
plt.title('Per-class score 1')
plt.xlabel('Openstack dataset')
plt.ylabel('')

# Show the plot
plt.grid(True)
plt.show()