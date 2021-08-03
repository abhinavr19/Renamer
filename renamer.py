import maya.cmds as mc

suffixes = {"mesh": "geo", "joint": "jnt", "camera": None}
ds = "grp"


def renamer():
    selection = mc.ls(selection=True)

    if len(selection) == 0:
        selection = mc.ls(dag=True, long=True)
    selection.sort(key=len, reverse=True)

    for obj in selection:
        shortName = obj.split("|")[-1]
        children = mc.listRelatives(obj, children=True) or []
        if len(children) == 1:
            child = children[0]
            objType = mc.objectType(child)
        else:
            objType = mc.objectType(obj)

        suffix = suffixes.get(objType, ds)

        if not suffix:
            continue

        if obj.endswith('_' + suffix):
            continue

        newName = shortName + "_" + suffix
        mc.rename(obj, newName)
        print ("After rename: ", newName)


renamer()
