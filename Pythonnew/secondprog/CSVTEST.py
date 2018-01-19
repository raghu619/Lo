
import csv
from datetime import *
path="/home/raghvendra/Desktop/Google Stock Market Data - google_stock_data.csv.csv"
file=open(path,'r')
reader=csv.reader(file)
print(next(reader),"\n\n")
header=next(reader) # First line is the header
dataset=[]
for row in reader:
   date=datetime.strptime(row[0],'%m/%d/%Y')
   print(row)
   open_price=float(row[1]) #'open ' is a builtin function
   high=float(row[2])
   low=float(row[3])
   close=float(row[4])
   volume=int(row[5])
   adj_close=float(row[6])
   dataset.append([date,open_price,high,low,close,volume,adj_close])
#print(header)
#print(dataset[0])

#Compute the daily stock returns
return_path="/home/raghvendra/Desktop/google_returns.csv"
file=open(return_path,'w')
writer=csv.writer(file)
writer.writerow(["DATE","RETURN"])

for i in range(len(dataset)-1):
    today_row=dataset[i]
    today_date=today_row[0]
    today_price=today_row[-1]
    yesterday_row=dataset[i+1]
    yesterday_price=yesterday_row[-1]

    daily_return=(today_price-yesterday_price)/yesterday_price
    formatted_date=today_date.strftime('%m/%d/%y')
    writer.writerow([formatted_date,daily_return])