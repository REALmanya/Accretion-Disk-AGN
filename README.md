# Accretion-Disk-AGN

A computational study of a thin accretion disk around a black hole, implemented using
Newtonian gravity. This project models radial energy dissipation, disk luminosity, and
the effect of mass accretion rate on disk structure, with all results saved as reproducible plots.

---

## Project Motivation

Accretion disks are central to the physics of Active Galactic Nuclei (AGN), where matter
spiraling into a supermassive black hole releases vast amounts of energy.
This project focuses on understanding **where** and **how** that energy is dissipated
within a thin disk, using a simplified but physically meaningful analytical model.

The goal is not realism at the GRMHD level, but clarity:
to connect analytical disk theory with numerical implementation and visualization.

---

## Physical Model

We model a **geometrically thin, optically thick accretion disk** using normalized units
(\( G = M = 1 \)).

### Energy Flux Profile

The radial energy flux is given by the standard thin-disk expression:

$$
F(r) = \frac{3GM\dot{M}}{8\pi r^3}
\left(1 - \sqrt{\frac{r_{\mathrm{in}}}{r}}\right)
$$

where:
- $\dot{M}$ is the mass accretion rate  
- $r_{\mathrm{in}}$ is the inner disk radius (ISCO-like proxy)


---
## Numerical Implementation

The disk is discretized radially between an inner and outer radius.
From the energy flux, we compute:

**Differential luminosity**

dL/dr = 2 π r F(r)

**Total disk luminosity** via numerical integration

**Cumulative luminosity** to determine where most energy is released

A parameter study is performed by varying the accretion rate (Ṁ).


## Results

### Energy Flux Profile
Energy dissipation is strongly concentrated toward the inner disk radii.

### Differential Disk Luminosity
Most of the luminosity originates close to the black hole.

### Cumulative Luminosity
A large fraction of the total luminosity is emitted within a small inner region of the disk.

### Accretion Rate Study
Increasing \( \dot{M} \) scales the energy flux uniformly, preserving the radial profile shape.

All plots are automatically saved in the `results/plots/` directory.

---

## Scientific Insights

- Energy dissipation in accretion disks is strongly concentrated toward the inner radii.
- The total luminosity scales linearly with mass accretion rate.
- Log–log flux profiles reveal power-law behavior expected from analytical disk theory.
- This model captures the qualitative physics of thin-disk accretion relevant to AGN environments.

---

## Project Structure

Accretion-Disk-AGN/
│
├── acceleration_disk.py # Main simulation and analysis script
├── README.md # Project documentation
└── results/
└── plots/
├── flux_profile.png
├── differential_luminosity.png
├── cumulative_luminosity.png
└── flux_profile_mdot_study.png


---

## Future Extensions

- Inner radius variation as a proxy for black hole spin
- Radiative efficiency calculation
- Connection to observed AGN spectral energy distributions
- Inclusion of relativistic correction factors

---

## Author

**Manya Johari**  
Aerospace Engineering (B.Tech)  
Astrophysics & Computational Modelling Enthusiast

