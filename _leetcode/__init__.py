import time


def measure_execution_speed(func1, func2, num_iterations=1000, **kwargs):
    total_time_func1 = measure_function_execution_time(func1, num_iterations, **kwargs)
    total_time_func2 = measure_function_execution_time(func2, num_iterations, **kwargs)

    avg_time_func1 = total_time_func1 / num_iterations
    avg_time_func2 = total_time_func2 / num_iterations

    print("\n  Speed comparison:")
    print(f"  - Average execution speed of function 1 ({func1.__name__}):", avg_time_func1)
    print(f"  - Average execution speed of function 2 ({func2.__name__}):", avg_time_func2)

    if avg_time_func1 < avg_time_func2:
        print(f"  - Function 1 (({func1.__name__})) executes faster")
    elif avg_time_func1 > avg_time_func2:
        print(f"  - Function 2 ({func2.__name__}) executes faster")
    else:
        print("  - Both functions execute at the same speed!")


def measure_function_execution_time(func, num_iterations, **kwargs):
    total_time = 0
    for _ in range(num_iterations):
        start_time = time.time()
        func(**kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        total_time += execution_time
    return total_time
