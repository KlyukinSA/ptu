from numpy import array, average, full, argmin, linspace, pi, sin, cos
from numpy.random import rand
from numpy.linalg import eig, norm
import matplotlib.pyplot as plt

def rotate_randomly(x):
    a = rand(len(x), len(x))
    _, v = eig(a)
    return v @ x

def show_current_step_scatter(step, pop, func, scatter_choser):
    if scatter_choser(step):
        plt.scatter(pop[0], pop[1], c=func(pop), cmap='copper')
        plt.colorbar()
        plt.title('step = {}'.format(step))
        plt.show()

def opt_hyrax(func, x, initial_spread,
        n_steps, n_agents,
        scatter_choser=lambda step: 0,
        method='scale'):
    pop_shape = (len(x), n_agents)
    pop = initial_spread * (rand(*pop_shape) - full(pop_shape, 0.5))
    for i in range(n_agents):
        pop[:, i] += x
    if method == 'scale':
        leader_pos = argmin(func(pop))
        for step in range(n_steps):
            show_current_step_scatter(step, pop, func, scatter_choser)
            leader = rand() * pop[:, leader_pos]
            for i in range(n_agents):
                pop[:, i] = rand() * pop[:, i] - leader
            leader_pos = argmin(func(pop))
        return pop[:, leader_pos]
    elif method == 'rotate':
        old_leader = x
        for step in range(n_steps):
            show_current_step_scatter(step, pop, func, scatter_choser)
            leader = pop[:, argmin(func(pop))]
            for i in range(n_agents):
                pop[:, i] = rand() * rotate_randomly(pop[:, i] - old_leader) + leader
            old_leader = leader
        return old_leader
    else:
        raise Exception('no such method')

def sphere(x):
    return (x[0] - 1.0)**2 + (x[1] - 1.0)**2

def rosenbrock(x):
    return (x[0] - 1.0)**2 + 100.0 * (x[1] - x[0]**2)**2

def valley_sphere(x):
    return (x[0] - 1.0)**2 + 3000 * (x[1] - x[0])**2

x_true = array([1.0, 1.0])

def repeat(n_times, f): 
    for _ in range(n_times): 
        yield f() 

def print_methods_functions_table(averaging_size=3, n_steps=5, n_agents=30, scatter_choser=lambda step: step % 2 == 0):
    x = array([3.0, 5.0])
    initial_spread = 8.0
    for method in 'scale', 'rotate':
        for func in sphere, rosenbrock:
            x_predicted = average(list(repeat(averaging_size, lambda: opt_hyrax(func, x, initial_spread, n_steps, n_agents, scatter_choser, method))), 0)
            print(method, func.__name__, x_predicted, norm(x_predicted - x_true))

def show_methods_prediction_scatter(n_predictions=100, n_steps=10, n_agents=100, scatter_choser=lambda step: False, func=rosenbrock, valley_func=lambda x: x**2):
    x = array([0.0, 0.0])
    initial_spread = 40.0
    for method in 'scale', 'rotate':
        predictions = array(list(repeat(n_predictions, lambda: opt_hyrax(func, x, initial_spread, n_steps, n_agents, scatter_choser, method)))).reshape(2, -1)

        plt.scatter(predictions[0], predictions[1], c=func(predictions), cmap='copper')
        plt.colorbar()
        plt.title('method = {}, func = {}'.format(method, func.__name__))

        valley_x = linspace(-4, 4, 20)
        plt.plot(valley_x, valley_func(valley_x))

        plt.show()

def print_methods_functions_article_table():
    article_averaging_size = 30
    article_n_steps = 1000
    article_n_agents = 50
    print_methods_functions_table(article_averaging_size, article_n_steps, article_n_agents, scatter_choser=lambda step: False)

def print_different_funcs_preds():
    def powell_sum(x):
        return abs(x[0])**2 + abs(x[1])**3 + abs(x[2])**4

    x_predicted = average(list(repeat(10, lambda: opt_hyrax(powell_sum, array([2,3,4]), 20, 20, 20, method='rotate'))), 0)
    print(x_predicted)

    def schaffer2(x):
        num = (sin((x[0]**2 * x[1]**2)**2)**2) - 0.5
        den = (1 + 0.001*(x[0]**2 * x[1]**2))**2 
        return 0.5 + num/den

    x_predicted = average(list(repeat(1, lambda: opt_hyrax(schaffer2, array([2,3]), 20, 500, 100, method='rotate'))), 0)
    print(x_predicted)

print_methods_functions_table() # and show population in some steps
print_methods_functions_article_table()
show_methods_prediction_scatter()
show_methods_prediction_scatter(func=valley_sphere, valley_func=lambda x: x)
print_different_funcs_preds()

