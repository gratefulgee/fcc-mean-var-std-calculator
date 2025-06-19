import numpy as np

def calculate(input_list):
    if len(input_list) != 9:
        raise ValueError("List must contain nine numbers.")

    matrix = np.array(input_list).reshape(3,3)

    calculations = {
        'mean' : [list(np.mean(matrix, axis=0)), list(np.mean(matrix, axis=1)), np.mean(matrix)],
        'variance': [list(np.var(matrix, axis=0)), list(np.var(matrix, axis=1)), np.var(matrix)],
        'standard deviation': [list(np.std(matrix, axis=0)), list(np.std(matrix, axis=1)), np.std(matrix)],
        'max': [list(np.max(matrix, axis=0)), list(np.max(matrix, axis=1)), np.max(matrix)],
        'min': [list(np.min(matrix, axis=0)), list(np.min(matrix, axis=1)), np.min(matrix)],
        'sum': [list(np.sum(matrix, axis=0)), list(np.sum(matrix, axis=1)), np.sum(matrix)]
    }

    return calculationsgit remote remove origin
git remote add origin https://github.com/gratefulgee/fcc-mean-var-std-calculator.git
git push -u origin main