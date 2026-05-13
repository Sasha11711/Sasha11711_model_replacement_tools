#TODO
import bpy

def map_vertex_group_names(mapping: dict, debug_mode: bool):
    #   "[old_name]": "[deadlock_name]",

    for obj in bpy.context.selected_objects:
        if obj.type != 'MESH':
            continue

        vgroups = obj.vertex_groups
        for key in mapping.keys():
            if key == mapping[key]:
                obj.vertex_groups.new(name = key)
            elif key in vgroups:
                if mapping[key] in vgroups:
                    if debug_mode: print(f"Skipped \"{key}\" -> \"{mapping[key]}\" on {obj.name} (target exists)")
                else:
                    vgroups[key].name = mapping[key]

#for obj in bpy.context.selected_bones:
#    print(f"\"{obj.name}\": \"{obj.name}\",")