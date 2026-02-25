

#Plot indoor tables

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

indoor = pd.read_csv('lab5_trial5.csv')
indoor = indoor.iloc[15:].reset_index(drop=True) #drop first 15 rows because the trials are 2 seconds apart -- we cut the first 30 seconds we were not yet outside

# Convert time to seconds since start
indoor["time_seconds"] = indoor["time"] - indoor["time"].iloc[0]

# Plot every variable vs time
variables = [c for c in indoor.columns if c not in ["time", "time_seconds"]]

for var in variables:
    plt.figure()
    plt.plot(indoor["time_seconds"], indoor[var])
    plt.xlabel("Time (seconds)")
    plt.ylabel(var)
    plt.title(f"{var} vs Time")
    plt.show()

#Plot outdoor variables
outdoor = pd.read_csv('lab5_trial6.csv')
outdoor = outdoor.iloc[15:].reset_index(drop=True) #cut first 30 seconds
# Convert time to seconds since start
outdoor["time_seconds"] = outdoor["time"] - outdoor["time"].iloc[0]

# Plot every variable vs time
variables = [c for c in outdoor.columns if c not in ["time", "time_seconds"]]

for var in variables:
    plt.figure()
    plt.plot(outdoor["time_seconds"], outdoor[var])
    plt.xlabel("Time (seconds)")
    plt.ylabel(var)
    plt.title(f"{var} vs Time")
    plt.show()

# Plot each variable with indoor and outdoor on same graph
for var in variables:
    plt.figure()
    plt.plot(indoor["time_seconds"], indoor[var], label="Indoor")
    plt.plot(outdoor["time_seconds"], outdoor[var], label="Outdoor")
    plt.xlabel("Time (seconds)")
    plt.ylabel(var)
    plt.title(f"{var}: Indoor vs Outdoor")
    plt.legend()
    plt.show()

# Create histogram for each variable
for var in variables:
    plt.figure()

    plt.hist(indoor[var], bins=30, alpha=0.5, label="Indoor")
    plt.hist(outdoor[var], bins=30, alpha=0.5, label="Outdoor")

    plt.xlabel(var)
    plt.ylabel("Frequency")
    plt.title(f"{var}: Indoor vs Outdoor Distribution")
    plt.legend()
    plt.show()

#The weather data seems to be a lot more meaningful given that the particulate matter is more random and susceptible to small changes. The temperature data covered a lot larger of a spread for the Outdoor measurements, which if you look at the time series makes sense because as the sensor calibrated to outdoor temperature it steadily decreased. The Gas distribution follows a similar pattern, but the outdoor measurements were increimentally higher than the indoor measurements. Humidity was a lot higher outside which also makes sense given it rained earlier today. Air pressure corresponded to this higher humidity by being lower outside, also most likely attributed to the inclement weather. Finally, the altitude increased for the 'outdoor' measurements because a flight of stairs was taken to bring the sensor outdoors.

import pandas as pd

trial5 = pd.read_csv('lab5_trial5.csv')
trial6 = pd.read_csv('lab5_trial6.csv')


t5_mean_temp = trial5['temp'].mean()
t5_std_temp = trial5['temp'].std()
t6_mean_temp = trial6['temp'].mean()
t6_std_temp = trial6['temp'].std()


t5_mean_pressure = trial5['pressure'].mean()
t5_std_pressure = trial5['pressure'].std()
t6_mean_pressure = trial6['pressure'].mean()
t6_std_pressure = trial6['pressure'].std()


t5_mean_humidity = trial5['humidity'].mean()
t5_std_humidity = trial5['humidity'].std()
t6_mean_humidity = trial6['humidity'].mean()
t6_std_humidity = trial6['humidity'].std()


t5_mean_altitude = trial5['altitude'].mean()
t5_std_altitude = trial5['altitude'].std()
t6_mean_altitude = trial6['altitude'].mean()
t6_std_altitude = trial6['altitude'].std()


