def gradient_descent(x, learning_rate, steps):
    for _ in range(steps):
        x = x-learning_rate*(2*x)
    return x
x = 4
learning_rate = 0.1
steps = 100
print(gradient_descent(x, learning_rate, steps))