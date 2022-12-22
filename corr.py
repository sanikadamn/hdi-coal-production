#pls go through this tomorrow
import csv


def read_csv(filepath):
    x=[]
    with open(filepath,newline="") as csv_file:
        reader=csv.reader(csv_file)
        for row in reader:
            x.append(row)

    return x
    



def mean(x):
    return sum(x)/len(x)

def mean(y):
    return sum(y)/len(y)    


def calc_corr(x,y):
    x_mean=mean(x)
    y_mean=mean(y)

    
    numerator=0
    denominator=0
    sum_x=0
    sum_y=0
    
    for x_i,y_i in zip(x,y):
        numerator+=(x_i-x_mean)*(y_i-y_mean)

    for x_i in x:
        sum_x+=(x_i-x_mean)**2

    for y_i in y:
        sum_y+=(y_i-y_mean)**2    

    denominator=(sum_x*sum_y)**0.5 

    corr=numerator/denominator
        

    return corr

file_1="fertility-rate.csv"
file_2="literacy-rate.csv"
X=read_csv(file_1)
Y=read_csv(file_2)

compiled_X={}
compiled_Y={}

for x,y in zip(X,Y):
    state_x=x[0]
    state_y=y[0]
    compiled_X[state_x]=x[1]
    compiled_Y[state_y]=y[1]

del compiled_X["States/UTs"]
del compiled_Y["States/UTs"]    

compiled_fertility_rate=[]    
compiled_literacy_rate=[]

states=sorted(list(compiled_X.keys()))
for state in states:
    if state in compiled_Y:
        compiled_fertility_rate.append(float(compiled_X[state]))
        compiled_literacy_rate.append(float(compiled_Y[state]))

print(calc_corr(compiled_fertility_rate,compiled_literacy_rate))        