x = [34,46,43,27,57,41,45,21,70]
print("Before sorting:",x)
bubblesort(x)
print("After sorting:",x)
x=list(range(1,10000))
plt.plot(x,[y*y for y in x] )
plt.title("Bubble sort- Time Complexity is O(n)")
plt.xlabel("Input")
plt.ylabel("Time")
plt.show()