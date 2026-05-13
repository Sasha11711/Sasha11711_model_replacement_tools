from bpy.types import Context, Panel
from .operators import S11711_OT_DeleteZeroWeights, S11711_OT_HandleClothChain, S11711_OT_DeleteZeroShapekeys

class BasePanel:
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Sasha11711"


class S11711_PT_UIPanel(BasePanel, Panel):
    bl_idname = "S11711_PT_UIPanel"
    bl_label = "Sasha11711"

    def draw(self, context: Context):
        props = context.scene.s11711_props

        layout = self.layout
        layout.use_property_split = True
        layout.use_property_decorate = False  # No animation.

        layout.prop(props, "debug_mode", text="Debug mode")


class S11711_PT_UIDeleteZeroWeights(BasePanel, Panel):
    bl_idname = "S11711_PT_UIDeleteZeroWeights"
    bl_parent_id = "S11711_PT_UIPanel"
    bl_label = "Delete Zero Weights"
    # bl_context = 'objectmode'
    # bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context: Context):
        props = context.scene.s11711_props

        layout = self.layout
        layout.use_property_split = True
        layout.use_property_decorate = False  # No animation.

        layout.prop(props, "weight_epsilon", text="Weight Epsilon")

        layout.operator(S11711_OT_DeleteZeroWeights.bl_idname, icon="GROUP_VERTEX")
        # layout.separator()


class S11711_PT_UIHandleClothChain(BasePanel, Panel):
    bl_idname = "S11711_PT_UIHandleClothChain"
    bl_parent_id = "S11711_PT_UIPanel"
    bl_label = "Handle Cloth Chain"
    # bl_context = 'objectmode'
    # bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context: Context):
        props = context.scene.s11711_props

        layout = self.layout
        layout.use_property_split = True
        layout.use_property_decorate = False  # No animation.

        layout.prop(props, "cloth_bone_length", text="Bone Length")

        col = layout.column(align=True)
        col.prop(props, "cloth_bone_x", text="Rotation x")
        col.prop(props, "cloth_bone_roll", text="y (roll)")

        layout.operator(S11711_OT_HandleClothChain.bl_idname, icon="CON_SPLINEIK")
        # layout.separator()


class S11711_PT_UIDeleteZeroShapekeys(BasePanel, Panel):
    bl_idname = "S11711_PT_UIDeleteZeroShapekeys"
    bl_parent_id = "S11711_PT_UIPanel"
    bl_label = "Delete Empty Shapekeys"
    # bl_context = 'objectmode'
    # bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context: Context):
        props = context.scene.s11711_props

        layout = self.layout
        layout.use_property_split = True
        layout.use_property_decorate = False  # No animation.

        layout.prop(props, "shapekey_epsilon", text="Shapekey Epsilon")

        layout.operator(S11711_OT_DeleteZeroShapekeys.bl_idname, icon="SHAPEKEY_DATA")
        # layout.separator()