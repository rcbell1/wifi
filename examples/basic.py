from wifi.config import (
    WifiConfig,
    PhyConfig,
    MimoConfig,
    MacConfig,
    Amendment,
    Modulation,
    Bandwidth,
    AckPolicy,
    Preamble,
)

from wifi.phy import Transmitter, Receiver
from wifi.channel import Channel
from wifi.payload import Payload

n_20mhz = WifiConfig(
    phy=PhyConfig(
        amendment=Amendment.N,
        modulation=Modulation.QAM16,  # max 64-QAM in 11n
        bandwidth=Bandwidth.MHZ_20,
        guard_interval_ns=400,  # short GI
        preamble_type=Preamble.LT,
        mimo=MimoConfig(enabled=True, spatial_streams=1, sounding=True),
    ),
    mac=MacConfig(
        slot_time_us=9,  # OFDM slot time
        sifs_time_us=16,
        difs_time_us=16 + 2 * 9,  # = 34 μs
        rts_cts=False,
        fragmentation_threshold=2346,  # default MPDU size
        ack_policy=AckPolicy.NORMAL,
        retry_limit=4,
    ),
)

tx = Transmitter(n_20mhz)
chan = Channel(type="awgn", snr_db=20)
rx = Receiver(n_20mhz)
bits = Payload(num_bits=1000).generate()

tx_samples = tx.send(bits)

rx_samples = chan.apply(tx_samples)

rx_bits = rx.receive(rx_samples)
