# Student-Network-Visualizer

# Student Relationship Visualization

This project is designed to visualize relationships among students using their details stored in a CSV file. It utilizes Python libraries such as Pandas, NetworkX, and Matplotlib to create graphical representations of student data and relationships.

## Features

1. **Single Student Details**: Visualize detailed information for a single student.
2. **Relationship Visualization**: Compare details between two students and visualize their relationships based on shared attributes.
3. **Group Relationship Visualization**: Display relationships among all students in a specific category.

## Requirements

- Python 3.x
- Libraries:
  - `pandas`
  - `networkx`
  - `matplotlib`
  
You can install the required libraries using pip:

pip install pandas networkx matplotlib


1. Data Preparation
Make sure you have a CSV file named student_detail_reduced.csv in the same directory as the script. This file should contain the student details you want to visualize. The first column should represent unique student identifiers.

2. Running the Script
Clone the repository:

bash
Copy code
git clone https://github.com/yourusername/student-relationship-visualization.git
cd student-relationship-visualization
Run the script:

bash
Copy code
python your_script_name.py
Follow the on-screen prompts to choose the type of visualization you want to perform:

1: Find details about a single student.
2: Find the relationship between two students.
3: Find relationships among all students in a specified category.
3. Interacting with the Script
After running the script, you will be prompted to enter:

For single student details: Enter the student's ID.
For relationship visualization: Enter the IDs of the two students.
For group visualization: Select a category from the available attributes and provide known data for that category.
Example Usage
To find details about a single student, choose option 1 and input the student ID when prompted.

To find relationships between two students, choose option 2 and provide the IDs of both students.

To visualize all relationships within a category, choose option 3, select a category, and input the known data.

Visualization
The script generates visual graphs representing student details and relationships. The nodes represent student attributes, and edges indicate relationships or shared attributes between students.


```bash
pip install pandas networkx matplotlib
