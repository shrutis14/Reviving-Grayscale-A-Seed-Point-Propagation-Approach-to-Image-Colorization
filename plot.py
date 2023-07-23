import matplotlib.pyplot as plt

# Define the categories and the number of images in each category
categories = ['garden', 'wave', 'house', 'barn', 'road']
num_images1 = [10, 20, 15, 5, 30]
num_images2 = [5, 10, 20, 25, 15]

# Plot the first line graph
plt.plot(categories, num_images1, marker='o', label='Cheng model')

# Plot the second line graph
plt.plot(categories, num_images2, marker='o', label='Our model')

# Add labels and title
plt.xlabel('Scene classes')
plt.ylabel('PSNR')
plt.title('PSNR values for scene categories')

# Add a legend
plt.legend()

# Show the plot
plt.show()

