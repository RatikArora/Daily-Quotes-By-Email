import gspread
import csv
import os

def main():
    sa = gspread.service_account(filename="dailyquotes-9-19c0583b8150.json")
    sh =sa.open("informations")
    wks = sh.worksheet("res1")
    # print("rows : ",wks.row_count)
    # print("columns : ",wks.col_count)

    # print(wks.get_all_records())
    # print(wks.get_all_values()) 
    f = open("value_of_i.csv",'r')
    file = open('emails.csv','a',newline='')
    row = csv.reader(f)
    for data in row:
        print("Current value of i : ",data[0])
        i = data[0]

    while 1:
        string = 'c'+i
        print("At column : ",string)
        email = wks.acell(string).value
        if email:
            print(email)
            x = csv.writer(file)
            record = [email]
            x.writerow(record)
            i=int(i)
            i+=1
            i=str(i)

        else:
            f.close()
            os.remove("value_of_i.csv")
            f = open("value_of_i.csv",'w')
            f.write(i)
            file.close()
            f.close()
            break
