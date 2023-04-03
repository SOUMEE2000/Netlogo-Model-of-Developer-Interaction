import csv
import matplotlib.pyplot as plt
import numpy as np
import streamlit as st

class Backend_functions:
    def __init__(self):
        self.param_map = {}
        self.param_list = []
        self.run_data = []

    def parse_csv(self, doc, num_params):

        line_count = 1
        key = 0
        for row in doc:
            row = row.replace("\"","").split(",")
            if line_count > 6 and line_count <= 6 + num_params + 1 and len(row) != 0:
                self.param_map[row[0]] = self.param_map.get(row[0], key)
                lst = list(map(float, row[1:]))
                self.param_list.append(lst)
                key += 1
            elif line_count > 6 + num_params + 1 and len(row) != 0 and row[0] == "":
                self.run_data.append(list(map(float, row[1:])))
            line_count += 1
        self.run_data = self.run_data[1:-2]
        return self.param_map

    def Extract(self, lst, i):
        return [item[i] for item in lst]

    def plot_val(self, reqd_params, length):
        Y = [i for i in range(200)]
        time_series = []

        reqd_params, title, legend = self.plot_util(reqd_params, length)
        for j in reqd_params:
            for i in range(len(self.param_list[0])):
                param_set = self.Extract(self.param_list, i)
                #print(j)
                #print(self.run_data)
                if (param_set[1:] == j).all():
                    index = int(param_set[0])
                    time_series.append(np.transpose(self.run_data)[index])
                    break

        for i in time_series:
            plt.plot(Y, i)
        plt.title(title)
        plt.legend(legend)
        #plt.figure(figsize=(8, 8))

        return title, plt

    def plot_util(self, reqd_params, length):
        title = ""
        legend = ""
        for enum, i in enumerate(reqd_params):
            if len(i) == 1:
                name = list(self.param_map.keys())[enum+1]
                title += str(name) + " = " + str(i[0]) + "  "
            else:
                legend = i
            i[:] = [i[0]]*(length-len(i)) + i

        return np.transpose(reqd_params), title, legend
