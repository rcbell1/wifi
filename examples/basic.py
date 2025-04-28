from wifi import Transmitter, Receiver, Channel, Payload, WifiConfig

n_20mhz = WifiConfig()

tx = Transmitter(n_20mhz)
chan = Channel(type="awgn", snr_db=20)
rx = Receiver(n_20mhz)
bits = Payload(num_bits=1000).generate()

tx_samples = tx.send(bits)

rx_samples = chan.apply(tx_samples)

rx_bits = rx.receive(rx_samples)
