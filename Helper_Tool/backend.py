import csv
import matplotlib.pyplot as plt
import numpy as np
import streamlit as st

class Backend_functions:
    def __init__(self):
        # self.param_map[parameter_name] = self.param_map.get(parameter_name, [maximum, minimum, step])
        self.param_map = {}
        # self.param_list = values of parameters, one row having all combinations of that parameter
        self.param_list = []
        # run_data
        self.run_data = []
        # Number of epochs for which it was run
        self.steps = 0
        # Number of Reporters
        self.reporter = []

    def parse_csv(self, doc, num_params, num_reporters):

        line_count = 1
        key = 0
        for row in doc:
            row = row.replace("\"","").split(",")
            if line_count > 6 and line_count <= 6 + num_params + 1 and len(row) != 0:
                step = 0
                maximum = -10000000
                minimum = 10000000
                flag = 1
                for i in range(1,len(row)):
                    if row[i] == "":
                        row[i] = row[i-1]
                    if float(row[i]) - float(row[1]) > 0 and flag:
                        step = float(row[i]) - float(row[1])
                        flag = 0
                    maximum = max(float(row[i]), maximum)
                    minimum = min(float(row[i]), minimum)

                self.param_map[row[0]] = self.param_map.get(row[0], [maximum, minimum, step])
                #print(maximum, minimum, step)
                #print(len(row))
                lst = list(map(float, row[1:]))
                self.param_list.append(lst)
                key += 1
            elif row[0] == "[steps]":
                self.steps = int(row[1])
            elif row[0] == "[reporter]":
                self.reporter = row[1:num_reporters + 1]
            elif line_count > 6 + num_params + 1 and len(row) != 0 and row[0] == "":
                row = row[1:]
                # for i range(len(row)):
                #     self.run_data[self.reporter[ i % (num_reporters-1)]].append([map(float, row[i])])
                self.run_data.append(list(map(float, row[1:])))
            line_count += 1
        self.run_data = self.run_data[1:-2]
        return self.param_map, self.reporter

    def Extract(self, lst, i):
        return [item[i] for item in lst]

    def plot_val(self, reqd_params, length, reporter_no):
        Y = [i for i in range(self.steps)]
        time_series = []

        reqd_params, title, legend = self.plot_util(reqd_params, length)
        for j in reqd_params:
            for i in range(reporter_no, len(self.param_list[0]) - reporter_no, len(self.reporter)):
                param_set = self.Extract(self.param_list, i + reporter_no)
                #print(j)
                #print(self.run_data)
                if (param_set[1:] == j).all():
                    index = int(param_set[0])
                    time_series.append(np.transpose(self.run_data)[index])
                    break

        for i in time_series:
            plt.plot(Y, i)
        plt.title(title)
        plt.ylabel(self.reporter[reporter_no])
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
