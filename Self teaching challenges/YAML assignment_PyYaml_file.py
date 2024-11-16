# This python file linked to the YAML assignment file
import yaml

# Load the YAML file
with open('C:\\Users\\Owner\\Documents\\GitHub\\AI Course final assignments\\YAML assignment.yaml', 'r') as file:
    data = yaml.safe_load(file)

# Display the output
print("Data loaded using PyYAML:")
print(data)
