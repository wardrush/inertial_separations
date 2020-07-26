import pandas as pd
import numpy as np
import scipy
from helpers import FlowSystem

"""
Created July 22, 2020 
by Ward Rushton
Inertial separations Simulation #1
Purpose: To find reasonable starting values for designing the inertial microfludic system from the defined bounds
See Inertial Microfluidics paper

Notes: 
7/22/20
-Simulations will begin assuming cylindrical tubing for simplicity--aspect ratio greatly affects fluid flow 
-Assume 7 gal/wash [26,500ml] for starting (Whirlpool WFW85HEFW) and 1000mL/min of flow
-Assume hydraulic diameter can be no larger than 1.5cm (can be changed. off the cuff number)


FAQ: 

Q: What are the boundary conditions for the system?
A: Flow must remain laminar (<1800 ideally, <2000 for sure), pressure drop must be minimized, channel dimensions should
    be something industrially available

Q: What values can be physically modified to affect resulting system (i.e. density is chosen by universe)?
A: Flow velocity, channel dimensions, and curvature radius are the most easily affected variables
"""

"""
Finding bounds for Re
Re = f(density, max velocity, diameter, dynamic viscosity) where we can affect max velocity and diameter
max velocity = g(diameter, fluid flow rate)

Re = (rho/mu)*(flow rate/cross sectional area)*hydraulic diameter  
cross sectional area = pi*(hydraulic diameter / 2)^2

Re = (rho/mu)*(flow rate/ [pi*hydraulic diameter^2/4])*hydraulic diameter  
Re = (rho/mu)*(flow rate/(pi*hydraulic diameter/4))
Re*(mu/rho)*(4*pi/flow rate) = 1/hydraulic diameter
(rho/(mu*re))*(flow rate/4*pi) = hydraulic diameter
"""

