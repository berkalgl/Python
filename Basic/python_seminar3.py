# python II

# List Comprehension

salaries = [1000,2000,3000,4000]

def NewSalary(x):
    return x*20/100+x

for salary in salaries:
    print(NewSalary(salary))

emptyList = []

for salary in salaries:
    if salary > 3000:
        emptyList.append(NewSalary(salary))
    else:
        emptyList.append(NewSalary(salary * 2))

####
a = [NewSalary(salary * 2) if salary < 3000 else NewSalary(salary) for salary in salaries]
print(a)

b = [salary * 2 for salary in salaries]
print(b)

c = [salary *2 for salary in salaries if salary < 3000]
print(c)

d = [salary * 2 if salary < 3000 else salary * 0 for salary in salaries]
print(d)

e = [NewSalary(salary) if salary < 3000 else NewSalary(salary) for salary in salaries]
####
## returns an array

students = ["John", "Mark", "Venessa", "Mariam"]
unwantedStudents = ["John", "Venessa"]

f = [student.lower() if student in unwantedStudents else student.upper() for student in students]
print(f)

####
# Dictionary Comprehension
####

dictionary = {'a':1,'b':2,'c':3,'d':4}
dictionary["a"]
dictionary.keys()
dictionary.values()
dictionary.items()

d1 = {k: v **2 for (k,v) in dictionary.items()}
print(d1)
d2 = {k * 2 : v for (k,v) in dictionary.items()}

####
# Add element to dictionary while using iteration
####

# Purpose: add even numbers by its square to the dictionary

numbers = range(10)
newDict = {}

for n in numbers:
    if n % 2 == 0:
        newDict[n] = n**2

d3 = {n : n**2 for n in numbers if n % 2 == 0}
print(d3)

####
# List & Dict Comprehension Apps
####

####
# Change variables' names in any datasets
####

# before:
# ['total' , 'speeding', 'alcohol', 'not_distracted', 'no_previous', 'ins_premium', 'ins_losses', 'abbrev']
# after:
# ['TOTAL' , 'SPEEDING', 'ALCOHOL', 'NOT_DISTRACTED', 'NO_PREVIOUS', 'INS_PREMIUM', 'INS_LOSSES', 'ABBREV']

##pandas framework:
import seaborn as sns

df = sns.load_dataset("car_crashes")
type(df)
df.columns

#bad approach
A=[]

for col in df.columns:
    A.append(col.upper)

df.columns = A

#Comprehension approach
df = sns.load_dataset("car_crashes")
df.columns = [col.upper() for col in df.columns]

###
# If name includes 'INS' make it start with FLAG_ otherwise NO_FLAG_
###

["FLAG_" + col for col in df.columns if "INS" in col]

df.columns = ["FLAG_" + col if "INS" in col else "NO_FLAG_" + col for col in df.columns]

###
# add cat at the start if it is Categotrical 
###
# before:
# ['total' , 'speeding', 'alcohol', 'not_distracted', 'no_previous', 'ins_premium', 'ins_losses', 'abbrev']
# after:
# ['TOTAL' , 'SPEEDING', 'ALCOHOL', 'NOT_DISTRACTED', 'NO_PREVIOUS', 'INS_PREMIUM', 'INS_LOSSES', 'CAT_ABBREV']

df = sns.load_dataset("car_crashes")
["CAT_" + col.upper() if df[col].dtype == "O" else col.upper() for col in df.columns]
# df.columns = ["CAT_" + col.upper() if df[col].dtype == "O" else col.upper() for col in df.columns]
# O stands for Object
# Abbrev column is an object you can check below
# get the information about the dataset
df.head()
df.info()

####
# the purpose is to create a list with string key and value is like below
# all key variables has to be integer
####
# Output:
# {
#   'total': ['mean', 'min', 'max', 'var'],
#   'speeding': ['mean', 'min', 'max', 'var'],
#   'alcohol': ['mean', 'min', 'max', 'var'],
#   'not_distracted': ['mean', 'min', 'max', 'var'],
#   'no_previous': ['mean', 'min', 'max', 'var'],
#   'ins_premium': ['mean', 'min', 'max', 'var'],
#   'ins_losses': ['mean', 'min', 'max', 'var']
# }

df = sns.load_dataset("car_crashes")
num_cols = [col for col in df.columns if df[col].dtype != "O"]
dict1 = {}
agg_list = ['mean', 'min', 'max', 'var']

for col in num_cols:
    dict1[col] = agg_list

{col: agg_list for col in num_cols}

new_dict = {col: agg_list for col in num_cols}
df.groupby("abbrev").agg(new_dict)
df.groupby("abbrev").agg(['mean', 'min', 'max', 'var'])
#################
df = sns.load_dataset("tips")
num_cols = [col for col in df.columns if df[col].dtype in [int,float]]

new_dict = {col: agg_list for col in num_cols}

df.groupby("time").agg(new_dict)

#before: 
#   {'total': ['mean', 'min', 'max', 'var'],
#   'speeding': ['mean', 'min', 'max', 'var'],
#   'alcohol': ['mean', 'min', 'max', 'var']}
#after:
#   {'total': ['total_mean', 'total_min', 'total_max', 'total_var'],
#   'speeding': ['total_mean', 'total_min', 'total_max', 'total_var'],
#   'alcohol': [total_'mean', 'total_min', 'total_max', 'total_var']}

df = sns.load_dataset("car_crashes")
num_cols = [col for col in df.columns if df[col].dtype != "O"]
agg_list = ['mean', 'min', 'max', 'var']

{col: [str(col) + "_" + c for c in agg_list] for col in num_cols}

####
# purpose: make the first column key and array of rest of the row.
####


df = sns.load_dataset("car_crashes")
num_cols = [col for col in df.columns if df[col].dtype in [int,float]]
df[num_cols].head()

{row[0]: [int(s) for s in row[1:]] for row in df[num_cols].values}
