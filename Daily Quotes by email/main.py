import getting_emails
import sending_emails
import csv

getting_emails.main()


with open("emails.csv", 'r') as file: 
  data = csv.reader(file)
  for row in data:
    # print(row[0])
    sending_emails.main(row[0])
  
  