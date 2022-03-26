# ************************************************************************************************************************************************************************************************** #
# ****************************************************** 8.	To determine the acceleration due to gravity (g) by Kater’s reversible pendulum. ******************************************************* #
# ************************************************************************************************************************************************************************************************** #
# -@ AmiLab


'''
Note-
    - **DATA VALIDATION EXCLUDED FOR BEING CHECKED AT THE TIME OF DATA INPUT**
    - All Testings have been logged into the terminal for future debuggings.
    - The Time taken for each Oscillation observed is assumed to be in the same unit in the case of the readings made from the 2 ends of the Kater's Pendulum.
    - Length of Kater's Pendulum for the readings made from its 2 ends are assumed to be in the same units..
'''


# ********************************************************************** Argument / Variable Declaration (for Testing purposes) ********************************************************************** #


n = 5                                                                                                   # The Total Number of Observations been performed
t = {'t1': [26.56, 35.20, 44.02, 52.83, 61.25], 't2': [26.41, 33.44, 42.02, 49.62, 58.80]}              # The Time taken for each Oscillation observed from the 2 Ends(Top and Bottom, that are A = 1 and B = 2) of the Kater's Pendulum
nox = [15, 20, 25, 30, 35]                                                                              # The Number of Oscillations been made in each observation by the Kater's Pendulum
l1 = 0.54                                                                                               # The length of the Kater's Pendulum measured from the 1st End(A = 1) of it
l2 = 0.32                                                                                               # The length of the Kater's Pendulum measured from the 2nd End(B = 2) of it



# **************************************************************************************** Section ends here **************************************************************************************** #


# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- #



# ******************************************************* Calculations for the acceleration due to gravity (g) by Kater’s reversible pendulum ******************************************************* #


from math import pi
import matplotlib.pyplot as plt
from scipy.constants import g
import numpy as np
from scipy import interpolate


def calTimePeriodsT(t, nox, n):                                             # For Calculating the Time Periods(T) from the Time count for one Oscilaltion(t) measurred for both the Ends(A & B) of the Kater's Pendulum, number of Oscillations(nox) made and the total number of Observations(n)
    global t1, t2
    t1, t2 = list(t.keys())[0], list(t.keys())[1]
    T = {t1.upper(): [], t2.upper(): []}
    for i in range(n):
        T[t1.upper()].append(t[t1][i] / nox[i])
        T[t2.upper()].append(t[t2][i] / nox[i])
    return T

# Testing-
T = calTimePeriodsT(t, nox, n)
print(T)


def calAvgTimePeriods(T, n):                                                # For Calculating the Average of the Time Periods Obtained by the previous function
    global T1, T2
    T1, T2 = str(t1).upper(), str(t2).upper()
    return {T1: sum(T[T1]) / n, T2: sum(T[T2]) / n}

# Testing-
T_avg = calAvgTimePeriods(T, n)
print(T_avg)


def cal_g_Theoretical(T_avg, l1, l2):                                        # For Calulating the Theoretical Value of Accleration Due to Gravity on Earth 'g', thus obtained, g_theoretical
    return (8 * pi ** 2) / (((T_avg[T1] ** 2 + T_avg[T2] ** 2) / (l1 + l2)) + ((T_avg[T1] ** 2 - T_avg[T2] ** 2) / (l1 - l2)))

# Testing-
g_theoretical = cal_g_Theoretical(T_avg, l1, l2)
print("Theoretical value of 'g' obtained:  {} m-sec^(-2)".format(g_theoretical))

print("Actual value of 'g':  {} m-sec^(-2)".format(g))                      # Printing the Actual Value of Accleration due to Gravity on Earth 'g', g_actual


def calSignedError(g_actual, g_theoretical):                                # For Calculating the Signed Error between the Actual and Theoretical Value of Accleration due to Gravity on Earth, Signed Error = g_actual - g_theoretical
    return (g_actual - g_theoretical)

#Testing-
signed_err = calSignedError(g, g_theoretical)
print('Signed Error =', signed_err)


def calAbsError(signed_err):                                                # For Calculating the Absolute Error between the Actual and Theoretical Value of Accleration due to Gravity on Earth
    return abs(signed_err)

# Testing-
abs_err = calAbsError(signed_err)
print('Absolute Error =', abs_err)


def calRelError(g_actual, abs_err):                                         # For Calculating the Relative Error between the Actual and Theoretical Value of Accleration due to Gravity on Earth
    return abs_err / g_actual

# Testing-
rel_err = calRelError(g, abs_err)
print('Relative Error =', rel_err)


def calPercentageError(rel_err):                                            # For Calculating the Percentage Error between the Actual and Theoretical Value of Accleration due to Gravity on Earth
    return rel_err * 100

# Testing-
percentage_err = calPercentageError(rel_err)
print('Percentage Error = {} %'.format(percentage_err))


def graphCurvePlotter(T, l1, l2, n):                                        # For Plotting the Curve of Time Period(T) v/s. the Length of the Kater's Pendulum(LA + LB)
    x = []
    for i in range(n):
        x.append((l1 + l2) * i)
    y = [T[T1][i] + T[T2][i] for i in range(n)]
    # plt.plot(x, y)

    x_new = np.linspace(1, 5, 50)
    bspline = interpolate.make_interp_spline(x, y)
    y_new = bspline(x_new)

    plt.plot(x_new, y_new)
    plt.title(r'($L_{A}$ + $L_{B}$) v/s. T')
    plt.xlabel(r'($L_{A} + L_{B}$)')
    plt.ylabel('T')
    plt.show()

# Testing-
graphCurvePlotter(T, l1, l2, n)



# ********************************************************************************* Section ends here *********************************************************************************************** #


# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- #




