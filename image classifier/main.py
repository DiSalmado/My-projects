
import glob
import os
import numpy as np
from PIL import Image
from sklearn import preprocessing, svm
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt

## Path to the folder you wish to import
image_folder_path = r"C:\Users\Alberto\Documents\VS Code\Projectos\Projectos para portafolio\image classifier\tf_files\star_wars"

# Load and normalize our data
X_train, X_test = list(), list()
for img_name in glob.glob(os.path.join(image_folder_path, "*.jpg")):
    if img_name.split('star_wars\\')[-1][0].isdigit():
        label = int(img_name.split('star_wars\\')[-1][0])
        img_array = np.array(Image.open(img_name))
    if len(img_array.shape) == 2:
        img_array = img_array.reshape(-1, 1)

# Reshape the arrays into 2D
        img_shape = img_array.shape
        if len(img_shape) == 3:
            img_array = img_array.reshape(img_shape[0], img_shape[1] * img_shape[2])
        else:
            img_array = img_array.reshape(img_shape[0], img_shape[1])

# Scale the data
        img_array = preprocessing.scale(img_array).reshape(-1,1)
        X_train = np.append(X_train, img_array)
        X_test.append(label)

# Check if there are any samples in X_train and X_test
if len(X_train) == 0 or len(X_test) == 0:
    print('Error: X_train and X_test must have at least 1 sample each')
    exit()

X_train = np.array(X_train)
Y_test = np.array(X_test)

# Split data into training and testing groups
if len(X_train) != len(X_test):
    minLen = min(len(X_train), len(Y_test))
    X_train = X_train[:minLen]
    Y_test = Y_test[:minLen]
x_train, x_test, y_train, y_test = train_test_split(X_train, X_test, test_size=0.1)

# Create an image classifier using support vector machines
clf = svm.SVC(kernel='linear')
clf.fit(x_train, y_train)

# Run the classifier on the test data and save the predicted labels
predictions = clf.predict(x_test)
accuracy = accuracy_score(y_test, predictions)

# Plot the results
plt.scatter(y_test, predictions)
plt.xlabel('Actual Labels')
plt.ylabel('Predicted Labels')
ticks = ['vader', 'luke', 'yoda']
plt.xticks([0, 1, 2], ticks)
plt.yticks([0, 1, 2], ticks)
titleText = 'Image Classifier Accuracy: {0:.2f}%'.format(accuracy*100)
plt.title(titleText)
plt.show()