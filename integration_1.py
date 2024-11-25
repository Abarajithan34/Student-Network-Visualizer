<<<<<<< HEAD
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib import colormaps 

import numpy as np
import random

import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning, message=".*Pyarrow.*")

random.seed(0)
np.random.seed(0)


def calculate_node_size(g, scale=500, extra_size=1500):
    return [(len(str(node)) * scale) + extra_size for node in g.nodes]



#1.Find about a single person
def visualize_single_student_details(student_id, data):
    g=nx.Graph()
    # Filter the data for the student with the given name

    

    student_data = data[data[attributes[0]] == student_id]

    if student_data.empty:
        print(f"No data found for student: {student_id}")
    else:   
            student_row = student_data.iloc[0]
            position = {}


            num=0
            x=0
            y=0
            for i in attributes:
                
                
                g.add_node(i+":\n"+str(student_row[i]))

                position[i+":\n"+str(student_row[i])] =(x,y) # Define custom positions for each node
                x+=10



                if(num>=1):# Add edges between the nodes
                    g.add_edge(attributes[num-1]+":\n"+str(student_row[attributes[num-1]]),i+":\n"+str(student_row[attributes[num]]))
                
                num+=1

            #print(position)
            # Calculate node sizes
            node_sizes = calculate_node_size(g, scale=500)

            nx.draw(g,with_labels="true",node_color="red",node_size=node_sizes,pos=position,font_size=10 )
            plt.margins(0)
            plt.show()



#2.Find about relationship between two people
def visualize_two_student_details(student_id_1,student_id_2,data):
    # Filter the data for the students with the given names
    attributes = data.columns.tolist()

    #data[attributes[0]] = data[attributes[0]].astype(str)
    #data[attributes[1]] = data[attributes[1]].astype(str)


    student_data_1 = data[data[attributes[0]] == student_id_1]
    student_data_2 = data[data[attributes[0]] == student_id_2]

    if student_data_1.empty and student_data_2.empty:
        print(f"No relation between the students id : {student_id_1} and {student_id_2}")
        return  # Early return if no data is found

    else:
        g = nx.Graph()  # Create a new graph for each visualization

        if not student_data_1.empty:
            student_row_1 = student_data_1.iloc[0]  # Pick the first matching record for student 1

        if not student_data_2.empty:
            student_row_2 = student_data_2.iloc[0]  # Pick the first matching record for student 2

        position = {}

        num = 0
        x = 0
        y = 0
        a = 0
        b = 10


        # Create nodes and edges for both students
        for i in attributes:
            g.add_node(i + ":\n" + str(student_row_1[i]))
            g.add_node(i + ":\n" + str(student_row_2[i]))

            

            if num >= 1:  # Add edges between the nodes

                g.add_edge(attributes[num-1] + ":\n" + str(student_row_1[attributes[num-1]]),i + ":\n" + str(student_row_1[attributes[num]]))
                g.add_edge(attributes[num-1] + ":\n" + str(student_row_2[attributes[num-1]]),i + ":\n" + str(student_row_2[attributes[num]]))
                
                

                # Add an edge if the values for both students are the same for a given attribute
                if str(student_row_1[attributes[num]]) == str(student_row_2[attributes[num]]):
                    
                    
                    g.add_edge(i + ":\n" + str(student_row_1[attributes[num]]),i + ":\n" + str(student_row_2[attributes[num]]))
                    b=5
                    position[i + ":\n" + str(student_row_1[i])] = (x, y)
                    position[i + ":\n" + str(student_row_2[i])] = (a, b)
                    b=10
                    x += 500
                    a += 500

                    num += 1
                    continue    


            position[i + ":\n" + str(student_row_1[i])] = (x, y)
            position[i + ":\n" + str(student_row_2[i])] = (a, b)  # Define custom positions for each node

            x += 500
            a += 500

            num += 1
        

        # Calculate node sizes
        node_sizes = calculate_node_size(g, scale=500)
        
        if not nx.__version__.startswith('2'):
            self_loops = [(u, v) for u, v in g.edges() if u == v]
            g.remove_edges_from(self_loops)



        # Draw the graph
        nx.draw(g, with_labels=True, node_color="red", node_size=node_sizes, pos=position, font_size=10)
        #plt.margins(.2)
        plt.show()


