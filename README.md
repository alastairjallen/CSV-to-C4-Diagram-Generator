# CSV-to-C4-Diagram-Generator

A Python tool for converting CSV data into PlantUML C4 model diagrams. This script facilitates the visualization of system architectures, relationships, and boundaries using a simple and intuitive CSV format. The tool supports generating C4 model diagrams from CSV files and defining system components, relationships, and boundaries in CSV. It also supports custom tagging of entities and relationships and automated generation of PNG diagram images.

### Getting Started
To use this tool, you need Python 3.x, Java Runtime Environment, PlantUML, and Graphviz installed on your system. 

To install, first clone the repository using `git clone https://github.com/[your-username]/CSV-to-C4-Diagram-Generator.git`, then navigate to the cloned directory with `cd CSV-to-C4-Diagram-Generator`. 

### Usage
Prepare your CSV file according to the specified format. Run the script with the path to your CSV file using `python csv_to_c4_diagram_generator.py your_file.csv`. The script will generate a PUML file and a PNG image of the diagram.

### CSV Format
The CSV file should be structured in two sections: Entities and Relationships. 

In the Entities Section, use the format `Entity Type, Entity Name, Description, Boundary, Boundary Description, Tag`. For example, `Person, User, User of the payment system, User Boundary, Description of User Boundary, `. 

In the Relationships Section, use the format `Source, Destination, Description, Technology, Tag`. For example, `User, Payment System, Submits payment, HTTPS, ` and `Payment System, Bank, Processes payment, REST API, Future Scope`.

### Contributing and License
Contributions to the project are welcome! Please refer to the contributing guidelines for more details. This project is licensed under the MIT License.

### Acknowledgments
Special thanks to the PlantUML Team and Graphviz Team for their tools that made this project possible.
