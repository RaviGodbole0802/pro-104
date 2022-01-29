import csv

with open("SOCR-HeightWeight.csv",newline='')as f:
    reader=csv.reader(f)
    file_data=list(reader)
    file_data.pop(0)
  # print(file_data[1][1])
    #print(file_data[2][1])
    print(len(file_data))
    new_Data=[]
    for i in range(len(file_data)):
        number=file_data[i][1]
        new_Data.append(float(number))
    #print(new_Data)
    numberofelements=len(new_Data)
    print("numberofelements "+str(numberofelements))
    total=0
    for x in range(len(new_Data)):
        total=total+x