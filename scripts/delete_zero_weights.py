def delete_zero_weights(obj, weight_epsilon: float, debug_mode: bool) -> int:
    if obj.type != "MESH":
        return 0
    
    me = obj.data
    vgs = obj.vertex_groups

    # copy list of groups so we don't hold direct references (null pointer possibility)
    vgs_copy = [vg for vg in vgs]

    groups_to_remove = []

    for vg in vgs_copy:
        has_nonzero = False
        gi = vg.index

        for v in me.vertices:
            for g in v.groups:
                if g.group == gi and g.weight > weight_epsilon:
                    has_nonzero = True
                    break
            if has_nonzero:
                break

        if not has_nonzero:
            groups_to_remove.append(vg.name)

    removed_count = 0
    for name in groups_to_remove:
        try:
            vg_fresh = obj.vertex_groups.get(name)
            if vg_fresh is not None:
                obj.vertex_groups.remove(vg_fresh)
                removed_count += 1
                if debug_mode: print(f"Removed zero-weight group '{name}' from '{obj.name}'")
        except Exception as e:
            print(f"Failed to remove vertex group '{name}' from '{obj.name}': {e}")

    return removed_count
