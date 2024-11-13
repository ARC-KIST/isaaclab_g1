"""Package containing asset and sensor configurations."""

import os
import toml

##
# Configuration for different assets.
##

# Conveniences to other module directories via relative paths
ISAACLAB_G1_EXT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__)))
"""Path to the extension source directory."""

# ISAACLAB_G1_DATA_DIR = os.path.join(ISAACLAB_G1_EXT_DIR, "data")
"""Path to the extension data directory."""

# ISAACLAB_G1_METADATA = toml.load(os.path.join(ISAACLAB_G1_EXT_DIR, "config", "extension.toml"))
"""Extension metadata dictionary parsed from the extension.toml file."""

# Configure the module-level variables
# __version__ = ISAACLAB_G1_METADATA["package"]["version"]


from .g1 import *
