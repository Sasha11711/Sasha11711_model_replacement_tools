def delete_zero_shapekeys(obj, shapekey_epsilon: float, debug_mode: bool) -> int:
    if obj.type != 'MESH':
        return 0

    sk_data = obj.data.shape_keys
    if not sk_data:
        return 0

    basis = sk_data.key_blocks.get("Basis")
    if not basis:
        return 0

    keys_to_remove = []

    for key in sk_data.key_blocks:
        if key == basis:
            continue

        is_empty = True
        for i, kb_vert in enumerate(key.data):
            if (kb_vert.co - basis.data[i].co).length > shapekey_epsilon:
                is_empty = False
                break

        if is_empty:
            keys_to_remove.append(key)

    for key in reversed(keys_to_remove):
        if debug_mode: print(f"Removing empty shapekey '{key.name}' from '{obj.name}'")
        obj.shape_key_remove(key)
    
    if len(sk_data.key_blocks) == 1:
        obj.shape_key_remove(sk_data.key_blocks[0])

    return len(keys_to_remove)
