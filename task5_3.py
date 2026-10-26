import math

def custom_stats(data):
    n = len(data)
    if n == 0:
        return 0, 0
    mean = sum(data) / n
    variance = sum((x - mean) ** 2 for x in data) / n
    std_dev = math.sqrt(variance)
    return mean, std_dev


def find_anomalies_pure(data, k=2.0):
    mean, std_dev = custom_stats(data)
    if std_dev == 0:
        return []
    return [x for x in data if abs(x - mean) > k * std_dev]


if __name__ == "__main__":
    data_sample = [10, 12, 11, 13, 10, 12, 100, 9, 11, -50]
    print("Аномалии (чистый Python):", find_anomalies_pure(data_sample, k=2.0))

    try:
        import numpy as np

        def find_anomalies_numpy(data, k=2.0):
            arr = np.array(data)
            mean = np.mean(arr)
            std_dev = np.std(arr)
            if std_dev == 0:
                return []
            return arr[np.abs(arr - mean) > k * std_dev].tolist()

        print("Аномалии (numpy):", find_anomalies_numpy(data_sample, k=2.0))
    except ImportError:
        print("Библиотека NumPy не установлена.")
