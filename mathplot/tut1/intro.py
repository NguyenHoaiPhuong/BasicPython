import matplotlib.pyplot as plt

def single_plot():
    x = [1, 2, 3, 4]
    y = [10, 11, 12, 13]
    plt.plot(x, y)
    plt.xlabel("Time (s)")
    plt.ylabel("Heap In Used (GiB)")
    plt.show()

def multi_plot():
    x = [1, 2, 3, 4]
    y = [10, 11, 12, 13]
    z = [20, 21, 22, 23]
    plt.plot(x, y)
    plt.plot(x, z)
    plt.xlabel("Time (s)")
    plt.ylabel("Heap In Used (GiB)")
    plt.show()

def axis_format():
    import math
    x = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]
    y1 = []
    y2 = []
    y3 = []
    for i in x:
        y1.append(math.sin(i))
        y2.append(math.cos(i))
        y3.append(math.tan(i))

    plt.axis([0, 1, 0, 2])
    plt.plot(x, y1, 'b^')    # b = blue, ^ = triangle
    plt.plot(x, y2, 'gs')    # g = green, s = square
    plt.plot(x, y3, 'r--')    # g = green, --
    plt.xlabel("Time (s)")
    plt.ylabel("Heap In Used (GiB)")
    plt.show()