#3.Find all the relationship between all the people
def visualize_all_student_details(number_in_category, category, data_known, data):
    # Check the data type of the category column
    if pd.api.types.is_numeric_dtype(data[category]):
        # If the category is numeric, compare the values directly
        student_data = data[data[category] == float(data_known)]
    else:
        # If the category is a string, compare after converting to lowercase
        student_data = data[data[category].str.lower() == data_known.lower()]
    
    num_rows = len(student_data)

    if student_data.empty:
        print(f"No data found for category: {data_known}")
    else:
        position = {}
        g = nx.Graph()
        previous_node = None
        y = 0
        
        #edge_colors = ["red", "blue", "green", "yellow"]

        for i in range(num_rows):
            student_row = student_data.iloc[i]
            x = 0
            y+= 5
            # Create nodes for each attribute of the student row
            for j in range(len(student_row)):
                
                node_label = f"{data.columns[j]}:\n{student_row[j]}"
                g.add_node(node_label)
                position[node_label] = (x, y)

                x += 5

                if previous_node is not None:
                    g.add_edge(previous_node, node_label)
                
                # Update the previous_node to the current node
                previous_node = node_label

        # Calculate node sizes
        node_sizes = calculate_node_size(g, scale=100)

        # Draw the graph
        nx.draw(g, with_labels=True, node_color="red", node_size=node_sizes, pos=position, font_size=8)
        plt.margins(0)
        plt.show()















#csv_file = "student_detail.csv" # Path to your CSV file if you want more data

csv_file = "student_detail_reduced.csv" # Path to your CSV file

data = pd.read_csv(csv_file)

attributes = data.columns.tolist()

what_to_do=int(input("Enter what you want to do\n1.Find about a single person\n2.Find about relationship between two people\n3.Find all the relationship between all the people\nEnter number:"))

if(what_to_do==1): #we use studentid because it is a primary key
    student_id = int(input("Enter the student's Id: "))
    visualize_single_student_details(student_id, data)

elif(what_to_do==2):#we use studentid because it is a primary key

    student_id_1 = int(input("Enter the first student's Id: "))
    student_id_2 = int(input("Enter the second student's Id: "))


    first_name_1,last_name_1="Anthony Smith".split(" ")
    first_name_2, last_name_2="George Short".split(" ")

    # Visualize the student's details as a graph
    visualize_two_student_details(student_id_1,student_id_2,data)

elif(what_to_do==3):
    category_count = 1

    for i in attributes:
        print(f"{category_count}. {i}")
        category_count += 1


    print("")
    category = input("Type the category: ")

    number_in_category = 0
    for i in attributes:
        if category == i:
            break
        else:
            number_in_category += 1

    data_known = input("Enter the known data: ")

=======
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib import colormaps 

import numpy as np
import random

import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning, message=".*Pyarrow.*")

random.seed(0)
np.random.seed(0)


def calculate_node_size(g, scale=500, extra_size=1500):
    return [(len(str(node)) * scale) + extra_size for node in g.nodes]



#1.Find about a single person
def visualize_single_student_details(student_id, data):
    g=nx.Graph()
    # Filter the data for the student with the given name

    

    student_data = data[data[attributes[0]] == student_id]

    if student_data.empty:
        print(f"No data found for student: {student_id}")
    else:   
            student_row = student_data.iloc[0]
            position = {}


            num=0
            x=0
            y=0
            for i in attributes:
                
                
                g.add_node(i+":\n"+str(student_row[i]))

                position[i+":\n"+str(student_row[i])] =(x,y) # Define custom positions for each node
                x+=10



                if(num>=1):# Add edges between the nodes
                    g.add_edge(attributes[num-1]+":\n"+str(student_row[attributes[num-1]]),i+":\n"+str(student_row[attributes[num]]))
                
                num+=1

            #print(position)
            # Calculate node sizes
            node_sizes = calculate_node_size(g, scale=500)

            nx.draw(g,with_labels="true",node_color="red",node_size=node_sizes,pos=position,font_size=10 )
            plt.margins(0)
            plt.show()



