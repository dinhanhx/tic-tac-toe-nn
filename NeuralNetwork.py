from keras.models import Sequential
from keras.layers import Dense
from keras.utils import to_categorical
import pickle
import numpy as np

# Get training history
training_history = None
with open('training_history.pkl', 'rb') as f:
    training_history = pickle.load(f)

# Convert to numpy array
move_history = np.array([i[0] for i in training_history])
board_result = np.array([i[1] for i in training_history])

# Make food for neural network
X = move_history.reshape((len(training_history), 3*3))
Y = to_categorical(board_result, num_classes = 3)

boundary = int(0.8 * len(X))

X_train = X[:boundary]
Y_train = Y[:boundary]

X_valid = X[boundary:]
Y_valid = Y[boundary:]

# Make neural network
smort = Sequential()

smort.add(Dense(64, activation = 'relu', input_shape = (3*3,)))
smort.add(Dense(128, activation = 'relu'))
smort.add(Dense(128, activation = 'relu'))
smort.add(Dense(128, activation = 'relu'))
smort.add(Dense(3, activation = 'softmax'))

smort.compile(loss='categorical_crossentropy', optimizer='rmsprop', metrics=['accuracy'])

# Train the neural network
smort.fit(X_train, Y_train, validation_data=(X_valid, Y_valid), epochs = 128, batch_size = 32)

smort.save('smort')
