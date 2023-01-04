import matplotlib.pyplot as plt

x = []
for year in range(19):
    x.append((2000+int(year)))

a = -0.1518
b = 359.6
y = []
for value in x:
    y.append(a*value + b)

y_obs = [54.8, 56.1, 55.0, 55.7, 56.2, 55.4, 55.3, 57.0, 55.6, 53.2,
         55.5, 54.6, 54.1, 54.0, 54.1, 54.4, 53.6, 52.7, 52.9]

plt.plot(x, y, label = "Forventet")
plt.plot(x, y_obs, label = "Observasjoner")
plt.xlabel('Årstall')
plt.ylabel('Utslipp, 10^6 t CO2 ')
plt.title('CO2 utslipp per år')
plt.legend()
plt.show()
