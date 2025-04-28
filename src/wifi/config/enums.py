from enum import Enum


class Amendment(Enum):
    A = "802.11a"
    B = "802.11b"
    G = "802.11g"
    N = "802.11n"
    AC = "802.11ac"
    AX = "802.11ax"


class Modulation(Enum):
    BPSK = "BPSK"
    QPSK = "QPSK"
    QAM16 = "16-QAM"
    QAM64 = "64-QAM"
    QAM256 = "256-QAM"
    QAM1024 = "1024-QAM"


class Bandwidth(Enum):
    MHZ_20 = 20
    MHZ_40 = 40
    MHZ_80 = 80
    MHZ_160 = 160


class Preamble(Enum):
    LT = "legacy"  # only uses legacy STS and LTS
    HT = "high-throughput-mixed"  # after legacy, uses HT-STS and HT-LTS
    VHT = "very-high-throughput"  # the additional STS and LTS are modified
    HESU = "high-efficiency-single-user"
    HEMU = "high-efficiency-multi-user"


class AckPolicy(Enum):
    NORMAL = "normal"  # per-frame immediate ACK
    NO_ACK = "no-ack"  # unacknowledged
    BLOCK_ACK_IMMEDIATE = "block-ack-immediate"  # immediate compressed BA
    BLOCK_ACK_DELAYED = "block-ack-delayed"  # delayed compressed BA
    CF_ACK = "cf-ack"  # PCF contention-free ACK/poll
