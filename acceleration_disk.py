import numpy as np
import matplotlib.pyplot as plt
import os

os.makedirs("results/plots", exist_ok=True)

# -----------------------------
# Physical parameters (toy model)
# -----------------------------

# -----------------------------
# Physical parameters (normalized units)
# -----------------------------

G = 1.0          # Gravitational constant
M = 1.0          # Black hole mass
Mdot = 1.0       # Mass accretion rate
r_in = 3.0       # Inner disk radius (ISCO-like)
r_out = 100.0    # Outer disk radius



# -----------------------------
# Radial grid
# -----------------------------

N_r = 500                     # Number of radial points
r = np.linspace(r_in, r_out, N_r)

# -----------------------------
# Disk surface brightness model
# -----------------------------

def surface_brightness(r):
    """
    Toy model for accretion disk surface brightness.
    
    Parameters
    ----------
    r : numpy array
        Radial distance from the black hole.
    
    Returns
    -------
    F : numpy array
        Radiated flux per unit area at radius r.
    """
    return 1.0 / r**3

# -----------------------------
# Compute radial flux profile
# -----------------------------

F_r = surface_brightness(r)

# -----------------------------
# Differential luminosity
# -----------------------------

dL_dr = 2 * np.pi * r * F_r

# -----------------------------
# Total disk luminosity
# -----------------------------

L_total = np.trapz(dL_dr, r)
print(f"Total disk luminosity (normalized units): {L_total:.4f}")

# -----------------------------
# Plot energy flux profile
# -----------------------------

plt.figure(figsize=(6,4))
plt.plot(r, F_r, color="royalblue")
plt.xlabel("Radius r")
plt.ylabel("Energy flux F(r)")
plt.title("Accretion Disk Energy Flux Profile")
plt.grid(True)
plt.tight_layout()
plt.savefig("results/plots/flux_profile.png", dpi=150)
plt.show()

# -----------------------------
# Plot differential luminosity
# -----------------------------

plt.figure(figsize=(6,4))
plt.plot(r, dL_dr, color="darkorange")
plt.xlabel("Radius r")
plt.ylabel("dL/dr")
plt.title("Differential Disk Luminosity")
plt.grid(True)
plt.tight_layout()
plt.savefig("results/plots/differential_luminosity.png", dpi=150)
plt.show()

# -----------------------------
# Cumulative luminosity
# -----------------------------

L_cumulative = np.cumsum(dL_dr) * (r[1] - r[0])

plt.figure(figsize=(6,4))
plt.plot(r, L_cumulative / L_total, color="seagreen")
plt.xlabel("Radius r")
plt.ylabel("Fraction of Total Luminosity")
plt.title("Cumulative Disk Luminosity")
plt.grid(True)
plt.tight_layout()
plt.savefig("results/plots/cumulative_luminosity.png", dpi=150)
plt.show()

# -------------------------------------------------
# STEP 5B: Parameter study — effect of accretion rate
# -------------------------------------------------

mdot_values = [0.5, 1.0, 2.0]

plt.figure(figsize=(6,4))

for mdot in mdot_values:
    F_r_mdot = (3 * G * M * mdot / (8 * np.pi * r**3)) * (1 - np.sqrt(r_in / r))
    plt.plot(r, F_r_mdot, label=f"Mdot = {mdot}")

plt.xlabel("Radius r")
plt.ylabel("Energy Flux F(r)")
plt.title("Effect of Accretion Rate on Disk Energy Flux")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("results/plots/flux_profile_mdot_study.png", dpi=150)
plt.show()
