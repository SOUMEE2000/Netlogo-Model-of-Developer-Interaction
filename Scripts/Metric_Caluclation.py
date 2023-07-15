import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
from sklearn.metrics import mean_absolute_error as mae
from sklearn.metrics import mean_absolute_percentage_error as mape
from sklearn.metrics import max_error, median_absolute_error

class decode_metric(object):

  def __init__(self):

    self.Empirical = ""
    self.metric = ""
    self.scale_factor = 0.001
    self.mae_factor = 0
    self.max_val_ratio = 0
    self.dropped_na_empirical = None
    self.dropped_na_metric = None

  def read_files(self, path, metric, scale_factor, reqd_sheet):

    self.metric = metric
    self.scale_factor = scale_factor
    if self.metric == "Connection":
      self.Empirical = "avg_degree"
    else:
      self.Empirical = "avg_path_length"

    dataset = pd.ExcelFile(path)
    #print("Choose: " + str(dataset.sheet_names))
    #reqd_sheet = input()
    df1 = pd.read_excel(dataset, reqd_sheet)

    avgModel = pd.ExcelFile("/content/Average-Values-Version_3.xlsx")
    df2 = pd.read_excel(avgModel, 'Sheet1')

    self.dropped_na_empirical  = df1[self.Empirical].dropna()
    self.dropped_na_metric = df2[self.metric].dropna()

  def MAE_scaling_factor(self, fig = False) :

    sum = 0
    summation = []
    y = []
    #scale_factor = 0.01

    if len(self.dropped_na_empirical) != len(self.dropped_na_metric):
      raise Exception("Unequal lengths of simulated and empirical metric")


    # print(self.dropped_na_empirical)
    # print(self.dropped_na_metric)

    for j in range(1, 200):
      j = j*self.scale_factor
      y.append(j)
      sum = 0

      for i in abs(self.dropped_na_empirical - self.dropped_na_metric*j):
        sum += i
      summation.append(sum/50)
    #print(y)
    #print(summation)

    if fig:
      plt.plot(y, summation)

    return y[summation.index(min(summation))]

  def Max_value_ratio(self):
    res = max(self.dropped_na_empirical) / max(self.dropped_na_metric)
    return  res

  def get_scaling_factors(self, fig=False):
    print("MAE: " + str(self.MAE_scaling_factor(fig)) + " Max_value_ratio: " + str(self.Max_value_ratio()))

  def get_metrics(self):
    if self.dropped_na_empirical is None or self.dropped_na_metric is None:
      raise Exception("Files need to be read using read_files method")
    mae_factor = self.MAE_scaling_factor()
    max_val_ratio = self.Max_value_ratio()

    print("MaxValue:")
    print(mae(self.dropped_na_empirical,  self.dropped_na_metric*max_val_ratio))
    #print(mape(self.dropped_na_empirical,  self.dropped_na_metric*max_val_ratio))
    print(median_absolute_error(self.dropped_na_empirical,  self.dropped_na_metric*max_val_ratio))
    print(max_error(self.dropped_na_empirical,  self.dropped_na_metric*max_val_ratio))
    print(stats.pearsonr(self.dropped_na_empirical,  self.dropped_na_metric*max_val_ratio)[0])
    print(stats.spearmanr(self.dropped_na_empirical,  self.dropped_na_metric*max_val_ratio)[0])
    print("")
    print("MAE:")
    print(mae(self.dropped_na_empirical,  self.dropped_na_metric*mae_factor))
    #print(mape(self.dropped_na_empirical,  self.dropped_na_metric*mae_factor))
    print(median_absolute_error(self.dropped_na_empirical,  self.dropped_na_metric*mae_factor))
    print(max_error(self.dropped_na_empirical,  self.dropped_na_metric*mae_factor))
    print(stats.pearsonr(self.dropped_na_empirical,  self.dropped_na_metric*mae_factor)[0])
    print(stats.spearmanr(self.dropped_na_empirical,  self.dropped_na_metric*mae_factor)[0])
    print("")


#Usage
for i in [ "Separation","Connection"]:
  print(i + " :")
  obj1 = decode_metric()
  obj1.read_files("/content/openstack-2.xlsx", i, 0.01, "co-changes")
  obj1.get_scaling_factors(True)
  obj1.get_metrics()
