import numpy as np


def ponto_inicial(crmp):
    # NUMERO DE POÇOS PRODUTORES
    num_prod = crmp["num_prod"]

    # NUMERO DE POÇOS INJETORES
    num_inj = crmp["num_inj"]

    # NUMERO DE CICLOS DE CONTROLE
    control_steps = crmp["control_steps"]

    # CORRELACAO TEMPORAL
    s = crmp["temporal"]

    # PERTURBACAO DOS CONTROLES
    delta1 = crmp["delta1"]
    delta2 = crmp["delta2"]

    xpp = np.random.rand(num_prod, 1)

    C = np.zeros((control_steps, control_steps))
    for i in range(control_steps):
        for j in range(control_steps):
            condition = np.abs(i - j) <= s
            if condition:
                C[i, j] = (
                    1 - 1.5 * (np.abs(i - j) / s) + 0.5 * ((np.abs(i - j) / s) ** 3)
                )
            else:
                C[i, j] = 0

    L = np.linalg.cholesky(C)
    xwp = np.zeros((control_steps, num_prod))
    for i in range(num_prod):
        xp = np.tile(xpp[i, 0], (control_steps, 1))
        Z = np.random.normal(0.0, 1.0, (control_steps, 1))
        xwp[:, i] = (xp + delta1 * np.dot(L, Z)).squeeze()

    xpi = np.random.rand(num_inj, 1)

    xwi = np.zeros((control_steps, num_inj))
    for i in range(num_inj):
        xi = np.tile(xpi[i, 0], (control_steps, 1))
        Z = np.random.normal(0.0, 1.0, (control_steps, 1))
        xwi[:, i] = (xi + delta2 * np.dot(L, Z)).squeeze()

    for j in range(num_prod):
        for i in range(control_steps):
            if xwp[i, j] < 0:
                xwp[i, j] = 0
            elif xwp[i, j] > 1:
                xwp[i, j] = 1

    for j in range(num_inj):
        for i in range(control_steps):
            if xwi[i, j] < 0:
                xwi[i, j] = 0
            elif xwi[i, j] > 1:
                xwi[i, j] = 1

    XX = np.concatenate((xwp, xwi), axis=1)
    well_control_correlation = XX.reshape((control_steps * (num_inj + num_prod), 1))

    if crmp["Wcontrols"] == 1:
        x0 = well_control_correlation
    elif crmp["Wcontrols"] == 2:
        x0 = np.random.rand((num_prod + num_inj) * crmp["control_steps"], 1)

    return x0