t5_mean_gas = trial5['gas'].mean()
t5_std_gas = trial5['gas'].std()
t6_mean_gas = trial6['gas'].mean()
t6_std_gas = trial6['gas'].std()


t5_mean_pm10_std = trial5['pm10 standard'].mean()
t5_std_pm10_std = trial5['pm10 standard'].std()
t6_mean_pm10_std = trial6['pm10 standard'].mean()
t6_std_pm10_std = trial6['pm10 standard'].std()

t5_mean_pm25_std = trial5['pm25 standard'].mean()
t5_std_pm25_std = trial5['pm25 standard'].std()
t6_mean_pm25_std = trial6['pm25 standard'].mean()
t6_std_pm25_std = trial6['pm25 standard'].std()

t5_mean_pm100_std = trial5['pm100 standard'].mean()
t5_std_pm100_std = trial5['pm100 standard'].std()
t6_mean_pm100_std = trial6['pm100 standard'].mean()
t6_std_pm100_std = trial6['pm100 standard'].std()


t5_mean_pm10_env = trial5['pm10 env'].mean()
t5_std_pm10_env = trial5['pm10 env'].std()
t6_mean_pm10_env = trial6['pm10 env'].mean()
t6_std_pm10_env = trial6['pm10 env'].std()

t5_mean_pm25_env = trial5['pm25 env'].mean()
t5_std_pm25_env = trial5['pm25 env'].std()
t6_mean_pm25_env = trial6['pm25 env'].mean()
t6_std_pm25_env = trial6['pm25 env'].std()

t5_mean_pm100_env = trial5['pm100 env'].mean()
t5_std_pm100_env = trial5['pm100 env'].std()
t6_mean_pm100_env = trial6['pm100 env'].mean()
t6_std_pm100_env = trial6['pm100 env'].std()


t5_mean_03um = trial5['03um'].mean()
t5_std_03um = trial5['03um'].std()
t6_mean_03um = trial6['03um'].mean()
t6_std_03um = trial6['03um'].std()

t5_mean_05um = trial5['05um'].mean()
t5_std_05um = trial5['05um'].std()
t6_mean_05um = trial6['05um'].mean()
t6_std_05um = trial6['05um'].std()

t5_mean_10um = trial5['10um'].mean()
t5_std_10um = trial5['10um'].std()
t6_mean_10um = trial6['10um'].mean()
t6_std_10um = trial6['10um'].std()

t5_mean_25um = trial5['25um'].mean()
t5_std_25um = trial5['25um'].std()
t6_mean_25um = trial6['25um'].mean()
t6_std_25um = trial6['25um'].std()

t5_mean_50um = trial5['50um'].mean()
t5_std_50um = trial5['50um'].std()
t6_mean_50um = trial6['50um'].mean()
t6_std_50um = trial6['50um'].std()

t5_mean_100um = trial5['100um'].mean()
t5_std_100um = trial5['100um'].std()
t6_mean_100um = trial6['100um'].mean()
t6_std_100um = trial6['100um'].std()


#significance


cols = [
    'temp', 'pressure', 'humidity', 'altitude', 'gas',
    'pm10 standard', 'pm25 standard', 'pm100 standard',
    'pm10 env', 'pm25 env', 'pm100 env',
    '03um', '05um', '10um', '25um', '50um', '100um'
]

print("STATISTICAL SIGNIFICANCE CHECK ")

for col in cols:

    m5 = trial5[col].mean()
    sd5 = trial5[col].std()


    m6 = trial6[col].mean()


    diff = abs(m6 - m5)
    threshold = 3 * sd5

    print(f"Variable: {col.upper()}")
    print(f"Trial 5 Mean: {m5:.4f}, Std Dev: {sd5:.4f}")
    print(f"Trial 6 Mean: {m6:.4f}")


    if diff > threshold:
        print("RESULT: They are statistically different")
    else:
        print("RESULT: They are NOT statistically different")
    print("-" * 30)

