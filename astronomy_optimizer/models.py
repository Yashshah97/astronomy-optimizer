from dataclasses import dataclass
from typing import List

@dataclass(frozen=True)
class Star:
    """A star in a catalog."""
    name: str
    ra: float  # Right Ascension in degrees
    dec: float  # Declination in degrees
    magnitude: float

@dataclass(frozen=True)
class LightCurve:
    """A light curve for a star."""
    star_name: str
    time_points: List[float]  # Time points in days since JD 2451545.0 (IAU epoch)
    flux_values: List[float]

@dataclass(frozen=True)
class ParameterSet:
    """A set of parameters to optimize."""
    stars: List[Star]
    light_curves: List[LightCurve]
