import matplotlib.pyplot as plt
# line 1 points
x1 = [1000,25000,50000,100000]
y1 = [17147,368218,723517,1433913]
# plotting the line 1 points
plt.plot(x1, y1, label = "Quicksort")

# line 2 points
x2 = [1000,25000,50000,100000]
y2 = [23140,483728,889400,1942870]
# plotting the line 2 points
plt.plot(x2, y2, label = "Merge Sort")

# line 3 points
x3 = [1000,25000,50000,100000]
y3 = [134398,722663,2782445,11620617]
# plotting the line 3 points
plt.plot(x3, y3, label = "Selection Sort")

# line 4 points
x4 = [1000,25000,50000,100000]
y4 = [84833,552663,1782445,6379526]
# plotting the line 4 points
plt.plot(x4, y4, label = "Insertion Sort")

# naming the x axis
plt.xlabel('input size (N)')
# naming the y axis
plt.ylabel('Execution Time (microsec)')
# giving a title to my graph
plt.title("Sorting Algorithms")

# show a legend on the plot
plt.legend()
# function to show the plot
plt.show()
