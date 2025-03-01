import pandas as pd
import matplotlib.pyplot as plt
from astroquery.gaia import Gaia

# Enable async TAP queries for large data retrieval
Gaia.ROW_LIMIT = 50000  # Adjust for larger/smaller datasets

# ADQL Query to retrieve Gaia DR3 data
query = """
SELECT 
    source_id,
    bp_rp AS color_index,
    phot_g_mean_mag - 5 * LOG10(1000 / parallax) + 5 AS abs_mag_g,
    teff_gspphot
FROM gaiadr3.gaia_source
WHERE 
    parallax > 1  -- Ensures stars within ~1 kpc
    AND parallax_over_error > 10  -- High-quality parallax
    AND bp_rp IS NOT NULL  -- Ensures BP-RP color exists
    AND phot_g_mean_mag IS NOT NULL  -- Ensures G-band magnitude exists
    AND teff_gspphot IS NOT NULL  -- Ensures temperature exists
LIMIT 50000
"""

print("Querying Gaia DR3 archive... This may take some time.")
job = Gaia.launch_job_async(query)
results = job.get_results()
print("Data retrieval complete.")

# Convert the results to a Pandas DataFrame
df = results.to_pandas()

# Save to CSV (optional)
df.to_csv("gaia_hr_diagram.csv", index=False)

# Plot H-R Diagram (Color-Magnitude)
plt.figure(figsize=(8, 10))
scatter = plt.scatter(df['color_index'], df['abs_mag_g'], c=df['teff_gspphot'], cmap='plasma', s=1, alpha=0.5)

plt.colorbar(label="Effective Temperature (K)")
plt.gca().invert_yaxis()  # Brighter stars on top
plt.xlabel("BP-RP (Color Index)")
plt.ylabel("Absolute Magnitude (M_G)")
plt.title("Hertzsprung-Russell Diagram from Gaia DR3")

plt.show()