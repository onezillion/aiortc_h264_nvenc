"""
Shim module so Omniverse Kit's pipapi import-check passes.

This package's real import is `aiortc`, but Kit checks `import <requirement_name>`.
"""
from aiortc import *  # re-export (optional)
