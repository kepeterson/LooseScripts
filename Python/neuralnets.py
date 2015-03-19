import math, random


class Unit:
    def __init__(self, value, grad):
        self.value = value
        self.grad = grad

    def __str__(self):
        #s1, s2 = (str(self.value), str(self.grad))
        s1 = str(self.value)
        s2 = str(self.grad)
        return 'Value: %s Grad: %s' % (s1, s2)


class AddGate:
    def forward(self, u0, u1):
        self.u0 = u0
        self.u1 = u1
        self.utop = Unit(u0.value + u1.value, 0.0)
        return self.utop

    def backward(self):
        self.u0.grad += 1 * self.utop.grad
        self.u1.grad += 1 * self.utop.grad


class MultiplyGate:
    def forward(self, u0, u1):
        self.u0 = u0
        self.u1 = u1
        self.utop = Unit(u0.value * u1.value, 0.0)
        return self.utop

    def backward(self):
        self.u0.grad += self.u0.value * self.utop.grad
        self.u1.grad += self.u1.value * self.utop.grad


class Circuit:
    def __init__(self):
        self.mulg0 = MultiplyGate()
        self.mulg1 = MultiplyGate()
        self.addg0 = AddGate()
        self.addg1 = AddGate()

    def forward(self, x, y, a, b, c):
        self.ax = self.mulg0.forward(a, x)
        self.by = self.mulg1.forward(b, y)
        self.axpby = self.addg0.forward(self.ax, self.by)
        self.axpbypc = self.addg1.forward(self.axpby, c)
        return self.axpbypc

    def backward(self, gradient_top):
        self.axpbypc.grad = gradient_top
        self.addg1.backward()
        self.addg0.backward()
        self.mulg1.backward()
        self.mulg0.backward()


class SVM:
    def __init__(self):
        self.a = Unit(1.0, 0.0)
        self.b = Unit(-2.0, 0.0)
        self.c = Unit(-1.0, 0.0)
        self.circuit = Circuit()

    def forward(self, x, y):
        self.unit_out = self.circuit.forward(x, y, self.a,
                                             self.b, self.c)
        return self.unit_out

    def backward(self, label):
        self.a.grad = 0.0
        self.b.grad = 0.0
        self.c.grad = 0.0

        pull = 0.0
        if label == 1.0 and self.unit_out.value < 1.0:
            pull = 1.0
        elif label == -1.0 and self.unit_out.value > 1.0:
            pull = -1.0

        self.circuit.backward(pull)

        self.a.grad += -self.a.value
        self.b.grad += -self.b.value

    def learn_from(self, x, y, label):
        self.forward(x, y)
        self.backward(label)
        self.parameter_update()

    def parameter_update(self):
        step_size = .01
        self.a.value += step_size * self.a.grad
        self.b.value += step_size * self.b.grad
        self.c.value += step_size * self.c.grad


data = []

data.append((1.2, .7, 1))
data.append((-.3, -.5, -1))
data.append((3., .1, 1))
data.append((-.1, -1., -1))
data.append((-1., 1.1, -1))
data.append((2.1, -3., 1))

svm = SVM()


def eval_training_accuracy():
    num_correct = 0
    for a, b, answer in data:
        x = Unit(a, 0.)
        y = Unit(b, 0.)

        if svm.forward(x, y).value > 0:
            predicted_label = 1
        else:
            predicted_label = -1

        if predicted_label == answer:
            num_correct += 1

    return float(num_correct)/len(data)

for run in xrange(400):
    i = math.floor(random.random() * len(data)).__int__()
    x = Unit(data[i][0], 0.)
    y = Unit(data[i][1], 0.)
    label = data[i][2]
    svm.learn_from(x, y, label)

    if run % 25 == 0:
        accuracy = eval_training_accuracy()
        s = "accuracy at run {0}: {1}".format(run, accuracy)
        print(s)
