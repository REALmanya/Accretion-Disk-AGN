# Accretion-Disk-AGN

Computational study of a **geometrically thin accretion disk** around a compact central
object using a **Newtonian analytical thin-disk model**.  
The project investigates **radial energy dissipation, disk luminosity, and scaling with
mass accretion rate**, with results visualized through reproducible numerical plots.

---

## 🌌 Project Motivation

Accretion disks play a central role in the physics of **Active Galactic Nuclei (AGN)**,
where gravitational potential energy is converted into radiation as matter spirals inward
toward a supermassive black hole.

This project focuses on understanding **where** and **how** energy is dissipated within
a thin disk using a simplified but physically meaningful analytical model.  
The goal is **not relativistic or GRMHD realism**, but clarity: connecting **analytical
thin-disk theory** with numerical implementation and visualization.

---

## 🧠 Physical Model

The disk is modeled as a **geometrically thin, optically thick accretion disk** using
normalized units (\( G = M = 1 \)) and a Newtonian gravitational potential.

### Radial Energy Flux

The local energy flux is given by the standard thin-disk expression:

$$
F(r) = \frac{3GM\dot{M}}{8\pi r^3}
\left(1 - \sqrt{\frac{r_{\mathrm{in}}}{r}}\right)
$$

where:
- \( \dot{M} \) is the mass accretion rate  
- \( r_{\mathrm{in}} \) is the inner disk radius (used here as an ISCO-like proxy)

This formulation captures the **qualitative radial structure** of energy dissipation in
classical thin-disk models.

---

## 💻 Numerical Implementation

The disk is discretized radially between prescribed inner and outer radii.
From the energy flux profile, the following quantities are computed:

- **Differential luminosity**
$$
\frac{dL}{dr} = 2\pi r F(r)
$$

- **Total disk luminosity** via numerical integration  
- **Cumulative luminosity** to determine where most energy is released  

A parameter study is performed by varying the mass accretion rate \( \dot{M} \).

---

## 📊 Results and Validation

### Radial Energy Flux
Energy dissipation is strongly concentrated toward the inner disk radii, consistent with
thin-disk analytical expectations.

### Differential Disk Luminosity
The majority of the emitted luminosity originates close to the central object.

### Cumulative Luminosity
A significant fraction of the total luminosity is produced within a relatively small
inner region of the disk.

### Accretion Rate Scaling
Varying \( \dot{M} \) scales the energy flux and luminosity **linearly**, while preserving
the radial profile shape, providing a key **consistency check** of the implementation.

All plots are automatically saved in the `results/plots/` directory.

---

## 🔬 Scientific Interpretation

- Radial energy dissipation follows the expected \( r^{-3} \)–dominated behavior of
  classical thin-disk models.
- Total disk luminosity scales linearly with mass accretion rate, as predicted analytically.
- Cumulative luminosity profiles demonstrate that inner disk regions dominate energy output.
- The numerical results are **qualitatively consistent with canonical thin-disk theory**,
  validating the implementation at an exploratory level.

---

## 📂 Project Structure
Accretion-Disk-AGN/
│
├── accretion_disk.py # Main simulation and analysis script
├── README.md # Project documentation
└── results/
└── plots/
├── flux_profile.png
├── differential_luminosity.png
├── cumulative_luminosity.png
└── flux_profile_mdot_study.png


---

## 🎯 Purpose and Scope

This project serves as a **conceptual and computational exploration** of thin-disk
accretion physics, forming a foundation for more advanced studies involving:

- Relativistic correction factors  
- Spin-dependent inner disk radii  
- Radiative efficiency estimates  
- Connections to observed AGN spectral energy distributions  

The emphasis is on **physical interpretation and numerical consistency**, rather than
high-fidelity astrophysical realism.

---

## 👤 Author

**Manya Johari**  
Undergraduate – Aerospace Engineering  
Interests: Computational astrophysics and numerical modeling




