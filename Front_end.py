import folium
import sqlite3

connection = sqlite3.connect("location.db")
crsr = connection.cursor()
crsr.execute("SELECT * FROM Location_Table") 
ans = crsr.fetchall()
my_mapp = folium.Map(location = [ans[0][1], ans[0][2]],zoom_start = 15)
for i in range (0,len(ans)):
    folium.Marker([ans[i][1], ans[i][2]],popup = ' Human ').add_to(my_mapp)

my_mapp.save("maps\stranded_people6.html ")