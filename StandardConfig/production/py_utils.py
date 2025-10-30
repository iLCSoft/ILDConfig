from typing import Dict, List


def get_drop_collections(calib: Dict[str, str], cmds: bool) -> List[str]:
    """Get the collections to drop from the calibration

    Combine all the different sources for dropping collections into one list.
    These sources are
    - DropCollectionsCalibrationREC (i.e. the ones defined in the calibration)
    - AdditionalDropCollectionsREC (i.e. user defined ones)

    Args:
        calib (Dict[str, str]): The calibration configuration
        cmds (bool): Whether or not the list should be turned into a list of
            keep / drop commands as used by EDM4hep output

    Returns:
        List [str]: A list of collections to drop
    """
    drop_calib = calib.get("DropCollectionsCalibrationREC", "")
    drop_calib = drop_calib.split(" ") if drop_calib else []
    drop_add = calib.get("AdditionalDropCollectionsREC", "")
    drop_add = drop_add.split(" ") if drop_add else []

    prefix = "drop " if cmds else ""
    return [f"{prefix}{c}" for c in drop_calib + drop_add]


def _append_commas_expect_last(config_list, list_to_add):
    """Append a comma to each string in the list except the last one."""
    config_list.extend([f"{ele}," for ele in list_to_add[:-1]] + [list_to_add[-1]])


def encode_CT_steps_dict_to_legacy_list(steps_dict: dict) -> list[str]:
    """
    Encode the conformal tracking configuration into the list of strings that is expected by the Marlin processor
    """
    legacy_list = []

    # Loop over steps
    for step_name, step in steps_dict.items():
        legacy_list.append(f"[{step_name}]")

        # Collections
        legacy_list.extend(["@Collections", ":"])
        _append_commas_expect_last(legacy_list, step.get("collections"))

        # Parameters
        legacy_list.extend(["@Parameters", ":"])
        for key, value in step.get("params", {}).items():
            if key in ["SlopeZRange", "HighPTCut"]:
                legacy_list.append(f"{key}:")
            else:
                legacy_list.append(str(key))
                legacy_list.append(":")
            legacy_list.append(f"{value};")

        # Flags
        flags = step.get("flags", [])
        if flags:
            legacy_list.extend(["@Flags", ":"])
            _append_commas_expect_last(legacy_list, flags)

        # Functions
        functions = step.get("functions", [])
        if functions:
            legacy_list.extend(["@Functions", ":"])
            _append_commas_expect_last(legacy_list, functions)

    return legacy_list
