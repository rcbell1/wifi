# WiFi

This project implements physical (PHY) and media-access-control (MAC) layer algorithms, used by WiFi, in Python. It is intended to be a useful tool to learn from, not a bit level accurate implementation of any particular 802.11 amendment (i.e. a/b/g/n/ac/ax). No guarantee is made that this code replicates any particular standard, however, the goal is to use the same algorithms and packet structure that production WiFi devices use.

# Setup

This project uses the `uv` Python package manager for installation. Run the following commands to setup the project:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh   # download and install uv
git clone git@github.com:rcbell1/wifi.git         # clones the git repo
cd wifi
uv sync                                           # installs all dependencies

```

# Where do I start?

I recommend running the `examples/basic.py` script to begin. If you understand how this script works, you are ready to write your own.
