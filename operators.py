import bpy 
from .scripts.delete_zero_weights import delete_zero_weights
from .scripts.handle_cloth_chain import handle_cloth_chain
from .scripts.delete_zero_shapekeys import delete_zero_shapekeys

class S11711_OT_DeleteZeroWeights(bpy.types.Operator):
    """Delete useless vertex groups.
    (in selected objects)"""
    bl_idname = "s11711.delete_zero_weights"
    bl_label = "Delete Zero Weights"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(self, context):
        for obj in context.selected_objects:
            if obj.type == "MESH":
                return True
        return False
    
    def execute(self, context):
        props = context.scene.s11711_props
        weight_epsilon = props.weight_epsilon # type: float
        debug_mode = props.debug_mode # type: bool

        if not debug_mode:
            for obj in context.selected_objects:
                delete_zero_weights(obj, weight_epsilon, False)
        else:
            total_removed = 0
            for obj in context.selected_objects:
                total_removed += delete_zero_weights(obj, weight_epsilon, True)
            print(f"Done. Removed {total_removed} zero-weight vertex group(s).")

        return {'FINISHED'}


class S11711_OT_HandleClothChain(bpy.types.Operator):
    """Adjust a chain of bones to work better as a Source 2 cloth chain.
    (starting from the active edit bone)"""
    bl_idname = "s11711.handle_cloth_chain"
    bl_label = "Handle Cloth Chain"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(self, context):
        return context.mode == "EDIT_ARMATURE" and context.active_bone in context.selected_bones
    
    def execute(self, context):
        props = context.scene.s11711_props
        cloth_bone_length = props.cloth_bone_length # type: float
        cloth_bone_x = props.cloth_bone_x # type: float
        cloth_bone_roll = props.cloth_bone_roll # type: float
        debug_mode = props.debug_mode # type: bool
        handle_cloth_chain(context.active_bone, cloth_bone_length, cloth_bone_x, cloth_bone_roll, debug_mode)
        
        return {'FINISHED'}


class S11711_OT_DeleteZeroShapekeys(bpy.types.Operator):
    """Delete useless shapekeys.
    (in selected objects)"""
    bl_idname = "s11711.delete_zero_shapekeys"
    bl_label = "Delete Empty Shapekeys"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(self, context):
        for obj in context.selected_objects:
            if obj.type == "MESH":
                return True
        return False
    
    def execute(self, context):
        props = context.scene.s11711_props
        shapekey_epsilon = props.shapekey_epsilon # type: float
        debug_mode = props.debug_mode # type: bool

        if not debug_mode:
            for obj in context.selected_objects:
                delete_zero_shapekeys(obj, shapekey_epsilon, False)
        else:
            total_removed = 0
            for obj in context.selected_objects:
                total_removed += delete_zero_shapekeys(obj, shapekey_epsilon, True)
            print(f"Done. Removed {total_removed} empty shapekey(s).")

        return {'FINISHED'}
    