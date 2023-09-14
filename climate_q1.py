import matplotlib.pyplot as plt
connection = sqlite3.connect('climate.db')
cursor = connection.cursor()
        
years = []
co2 = []
temp = []

cursor.execute('SELECT years, co2, temp FROM ClimateData')
rows = cursor.fetchall()
for row in rows:
    year, co2, temp = row
    year.append(year)
    co2.append(co2)
    temp.append(temp)

plt.subplot(2, 1, 1)
plt.plot(years, co2, 'b--') 
plt.title("Climate Data") 
plt.ylabel("[CO2]") 
plt.xlabel("Year (decade)") 

plt.subplot(2, 1, 2)
plt.plot(years, temp, 'r*-') 
plt.ylabel("Temp (C)") 
plt.xlabel("Year (decade)") 
plt.show() 
plt.savefig("co2_temp_1.png") 

connection.close()
