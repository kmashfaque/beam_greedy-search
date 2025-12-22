import numpy as np

# # input data and target

# input_data = np.array([0, 3])
# target = 10

# # initialize weights
# weights = np.array([1.0, 1.0])

# learning_rate = 0.1

# # forward_pass 

# def predict(x, w):
#     return np.dot(x, w)


# # loss function

# def mse_loss(y_pred, y_true):
#     return (y_pred - y_true) ** 2

# # gradient of loss wrt weights

# def compute_gradient(x, y_pred, y_true):
#     error = y_pred - y_true
#     return 2 * x * error


# # training step

# # forward_pass
# prediction = predict(input_data, weights)

# # loss function
# loss = mse_loss(prediction, target)

# # gradient calculation
# gradient = compute_gradient(input_data, prediction, target)

# # weights update (Gradient Descent)
# weights_updated = weights - learning_rate * gradient

# # new prediction after update
# new_prediction = predict(input_data, weights_updated)

# # new loss
# new_loss = mse_loss(new_prediction, target)

# print("Initial prediction: ", prediction)
# print("Initial loss: ", loss)

# print("Gradient: ", gradient)
# print("Updated weights: ", weights_updated)

# print("New Prediction", new_prediction)
# print("New Loss: ", new_loss)


