import csv

from datetime import datetime

import matplotlib.pyplot as plt

# filename = 'data/sitka_weather_07-2018_simple.csv'
filename = 'data/sitka_weather_2018_simple.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Get dates, and high temperatures from this file
    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        high = int(row[5] if row[5] else 0)
        low = int(row[6] if row[6] else 0)
        dates.append(current_date)
        highs.append(high)
        lows.append(low)

# Plot the high temperatures
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red')
ax.plot(dates, lows, c='blue')

# Format plot
# ax.set_title("Daily high temperatures, July 2018", fontsize=24)
ax.set_title("Daily high and low temperatures - 2018", fontsize=24)
ax.set_xlabel('', fontsize=16)
# Creates the date labels diagonally to prevent overlappint
fig.autofmt_xdate()
ax.set_ylabel("Temperature (F)", fontsize=16)
ax.tick_params(axis='both', which='major', labelsize=16)

plt.show()