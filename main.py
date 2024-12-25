import matplotlib.pyplot as plt
from numpy import exp, linspace



def f(x,y):
    return y

number_of_iterations = 6
x_list = []
y_list = []
initial_condition_x = 0
initial_condition_y=1
step_size= 0.5

x=initial_condition_x
y=initial_condition_y

for i in range(number_of_iterations):

    x_list.append(x)
    y_list.append(y)
    y += step_size*f(x,y)
    x +=step_size
    

true_x = linspace(x_list[0],x_list[-1])
true_y = exp(true_x)

plt.plot(x_list,y_list)
plt.plot(true_x,true_y)

plt.show()