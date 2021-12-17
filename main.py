import matplotlib.pyplot as plt
import pandas as pd
import csv

df = []

solar_mass = []
solar_radius = []
solar_gravity = []
solar_distance = []
name = []

with open("new_merged.csv", 'r') as f:
    csv_reader = csv.reader(f)
    for i in csv_reader:
        df.append(i)

star_data_rows = df[1:]

for star_data in star_data_rows:
    if len(star_data) < 9:
        star_data_rows.remove(star_data)
    elif len(star_data) == 9:
        solar_mass.append(star_data[6])
        solar_radius.append(star_data[7])
        solar_gravity.append(star_data[8])
        solar_distance.append(star_data[5])
        name.append(star_data[0])

final_star_list = []


for star_data in star_data_rows:
  temp_dict = {
      "name":star_data[0],
      "lightyears_from_earth":star_data[5],
      "star_mass":star_data[6],
      "star_radius":star_data[7],
      "gravity":star_data[8],
  }
  final_star_list.append(temp_dict)

print(final_star_list)



