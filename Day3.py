import statistics
from scipy.stats import skew
 
# Nominal Data (e.g., categories, no intrinsic order)
nominal_data = {"Red", "Blue", "Green"}
print("Nominal Data:", nominal_data)
 
# Ordinal Data (e.g., categories with order)
ordinal_data = {"Low", "Medium", "High"}
print("Ordinal Data:", ordinal_data)
 
# Discrete Data (e.g., countable, distinct values)
discrete_data = [1, 2, 3, 4, 5]
print("Discrete Data:", discrete_data)
 
# Continuous Data (e.g., real numbers, measurable values)
continuous_data = [1.5, 2.3, 3.8, 4.1, 5.0]
print("Continuous Data:", continuous_data)
 
# Mean
mean_discrete = statistics.mean(discrete_data)
mean_continuous = statistics.mean(continuous_data)
print("Mean (Discrete):", mean_discrete)
print("Mean (Continuous):", mean_continuous)
 
# Mode
mode_discrete = statistics.mode(discrete_data)
print("Mode (Discrete):", mode_discrete)
 
# Median
median_discrete = statistics.median(discrete_data)
median_continuous = statistics.median(continuous_data)
print("Median (Discrete):", median_discrete)
print("Median (Continuous):", median_continuous)
 
# Range
range_discrete = max(discrete_data) - min(discrete_data)
range_continuous = max(continuous_data) - min(continuous_data)
print("Range (Discrete):", range_discrete)
print("Range (Continuous):", range_continuous)
 
# Skewness
skewness_discrete = skew(discrete_data)
skewness_continuous = skew(continuous_data)
print("Skewness (Discrete):", skewness_discrete)
print("Skewness (Continuous):", skewness_continuous)
 
has context menu
