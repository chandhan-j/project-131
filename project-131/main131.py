import csv
import pandas as pd

rows = []

with open('Stars.csv', 'r') as f:
    csv_r = csv.reader(f)
    for row in csv_r:
        rows.append(row)

headers = rows[0]
stars_data = rows[1:]
headers[0] = 'Index'

star_data = []

for star in stars_data:
    if star[3] != '?': 
        star[3] = float(star[3].strip("\'"))*1.989e+30
    
    if star[4] != '?':
        star[4] = float(star[4].strip("\'"))*6.957e+8
    star_data.append(star)

star_data_gravity = []

for star in star_data:
    if star[3] != '?' and star[4] != '?':
        gravity = (6.674e-11 * float(star[3]))/(float(star[4])*float(star[4]))
    star.append(gravity)
    star_data_gravity.append(star)

name = []
distance = []
mass = []
radius = []
gravity = []

for row in star_data_gravity:
    name.append(row[1])
    distance.append(row[2])
    mass.append(row[3])
    radius.append(row[4])
    gravity.append(row[5])

df = pd.DataFrame(
    list(zip(name, distance, mass, radius, gravity)),
    columns=["Star Name", "Distance", "Mass", "Radius", "Gravity"],
)

df.to_csv('final.csv')