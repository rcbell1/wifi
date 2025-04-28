from dataclasses import dataclass, field

from .enums import Amendment, Modulation, Bandwidth, Preamble


@dataclass
class MimoConfig:
    enabled: bool = False
    spatial_streams: int = 1
    sounding: bool = False  # e.g. for beamforming


@dataclass
class PhyConfig:
    amendment: Amendment = Amendment.N
    modulation: Modulation = Modulation.BPSK
    bandwidth: Bandwidth = Bandwidth.MHZ_20
    preamble_type: Preamble = Preamble.LT
    mimo: MimoConfig = field(default_factory=MimoConfig)
    guard_interval_ns: int = 800  # e.g. 800ns or 400ns
