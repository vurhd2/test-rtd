import pandas as pd

def convert_list_to_series(arr: list):
   """
   Converts the given list to a Pandas Series
   @param arr     the list to be converted
   """
   return pd.Series(arr)

def num_test(s: pd.Series):
   """
   Returns the number of "test" found within the given Series
   @param s       the Pandas Series to count within
   """
   return s[s == "test"].size