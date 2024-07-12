import json

# Load the JSON file
with open('TopoJson\EPT_Paris\Merged_EPT_Paris.json', 'r', encoding='utf-8') as file:
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

t12_orly
