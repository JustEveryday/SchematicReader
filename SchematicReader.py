import nbt
import json

def nbt_to_dict(nbt_tag):
    if isinstance(nbt_tag, nbt.nbt.TAG_Compound):
        return {tag.name: nbt_to_dict(tag) for tag in nbt_tag.tags}
    elif isinstance(nbt_tag, nbt.nbt.TAG_List):
        return [nbt_to_dict(tag) for tag in nbt_tag]
    elif isinstance(nbt_tag, nbt.nbt.TAG_Byte):
        return nbt_tag.value
    elif isinstance(nbt_tag, nbt.nbt.TAG_Short):
        return nbt_tag.value
    elif isinstance(nbt_tag, nbt.nbt.TAG_Int):
        return nbt_tag.value
    elif isinstance(nbt_tag, nbt.nbt.TAG_Long):
        return nbt_tag.value
    elif isinstance(nbt_tag, nbt.nbt.TAG_Float):
        return nbt_tag.value
    elif isinstance(nbt_tag, nbt.nbt.TAG_Double):
        return nbt_tag.value
    elif isinstance(nbt_tag, nbt.nbt.TAG_Byte_Array):
        return list(nbt_tag.value)
    elif isinstance(nbt_tag, nbt.nbt.TAG_String):
        return nbt_tag.value
    elif isinstance(nbt_tag, nbt.nbt.TAG_Int_Array):
        return list(nbt_tag.value)
    elif isinstance(nbt_tag, nbt.nbt.TAG_Long_Array):
        return list(nbt_tag.value)
    else:
        return str(nbt_tag)

def schem_to_json(schem_file_path, json_file_path):
   
    nbt_data = nbt.nbt.NBTFile(schem_file_path, 'rb')

    schem_dict = nbt_to_dict(nbt_data)

    with open(json_file_path, 'w') as json_file:
        json.dump(schem_dict, json_file, indent=4)

schem_file_path = '<Pfad zur Schematic Datei>'
json_file_path = '<Pfad zur JSON-Datei, die automatisch erstellt wird>'


schem_to_json(schem_file_path, json_file_path)

print(f"Die .schem-Datei wurde erfolgreich in JSON konvertiert und unter {json_file_path} gespeichert.")
