import csv
from datetime import datetime
import subprocess

def generate_system_context_puml(csv_file_path):
    current_datetime = datetime.now().strftime("%Y%m%d_%H%M%S")
    puml_file_path = f"C4_System_Context_{current_datetime}.puml"

    puml_content = "@startuml\n"
    puml_content += "!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/master/C4_Context.puml\n"
    puml_content += "!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/master/C4_Container.puml\n"
    puml_content += "AddRelTag(\"Tag1\")\n"
    puml_content += "AddRelTag(\"Tag2\", $lineColor=\"Green\", $textColor=\"Green\")\n"
    puml_content += "AddElementTag(\"Tag3\")\n"
    puml_content += "AddElementTag(\"Tag4\", $bgColor=\"#FFCC00\")\n"
    
    entities = {}
    boundaries = {}
    boundary_descriptions = {}  # Dictionary to hold boundary descriptions
    interactions = []
    reading_entities = True

    with open(csv_file_path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if not row or not any(row):  # Skip empty rows
                continue

            if row[0] == "Source":  # Detect start of relationships section
                reading_entities = False
                continue

            if reading_entities:
                if row[0] == "Entity Type":  # Skip the header row of entity section
                    continue

                # Unpack entity information with boundary, description, and tag
                entity_data = row[:6]  # Ensure no unpacking error
                entity_type, entity_name, description, boundary, boundary_description, tag = entity_data
                identifier = entity_name.replace(" ", "_")
                entities[entity_name] = (entity_type, identifier, description, boundary, tag)
                if boundary:
                    boundaries.setdefault(boundary, []).append(entity_name)
                    boundary_descriptions[boundary] = boundary_description
            else:
                if row[0] == "Source":  # Skip the header row of relationship section
                    continue

                # Unpack relationship information
                relationship_data = row[:5]  # Ensure no unpacking error
                source, destination, rel_description, technology, rel_tag = relationship_data
                interactions.append((source, destination, rel_description, technology, rel_tag))

    # Process entities within boundaries
    for boundary, entity_names in boundaries.items():
        boundary_desc = boundary_descriptions.get(boundary, "")
        puml_content += f"Boundary({boundary.replace(' ', '_')}, \"{boundary}\""
        if boundary_desc:
            puml_content += f", \"{boundary_desc}\""
        puml_content += ") {\n"
        for entity_name in entity_names:
            entity_type, identifier, description, _, entity_tag = entities[entity_name]
            entity_line = f"  {entity_type}({identifier}, \"{entity_name}\", \"{description}\""
            if entity_tag:
                entity_line += f", $tags=\"{entity_tag}\""
            entity_line += ")"
            puml_content += entity_line + "\n"
        puml_content += "}\n"

    # Process entities not in any boundary
    for entity_name, (entity_type, identifier, description, boundary, entity_tag) in entities.items():
        if not boundary:
            entity_line = f"{entity_type}({identifier}, \"{entity_name}\", \"{description}\""
            if entity_tag:
                entity_line += f", $tags=\"{entity_tag}\""
            entity_line += ")"
            puml_content += entity_line + "\n"

    # Process interactions
    for source, destination, rel_description, technology, rel_tag in interactions:
        source_id = entities[source][1]
        destination_id = entities[destination][1]
        rel_line = f"Rel({source_id}, {destination_id}, \"{rel_description}\", \"{technology}\""
        rel_line += f", $tags=\"{rel_tag}\")" if rel_tag else ")"
        puml_content += rel_line + "\n"

    puml_content += "SHOW_LEGEND()\n"
    puml_content += "@enduml\n"

    with open(puml_file_path, 'w') as puml_file:
        puml_file.write(puml_content)
    
    return puml_file_path

def generate_diagram(puml_file_path):
    plantuml_jar_path = "C:\\plantuml-1.2023.13.jar" # Replace with the path to your jar file
    output_format = "-tpng"
    command = f"java -jar \"{plantuml_jar_path}\" {output_format} \"{puml_file_path}\""
    subprocess.run(command, shell=True)

# Usage
csv_path = "C4_System_Context.csv"  # Replace with the path to your CSV file
output_puml_file = generate_system_context_puml(csv_path)
print(f"PUML file generated: {output_puml_file}")

# Generate diagram image
generate_diagram(output_puml_file)
