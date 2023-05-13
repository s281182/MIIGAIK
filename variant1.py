import streamlit as st
import csv

def calculate_dataframe_stats(dataframe):
	surv30 = 0
	surv60 = 0
	unsurv30 = 0
	unsurv60 = 0
	count = len(dataframe)
	if count == 0:
		return 0, 0, 0, 0
	for line in dataframe:
		if line[5] != '':
			if line[1] == '1':
				if float(line[5]) < 30:
					surv30 += 1
				if float(line[5]) > 60:
					surv60 += 1
			elif line[1] == '0':
				if float(line[5]) < 30:
					unsurv30 += 1
				if float(line[5]) > 60:
					unsurv60 += 1
	return round(surv30/count*100), round(surv60/count*100), round(unsurv30/count*100), round(unsurv60/count*100)

def variant1():
	st.header("Посчитать долю пассажиров Титаника, указав: вести поиск среди спасенных или погибших, "
			  "искать в возрастных группах до 30 лет или старше 60 лет")
	with open("data.csv") as file:
		file_reader = csv.reader(file, delimiter=",")
		dataframe = []
		for i, line in enumerate(file_reader):
			# skip header
			if i == 0: continue
			dataframe.append(line)
		count = len(dataframe)
		surv30f, surv60f, unsurv30f, unsurv60f = calculate_dataframe_stats(dataframe)
		ch1 = st.radio("Поиск пассажиров среди:", ["спасенных", "погибших"])
		ch2 = st.radio("Поиск в возрастной группе:", ["до 30 лет", "старше 60 лет"])
		if ch1 == 'спасенных':
			if ch2 == 'до 30 лет':
				st.success("Доля спасенных пассажиров до 30 лет: "+str(surv30f)+"%")
			else:
				st.success("Доля спасенных пассажиров старше 60 лет: "+str(surv60f)+"%")
		else:
			if ch2 == 'до 30 лет':
				st.error("Доля погибших до 30 лет: "+str(unsurv30f)+"%")
			else:
				st.error("Доля погибших пассажиров старше 60 лет: "+str(unsurv60f)+"%")
