import numpy as np

def calculate(numbers):
    if len(numbers) < 9:
        raise ValueError("List must contain nine numbers.")
        return
    number_arr = np.array(numbers).reshape(-1)[:9]
    means = [None]*3
    variances = [None]*3
    stds = [None]*3
    mins = [None]*3
    maxs = [None]*3
    sums = [None]*3
    number_arr = number_arr.reshape(3,3)
    
    i=0
    means[i] = number_arr.mean(axis=i).reshape(-1).tolist()
    variances[i] = number_arr.var(axis=i).reshape(-1).tolist()
    stds[i] = number_arr.std(axis=i).reshape(-1).tolist()
    mins[i] = number_arr.min(axis=i).reshape(-1).tolist()
    maxs[i] = number_arr.max(axis=i).reshape(-1).tolist()
    sums[i] = number_arr.sum(axis=i).reshape(-1).tolist()

    i=1
    means[i] = number_arr.mean(axis=i).reshape(-1).tolist()
    variances[i] = number_arr.var(axis=i).reshape(-1).tolist()
    stds[i] = number_arr.std(axis=i).reshape(-1).tolist()
    mins[i] = number_arr.min(axis=i).reshape(-1).tolist()
    maxs[i] = number_arr.max(axis=i).reshape(-1).tolist()
    sums[i] = number_arr.sum(axis=i).reshape(-1).tolist()

    i=2
    means[i] = number_arr.mean(axis=None).reshape(-1).tolist()[0]
    variances[i] = number_arr.var(axis=None).reshape(-1).tolist()[0]
    stds[i] = number_arr.std(axis=None).reshape(-1).tolist()[0]
    mins[i] = number_arr.min(axis=None).reshape(-1).tolist()[0]
    maxs[i] = number_arr.max(axis=None).reshape(-1).tolist()[0]
    sums[i] = number_arr.sum(axis=None).reshape(-1).tolist()[0]

    calculations = {'mean': means, 'variance': variances, 'standard deviation': stds, 'max': maxs, 'min': mins, 'sum': sums}
    return calculations