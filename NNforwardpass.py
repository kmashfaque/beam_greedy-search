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


def train_linear_model(
    x,
    y_true,
    weights,
    learning_rate=0.01,
    steps=10
):
    """
    Trains a simple linear model using gradient descent
    and prints progress at each step.
    """

    def predict(x, w):
        return np.dot(x, w)

    def mse_loss(y_pred, y_true):
        return (y_pred - y_true) ** 2

    def compute_gradient(x, y_pred, y_true):
        error = y_pred - y_true
        return 2 * x * error

    print("Initial weights:", weights)
    print("-" * 50)

    for step in range(steps):
        # forward pass
        prediction = predict(x, weights)

        # loss
        loss = mse_loss(prediction, y_true)

        # gradient (RECOMPUTED every step)
        gradient = compute_gradient(x, prediction, y_true)

        # weight update
        weights = weights - learning_rate * gradient

        # progress print
        print(f"Step {step+1}")
        print("Prediction :", prediction)
        print("Loss       :", loss)
        print("Gradient   :", gradient)
        print("Weights    :", weights)
        print("-" * 50)

    return weights


input_data = np.array([0, 3])
target = 50
weights = np.array([-1.0, 3.0])

final_weights = train_linear_model(
    input_data,
    target,
    weights,
    learning_rate=0.01,
    steps=10
)
