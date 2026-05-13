# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

bl_info = {
    "name": "Sasha11711's Model Replacement Tools",
    "author": "Sasha11711",
    "description": "Scripts I found useful.",
    "blender": (5, 1, 0),
    "version": (0, 0, 3),
    "location": "View3D",
    "warning": "",
    "category": "Generic",
}

import bpy
from math import pi
from .operators import S11711_OT_DeleteZeroWeights, S11711_OT_HandleClothChain, S11711_OT_DeleteZeroShapekeys
from .ui import S11711_PT_UIPanel, S11711_PT_UIDeleteZeroWeights, S11711_PT_UIHandleClothChain, S11711_PT_UIDeleteZeroShapekeys

class S11711_Props(bpy.types.PropertyGroup):
    debug_mode: bpy.props.BoolProperty() # pyright: ignore[reportInvalidTypeForm]
    # Delete Zero Weights
    weight_epsilon: bpy.props.FloatProperty(default=1e-6, max=1.0, min=0.0, precision=6, step=1e-6) # pyright: ignore[reportInvalidTypeForm]
    # Handle Cloth Chain
    cloth_bone_length: bpy.props.FloatProperty(default=0.0, min=0.0, subtype="DISTANCE", description="0 - Keep existing length") # pyright: ignore[reportInvalidTypeForm]
    cloth_bone_x: bpy.props.FloatProperty(default=0.0, subtype="ANGLE") # pyright: ignore[reportInvalidTypeForm]
    cloth_bone_roll: bpy.props.FloatProperty(default=pi/2, subtype="ANGLE") # pyright: ignore[reportInvalidTypeForm]
    # Delete Zero Shapekeys
    shapekey_epsilon: bpy.props.FloatProperty(default=1e-6, max=1.0, min=0.0, precision=6, step=1e-6) # pyright: ignore[reportInvalidTypeForm]

classes = [
    S11711_Props,
    S11711_OT_DeleteZeroWeights,
    S11711_OT_HandleClothChain,
    S11711_OT_DeleteZeroShapekeys,
    S11711_PT_UIPanel,
    S11711_PT_UIDeleteZeroWeights,
    S11711_PT_UIHandleClothChain,
    S11711_PT_UIDeleteZeroShapekeys
]

def register():
    for cls in classes:
        bpy.utils.register_class(cls)
    bpy.types.Scene.s11711_props = bpy.props.PointerProperty(type=S11711_Props)

def unregister(): 
    for cls in classes:
        bpy.utils.unregister_class(cls)
    del bpy.types.Scene.s11711_props

if __name__ == "__main__":
    register()