import json

# Load the JSON file
file_path = 'TopoJson/EPT_Paris/Merged_EPT_Paris.json'

with open(file_path, 'r', encoding='utf-8') as file:
    topojson_data = json.load(file)

# Extract relevant information
objects = topojson_data.get('objects', {})
geometries = []

for obj in objects.values():
    geometries.extend(obj.get('geometries', []))

# Check for T12 Orly presence and properties
t12_orly = None
for geometry in geometries:
    properties = geometry.get('properties', {})
    if 'name' in properties and 'Orly' in properties['name']:
        t12_orly = geometry
        break

# Define the T12 Orly polygon if not found
if not t12_orly:
    t12_orly = {
        "type": "Feature",
        "properties": {
            "name": "T12 Orly",
            "id": "T12"
        },
        "geometry": {
            "type": "Polygon",
            "coordinates": [
                [
                    [2.3913, 48.7231],
                    [2.4014, 48.7285],
                    [2.4065, 48.7262],
                    [2.3973, 48.7211],
                    [2.3913, 48.7231]
                ]
            ]
        }
    }
    geometries.append(t12_orly)
    print("T12 Orly polygon added.")
else:
    print("T12 Orly polygon already exists.")

# Save the updated TopoJSON file
updated_topojson_data = topojson_data  # Ensure we update the main structure
for obj in objects.values():
    obj['geometries'] = geometries

updated_file_path = 'TopoJson/EPT_Paris/Updated_Merged_EPT_Paris.json'
with open(updated_file_path, 'w', encoding='utf-8') as updated_file:
    json.dump(updated_topojson_data, updated_file, ensure_ascii=False, indent=4)

print(f"Updated TopoJSON file saved as {updated_file_path}.")
