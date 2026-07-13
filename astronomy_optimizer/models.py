from dataclasses import dataclass, field
from typing import List

@dataclass(frozen=True)
class Star:
    """A star in a catalog."""
    name: str
    ra: float  # Right Ascension in degrees
    dec: float  # Declination in degrees
    magnitude: float

    def __post_init__(self):
        if not (0 <= self.ra < 360 and 0 <= self.dec < 90):
            raise ValueError("RA and DEC must be within valid ranges")

@dataclass(frozen=True)
class LightCurve:
    """A light curve for a star."""
    star_name: str
    time_points: List[float]  # Time points in days since JD 2451545.0 (IAU epoch)
    flux_values: List[float]

    def __post_init__(self):
        if len(self.time_points) != len(self.flux_values):
            raise ValueError("Time points and flux values must have the same length")

@dataclass(frozen=True)
class ParameterSet:
    """A set of parameters to optimize."""
    stars: List[Star]
    light_curves: List[LightCurve]

    def __post_init__(self):
        if not all(isinstance(star, Star) for star in self.stars):
            raise ValueError("All elements in 'stars' must be instances of Star")
        if not all(isinstance(light_curve, LightCurve) for light_curve in self.light_curves):
            raise ValueError("All elements in 'light_curves' must be instances of LightCurve")
