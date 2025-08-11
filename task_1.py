import random
import math


def sphere_function(x):
    return sum(xi**2 for xi in x)


def hill_climbing(func, bounds, iterations=1000, epsilon=1e-6, step_size=0.1):

    current = [random.uniform(b[0], b[1]) for b in bounds]
    current_value = func(current)

    for _ in range(iterations):
        candidate = [
            max(
                min(current[i] + random.uniform(-step_size, step_size), bounds[i][1]),
                bounds[i][0],
            )
            for i in range(len(bounds))
        ]
        candidate_value = func(candidate)

        if candidate_value < current_value:
            if abs(current_value - candidate_value) < epsilon:
                break
            current, current_value = candidate, candidate_value

    return current, current_value


def random_local_search(func, bounds, iterations=1000, epsilon=1e-6):
    current = [random.uniform(b[0], b[1]) for b in bounds]
    current_value = func(current)

    for _ in range(iterations):
        candidate = [random.uniform(b[0], b[1]) for b in bounds]
        candidate_value = func(candidate)

        if candidate_value < current_value:
            if abs(current_value - candidate_value) < epsilon:
                break
            current, current_value = candidate, candidate_value

    return current, current_value


def simulated_annealing(
    func, bounds, iterations=1000, temp=1000, cooling_rate=0.95, epsilon=1e-6
):
    current = [random.uniform(b[0], b[1]) for b in bounds]
    current_value = func(current)

    for _ in range(iterations):
        if temp < epsilon:
            break

        candidate = [
            max(min(current[i] + random.uniform(-1, 1), bounds[i][1]), bounds[i][0])
            for i in range(len(bounds))
        ]
        candidate_value = func(candidate)

        delta = candidate_value - current_value
        if delta < 0 or random.random() < math.exp(-delta / temp):
            if abs(current_value - candidate_value) < epsilon:
                break
            current, current_value = candidate, candidate_value

        # Охолодження
        temp *= cooling_rate

    return current, current_value


if __name__ == "__main__":
    bounds = [(-5, 5), (-5, 5)]

    print("Hill Climbing:")
    hc_solution, hc_value = hill_climbing(sphere_function, bounds)
    print("Розв'язок:", hc_solution, "Значення:", hc_value)

    print("\nRandom Local Search:")
    rls_solution, rls_value = random_local_search(sphere_function, bounds)
    print("Розв'язок:", rls_solution, "Значення:", rls_value)

    print("\nSimulated Annealing:")
    sa_solution, sa_value = simulated_annealing(sphere_function, bounds)
    print("Розв'язок:", sa_solution, "Значення:", sa_value)
