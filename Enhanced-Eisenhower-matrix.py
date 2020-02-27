import argparse
from pandas import read_csv, DataFrame
import pandas as pd
from datetime import datetime

parser = argparse.ArgumentParser()

parser.add_argument("--tasks", type= str, required= True, help= "Please provide path of tasks csv file")
"""
parser.add_argument("--task", type= str, reuqired= True, help= "Please provide the task name")
parser.add_argument("--est_hours", type= float, required= Tue, help= "Estimated hours that you can complete the task")
parser.add_argument("--complete_before", type= str, required= True, help= "Date when this task has to be completed. Format: dd-mm-yy")
parser.add_argument("--effort", type= int, required= True, help= "Amount of effort this will take [1 -> less effort, 1- -> max effort]")
"""
args = parser.parse_args()

uncertian_mins = 100
efort_max = 10
effective_working_hours = 15

csv_file = args.tasks
task_df = pd.read_csv(csv_file)
print(task_df)
print()

task_df['est_mins'] = task_df['est_mins'] + uncertian_mins
print(task_df)
print()

#task_df = task_df[['task_name', 'est_hours', 'actual_est_hours', 'comp_before', 'effort']]
#print(task_df)
#print()

task_df['effort'] = task_df['effort']/efort_max
print(task_df)
print()

task_df['datetime'] = task_df['comp_before'] + " " + task_df['comp_before_time']
print(task_df)
print()

now = datetime.now()
# dd/mm/YY H:M:S
dt_string = now.strftime("%Y/%m/%d %H:%M:%S")
print("date and time =", dt_string)

task_df['now'] = dt_string
print(task_df)
print()

task_df['datetime']= pd.to_datetime(task_df['datetime'])
task_df['now']= pd.to_datetime(task_df['now'])
print(task_df)
print()

#task_df['datetime'].astype('datetime64[ns]')
#task_df['now'].astype('datetime64[ns]')

task_df['mins_remain'] = (task_df['datetime'] - task_df['now']).astype('timedelta64[m]')
print(task_df)
print()

# Priority matrix
task_df['pirority'] = task_df['effort'] * task_df['mins_remain']
print(task_df)
print()

task_df = task_df.sort_values('pirority')
print(task_df)
print()