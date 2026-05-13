import bpy
import math
from mathutils import Matrix


def handle_cloth_chain(edit_bone: bpy.types.EditBone, cloth_bone_length: float, cloth_bone_x: float, cloth_bone_roll: float, debug_mode: bool):
    custom_bone_length = cloth_bone_length
    bone = edit_bone
    while bone:
        if not bone.children:
            if bone.parent:
                parent = bone.parent # type: bpy.types.EditBone
                bone.align_orientation(parent)
                if custom_bone_length: bone.length = cloth_bone_length
                bone = None
            else:
                if debug_mode: print("Active edit bone has neither a parent nor a child.")
                return
        else:
            child_bone = bone.children[0] # type: bpy.types.EditBone
            child_bone.use_connect = False
            if not custom_bone_length: cloth_bone_length = bone.length
            bone.tail = child_bone.head
            bone.length = cloth_bone_length
            bone.roll = 0
            bone_vector = bone.vector
            bone_matrix = bone.matrix.copy()
            bone.transform(bone_matrix
                           @ Matrix.Rotation(math.radians(-90), 4, 'Z')
                           @ Matrix.Rotation(cloth_bone_x, 4, 'X')
                           @ bone_matrix.inverted())
            bone.align_roll(bone_vector)
            bone.roll += cloth_bone_roll
            bone = child_bone