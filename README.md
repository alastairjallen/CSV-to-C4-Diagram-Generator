# CSV-to-C4-Diagram-Generator

A Python tool for converting CSV data into PlantUML C4 model diagrams. This script facilitates the visualization of system architectures, relationships, and boundaries using a simple and intuitive CSV format.

## Features

- Generate C4 model diagrams from CSV files.
- Define system components, relationships, and boundaries in CSV.
- Support for custom tagging of entities and relationships.
- Automated generation of PNG diagram images.

## Getting Started

### Prerequisites

- Python 3.x
- Java Runtime Environment
- PlantUML
- Graphviz

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/alastairjallen/CSV-to-C4-Diagram-Generator.git

	2.	Navigate to the cloned directory:

cd CSV-to-C4-Diagram-Generator



Usage

	1.	Prepare your CSV file according to the format specified in the CSV Format section below.
	2.	Run the script with the path to your CSV file:

python csv_to_c4_diagram_generator.py your_file.csv


	3.	The script will generate a PUML file and a PNG image of the diagram.

CSV Format

Entities Section

	•	Format: Entity Type, Entity Name, Description, Boundary, Boundary Description, Tag
	•	Example:

Person, User, User of the payment system, User Boundary, Description of User Boundary, 
System, Payment System, Processes user payments, Payment Boundary, Description of Payment Boundary, 



Relationships Section

	•	Format: Source, Destination, Description, Technology, Tag
	•	Example:

User, Payment System, Submits payment, HTTPS, 
Payment System, Bank, Processes payment, REST API, Future Scope



Contributing

Contributions to the project are welcome! Please refer to the contributing guidelines for more details.

License

This project is licensed under the MIT License.

Acknowledgments

	•	PlantUML Team
	•	Graphviz Team