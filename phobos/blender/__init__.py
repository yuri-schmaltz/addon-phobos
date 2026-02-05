#!/usr/bin/python3
# coding=utf-8

# -------------------------------------------------------------------------------
# This file is part of Phobos, a Blender Add-On to edit robot models.
# Copyright (C) 2020 University of Bremen & DFKI GmbH Robotics Innovation Center
#
# You should have received a copy of the 3-Clause BSD License in the LICENSE file.
# If not, see <https://opensource.org/licenses/BSD-3-Clause>.
# -------------------------------------------------------------------------------

# Re-export add-on metadata and common submodules for Blender-side tests/utilities.
# Keep imports guarded so CLI/API usage outside Blender doesn't fail.
try:
    import bpy  # noqa: F401
    _BPY_AVAILABLE = True
except ImportError:
    _BPY_AVAILABLE = False

from . import reserved_keys  # noqa: F401

if _BPY_AVAILABLE:
    from .. import bl_info  # noqa: F401
    from . import model  # noqa: F401
    from . import operators  # noqa: F401
    from . import utils  # noqa: F401
    from . import io  # noqa: F401
    from . import phobosgui  # noqa: F401
    from . import display  # noqa: F401
    from . import defs  # noqa: F401
