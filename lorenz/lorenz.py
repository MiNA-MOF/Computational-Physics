# lorenz.py
import numpy as np

def lorenz_derivatives(state, t, sigma=10.0, rho=28.0, beta=8/3):
    """Oblicza pochodne układu Lorenza (dx/dt, dy/dt, dz/dt)."""
    x, y, z = state
    dxdt = sigma * (y - x)
    dydt = x * (rho - z) - y
    dzdt = x * y - beta * z
    return [dxdt, dydt, dzdt]