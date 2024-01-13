import QuantLib as ql
import matplotlib.pyplot as plt
import numpy as np

# Set evaluation date
today = ql.Date.todaysDate()
ql.Settings.instance().evaluationDate = today

# Market data
spot_rates = [0.02, 0.02, 0.02, 0.02, 0.02, 0.02]  # Adding an additional rate
tenors = [ql.Period(6, ql.Months), ql.Period(1, ql.Years),
          ql.Period(2, ql.Years), ql.Period(3, ql.Years),
          ql.Period(5, ql.Years), ql.Period(6, ql.Years)]  # Extending to 6 years
calendar = ql.UnitedStates(ql.UnitedStates.GovernmentBond)
day_count = ql.ActualActual(ql.ActualActual.ISDA)

# Construct yield curve
spot_dates = [calendar.advance(today, tenor) for tenor in tenors]
spot_curve = ql.ZeroCurve(spot_dates, spot_rates, day_count, calendar)
spot_curve_handle = ql.YieldTermStructureHandle(spot_curve)

# Hull-White model parameters
a = 0.1
sigma = 0.01

# Create Hull-White process
hull_white_process = ql.HullWhiteProcess(spot_curve_handle, a, sigma)

# Time setup
length = 5  # in years
timestep = 90
grid = ql.TimeGrid(length, timestep)

# Random sequence generator
sequence_generator = ql.UniformRandomSequenceGenerator(timestep, ql.UniformRandomGenerator())
gaussian_sequence_generator = ql.GaussianRandomSequenceGenerator(sequence_generator)

# Gaussian path generator
path_generator = ql.GaussianPathGenerator(hull_white_process, length, timestep, gaussian_sequence_generator, False)

# Generate multiple paths
num_paths = 100
paths = np.zeros((num_paths, len(grid)))
for i in range(num_paths):
    sample_path = path_generator.next().value()
    for j in range(len(grid)):
        paths[i, j] = sample_path[j]

# Plotting
plt.figure(figsize=(10, 6))
for i in range(num_paths):
    plt.plot(np.linspace(0, length, len(grid)), paths[i, :], lw=0.8, alpha=0.5)
plt.title("Hull-White Short Rate Simulation")
plt.xlabel("Time (Years)")
plt.ylabel("Short Rate")
plt.grid(True)
plt.show()