#2.Find about relationship between two people
def visualize_two_student_details(student_id_1,student_id_2,data):
    # Filter the data for the students with the given names
    attributes = data.columns.tolist()

    #data[attributes[0]] = data[attributes[0]].astype(str)
    #data[attributes[1]] = data[attributes[1]].astype(str)


    student_data_1 = data[data[attributes[0]] == student_id_1]
    student_data_2 = data[data[attributes[0]] == student_id_2]

    if student_data_1.empty and student_data_2.empty:
        print(f"No relation between the students id : {student_id_1} and {student_id_2}")
        return  # Early return if no data is found

    else:
        g = nx.Graph()  # Create a new graph for each visualization

        if not student_data_1.empty:
            student_row_1 = student_data_1.iloc[0]  # Pick the first matching record for student 1

        if not student_data_2.empty:
            student_row_2 = student_data_2.iloc[0]  # Pick the first matching record for student 2

        position = {}

        num = 0
        x = 0
        y = 0
        a = 0
        b = 10


        # Create nodes and edges for both students
        for i in attributes:
            g.add_node(i + ":\n" + str(student_row_1[i]))
            g.add_node(i + ":\n" + str(student_row_2[i]))

            

            if num >= 1:  # Add edges between the nodes

                g.add_edge(attributes[num-1] + ":\n" + str(student_row_1[attributes[num-1]]),i + ":\n" + str(student_row_1[attributes[num]]))
                g.add_edge(attributes[num-1] + ":\n" + str(student_row_2[attributes[num-1]]),i + ":\n" + str(student_row_2[attributes[num]]))
                
                

                # Add an edge if the values for both students are the same for a given attribute
                if str(student_row_1[attributes[num]]) == str(student_row_2[attributes[num]]):
                    
                    
                    g.add_edge(i + ":\n" + str(student_row_1[attributes[num]]),i + ":\n" + str(student_row_2[attributes[num]]))
                    b=5
                    position[i + ":\n" + str(student_row_1[i])] = (x, y)
                    position[i + ":\n" + str(student_row_2[i])] = (a, b)
                    b=10
                    x += 500
                    a += 500

                    num += 1
                    continue    


            position[i + ":\n" + str(student_row_1[i])] = (x, y)
            position[i + ":\n" + str(student_row_2[i])] = (a, b)  # Define custom positions for each node

            x += 500
            a += 500

            num += 1
        

        # Calculate node sizes
        node_sizes = calculate_node_size(g, scale=500)
        
        if not nx.__version__.startswith('2'):
            self_loops = [(u, v) for u, v in g.edges() if u == v]
            g.remove_edges_from(self_loops)



        # Draw the graph
        nx.draw(g, with_labels=True, node_color="red", node_size=node_sizes, pos=position, font_size=10)
        #plt.margins(.2)
        plt.show()


#3.Find all the relationship between all the people
def visualize_all_student_details(number_in_category, category, data_known, data):
    # Check the data type of the category column
    if pd.api.types.is_numeric_dtype(data[category]):
        # If the category is numeric, compare the values directly
        student_data = data[data[category] == float(data_known)]
    else:
        # If the category is a string, compare after converting to lowercase
        student_data = data[data[category].str.lower() == data_known.lower()]
    
    num_rows = len(student_data)

    if student_data.empty:
        print(f"No data found for category: {data_known}")
    else:
        position = {}
        g = nx.Graph()
        previous_node = None
        y = 0
        
        #edge_colors = ["red", "blue", "green", "yellow"]

        for i in range(num_rows):
            student_row = student_data.iloc[i]
            x = 0
            y+= 5
            # Create nodes for each attribute of the student row
            for j in range(len(student_row)):
                
                node_label = f"{data.columns[j]}:\n{student_row[j]}"
                g.add_node(node_label)
                position[node_label] = (x, y)

                x += 5

                if previous_node is not None:
                    g.add_edge(previous_node, node_label)
                
                # Update the previous_node to the current node
                previous_node = node_label

        # Calculate node sizes
        node_sizes = calculate_node_size(g, scale=100)

        # Draw the graph
        nx.draw(g, with_labels=True, node_color="red", node_size=node_sizes, pos=position, font_size=8)
        plt.margins(0)
        plt.show()















#csv_file = "student_detail.csv" # Path to your CSV file if you want more data

csv_file = "student_detail_reduced.csv" # Path to your CSV file

data = pd.read_csv(csv_file)

attributes = data.columns.tolist()

what_to_do=int(input("Enter what you want to do\n1.Find about a single person\n2.Find about relationship between two people\n3.Find all the relationship between all the people\nEnter number:"))

if(what_to_do==1): #we use studentid because it is a primary key
    student_id = int(input("Enter the student's Id: "))
    visualize_single_student_details(student_id, data)

elif(what_to_do==2):#we use studentid because it is a primary key

    student_id_1 = int(input("Enter the first student's Id: "))
    student_id_2 = int(input("Enter the second student's Id: "))


    first_name_1,last_name_1="Anthony Smith".split(" ")
    first_name_2, last_name_2="George Short".split(" ")

    # Visualize the student's details as a graph
    visualize_two_student_details(student_id_1,student_id_2,data)

elif(what_to_do==3):
    category_count = 1

    for i in attributes:
        print(f"{category_count}. {i}")
        category_count += 1


    print("")
    category = input("Type the category: ")

    number_in_category = 0
    for i in attributes:
        if category == i:
            break
        else:
            number_in_category += 1

    data_known = input("Enter the known data: ")

>>>>>>> fab2e4a275a604eb7c1e8b526cd9820bcf14c460
    visualize_all_student_details(number_in_category, category, data_known, data)