import json 
import csv

accounts = ['Aki_Hoshide']

for account in accounts:
	FOLLOWERS_FILE = account + "_followers.json"
	f = open(FOLLOWERS_FILE) 
	data = json.load(f) 
	f.close()
	FOLLOWERS_CSV = account + "_followers.csv"
	f = open(FOLLOWERS_CSV) 
	csv_file = csv.writer(f) 
	for item in data: 
	    f.writerow(item) 

	f.close()