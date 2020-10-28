import pickle
import numpy as np
from keras.models import load_model
from keras.utils import to_categorical

# Get training history
training_history = None
with open('TEST_training_history.pkl', 'rb') as f:
    training_history = pickle.load(f)

# Convert to numpy array
move_history = np.array([i[0] for i in training_history])
board_result = np.array([i[1] for i in training_history])

# Make food for neural network
X = move_history.reshape((len(training_history), 3*3))
Y = to_categorical(board_result, num_classes = 3)

smort = load_model('smort')

test_loss, test_acc = smort.evaluate(X, Y)
print(test_loss, test_acc)
