import time
import unittest

def measure_time(func, *args, **kwargs):
    start_time = time.time()
    result = func(*args, **kwargs)
    end_time = time.time()
    execution_time = end_time - start_time
    return result, execution_time

def example_function(n):
    total = 0
    for i in range(n):
        total += i
    return total

result, execution_time = measure_time(example_function, 1000000)
print(f"Result: {result}, Execution time: {execution_time} seconds")

class TestMeasureTime(unittest.TestCase):
    def test_example_function(self):
        result, execution_time = measure_time(example_function, 1000000)
        self.assertEqual(result, 499999500000)
        self.assertTrue(execution_time > 0)

    def test_empty_function(self):
        def empty_function():
            pass
        result, execution_time = measure_time(empty_function)
        self.assertIsNone(result)
        self.assertTrue(execution_time >= 0)

if __name__ == '__main__':
    unittest.main()
