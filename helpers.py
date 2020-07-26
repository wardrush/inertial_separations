import pandas as pd
import numpy as np
import scipy

"""
General structure: Each specified flow system is made into an object and further calculations can be made with internal 
methods. 
TODO: consider making the calculated values properties within the class
"""


class FlowSystem:
    def __init__(self, flow_rate, hydraulic_diameter, particle_diameter, fluid_density, dynamic_viscosity,
                 curvature_radius, **kwargs):
        """
        Initializes the specified FlowSystem object. Only base values/important attributes are initialized. Calculation
        methods must be called by user in order to reduce unnecessary computational load.
        **kwargs option provided to pass additional arguments for future functions

        !!Defaults provided for pure water at 20C!!

        :param flow_rate: Maximum flow rate; given in m^3/s
        :param hydraulic_diameter: Hydraulic diameter/Characteristic length; given in m
        :param fluid_density: Density/Rho of fluid; given in kg/cum
        :param dynamic_viscosity: Dynamic viscosity/mu of fluid; given in Pa/s
        :param particle_diameter: Representative diameter of particle; given in m
        :param curvature_radius: A representative radius of curvature for the given system; given in m
        """
        self.flow_rate = flow_rate if flow_rate else None
        self.fluid_velocity = fluid_velocity if fluid_velocity else None
        self.hydraulic_diameter = hydraulic_diameter if hydraulic_diameter else None
        self.fluid_density = fluid_density if fluid_density else 1000
        self.dynamic_viscosity = dynamic_viscosity if dynamic_viscosity else 0.001002
        self.particle_diameter = particle_diameter if particle_diameter else None
        self.curvature_radius = curvature_radius if curvature_radius else None
        # Initializing variables that might not be calculated#
        if self.flow_rate:
            self.fluid_velocity = flow_rate / (0.25*np.pi*hydraulic_diameter^2)
        self.channel_reynolds_number = None
        self.particle_reynolds_number = None
        self.deans_number = None

        for key, value in kwargs.items():
            setattr(self, key, value)

    def __repr__(self):
        return f'{self.__class__.__name__}('f'{self.flow_rate!r}, {self.curvature_radius!r})'

    def return_channel_reynolds_number(self):
        """
        Returns the channel reynolds value for a given system. Defaults are for water at 20C
        This is the more widely used Reynolds number. The particle Reynolds number is for specific use cases.
        See notes in "return_particle_reynolds_number" docstring
        :return: Channel Reynolds number for given system
        :rtype: float
        """
        self.channel_reynolds_number = (self.fluid_density * self.fluid_velocity * self.hydraulic_diameter) / self.dynamic_viscosity
        return float(self.channel_reynolds_number)

    def return_particle_reynolds_number(self):
        """
        Returns the particle reynolds value for a given system. Defaults are for water at 20C
        This is a specific use case Reynolds number for systems in which the fluid flow contains particles on the same order
        of magnitude of the channel cross section (hydraulic_diameter). Confinement ratio is calculated as an intermediate
        value in case it is useful in the future.
        :return: Particle reynolds number for given system
        :rtype: float
        """
        self.confinement_ratio = self.particle_diameter / self.hydraulic_diameter
        self.particle_reynolds_number = self.return_channel_reynolds_number*self.confinement_ratio
        return self.particle_reynolds_number

    def return_deans_number(self):
        """
        Returns the Dean's number for a given system. Default values are for water at 20C
        Dean's number is a dimensionless values that represents second order flow dynamics in curving system caused by
        higher speed fluids flowing from the inner wall to the outer wall. A higher Dean's number indicates a stronger flow
        of this type.
        :return: Representative Dean's number for given system
        :rtype: float
        """
        self.deans_number = self.return_channel_reynolds_number * np.sqrt(
            self.hydraulic_diameter / (2 * self.curvature_radius))
        return self.deans_number
