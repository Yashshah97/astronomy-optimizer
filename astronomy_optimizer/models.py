from dataclasses import dataclass, field
from typing import List

@dataclass(frozen=True)
class Star:
    """
    A star in a catalog.

    Attributes:
        name (str): Name of the star.
        ra (float): Right Ascension in degrees.
        dec (float): Declination in degrees.
        magnitude (float): Magnitude of the star.
    """

    name: str
    ra: float  # Right Ascension in degrees
    dec: float  # Declination in degrees
    magnitude: float

    def __post_init__(self):
        if not (0 <= self.ra < 360 and -90 <= self.dec <= 90):  
            raise ValueError("RA must be between 0 and 360, DEC must be between -90 and 90")
        if self.magnitude < 0:
            raise ValueError("Magnitude cannot be negative")

@dataclass(frozen=True)
class LightCurve:
    """
    A light curve for a star.

    Attributes:
        star_name (str): Name of the star.
        time_points (List[float]): Time points in days since JD 2451545.0 (IAU epoch).
        flux_values (List[float]): Flux values corresponding to each time point.
    """

    star_name: str
    time_points: List[float]  # Time points in days since JD 2451545.0 (IAU epoch)
    flux_values: List[float]

    def __post_init__(self):
        if len(self.time_points) != len(self.flux_values):
            raise ValueError("Time points and flux values must have the same length")
        for time, flux in zip(self.time_points, self.flux_values):
            if not (time >= 0):  
                raise ValueError("Time cannot be negative")

@dataclass(frozen=True)
class ParameterSet:
    """
    A set of parameters to optimize.

    Attributes:
        stars (List[Star]): List of stars.
        light_curves (List[LightCurve]): List of light curves.
    """

    stars: List[Star]
    light_curves: List[LightCurve]

    def __post_init__(self):
        if not all(isinstance(star, Star) for star in self.stars):
            raise ValueError("All elements in 'stars' must be instances of Star")
        if not all(isinstance(light_curve, LightCurve) for light_curve in self.light_curves):
            raise ValueError("All elements in 'light_curves' must be instances of LightCurve")

    def add_star(self, star: Star):
        """
        Add a new star to the parameter set.

        Args:
            star (Star): The star to add.
        """
        if any(s.name == star.name for s in self.stars):
            raise ValueError("A star with this name already exists")
        self.stars.append(star)

    def remove_star(self, star_name: str):
        """
        Remove a star from the parameter set by its name.

        Args:
            star_name (str): Name of the star to remove.
        """
        if not any(s.name == star_name for s in self.stars):
            raise ValueError("No star with this name exists")
        self.stars = [s for s in self.stars if s.name != star_name]

    def add_light_curve(self, light_curve: LightCurve):
        """
        Add a new light curve to the parameter set.

        Args:
            light_curve (LightCurve): The light curve to add.
        """
        if any(s.name == light_curve.star_name for s in self.stars) and not any(lc.star_name == light_curve.star_name for lc in self.light_curves):
            raise ValueError("A light curve for this star already exists")
        self.light_curves.append(light_curve)
