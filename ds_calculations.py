"""An excel is attached where Column B is data input and column C to I have calculations,final required output is Column I [14-day DS].

1) Write a python script using core python(Without using any 3rd party library/package)  where column B is input and after doing all calculations print column I.

2) Write a python script using Numpy & Pandas  where column B is input and after doing all calculations write output to a CSV file."""

import os
import numpy as np
import pandas as pd


def read_input_from_file(file_name):
    cwd = os.getcwd()
    file = cwd + '/{}'.format(file_name)

    df = pd.read_excel(file)
    df.drop(df.index[:1], inplace=True)
    dff = df[df.columns[1]]
    return dff


def get_difference(dff):
    difference_ = np.diff(dff)
    difference_1 = np.around(list(difference_), decimals=2)
    return difference_1


def get_pov_nev_list(difference_1):
    pov_list = []
    nev_list = []

    for i in difference_1:
        if i > 0:
            pov_list.append(i)
            nev_list.append(0)
        else:
            pov_list.append(0)
            nev_list.append(abs(i))
    return pov_list, nev_list


def get_pov_nev_average(pov_list, nev_list, divider=14):
    pov_average_list = []
    nev_average_list = []
    ds = []
    final_ds = []

    pov_avg_val = sum(pov_list[0:13])/divider
    nev_avg_val = sum(nev_list[0:13])/divider
    for i in range(14, len(pov_list)):
        pov_average_list.append(round(pov_avg_val, 2))
        nev_average_list.append(round(nev_avg_val, 2))
        ds_val = round(pov_avg_val/nev_avg_val, 2)
        ds.append(ds_val)
        if ds_val > 0 and ds_val < 100:
            final_ds.append(round(100-(100/(1+ds_val)), 2))
        pov_avg_val = round(((pov_avg_val*13) + pov_list[i])/14, 2)
        nev_avg_val = round(((nev_avg_val*13) + nev_list[i])/14, 2)
    return pov_average_list, nev_average_list, ds, final_ds


def write_result_in_csv(input, output):
    data = {"Output": output}
    cwd = os.getcwd()
    dff = pd.DataFrame.from_dict(data)
    dff.to_csv(cwd + '/my_output.csv')


if __name__ == "__main__":
    input_diff = read_input_from_file('../../practice/ds.xls')
    difference = get_difference(input_diff)
    pov_l, nev_l = get_pov_nev_list(difference)
    pov_avg_l, nev_avg_l, ds, final_ds = get_pov_nev_average(pov_l, nev_l)
    write_result_in_csv(input_diff, final_ds)

