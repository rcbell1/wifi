from dataclasses import dataclass

from .enums import AckPolicy


@dataclass
class MacConfig:
    slot_time_us: int = 9  # 9μs for 802.11a/g/n/ac/ax
    sifs_time_us: int = 16
    difs_time_us: int = 34
    rts_cts: bool = False
    fragmentation_threshold: int | None = None
    ack_policy: AckPolicy = AckPolicy.NORMAL
    retry_limit: int = 4
