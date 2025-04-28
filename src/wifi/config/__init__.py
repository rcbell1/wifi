from dataclasses import dataclass, field

from .enums import Amendment, Modulation, Bandwidth, AckPolicy, Preamble
from .phy import PhyConfig, MimoConfig
from .mac import MacConfig

__all__ = [
    "Amendment",
    "Modulation",
    "Bandwidth",
    "PhyConfig",
    "MimoConfig",
    "MacConfig",
    "AckPolicy",
    "Preamble",
    "WifiConfig",
]


@dataclass
class WifiConfig:
    phy: PhyConfig = field(default_factory=PhyConfig)  # type: ignore
    mac: MacConfig = field(default_factory=MacConfig)
