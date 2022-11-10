import dataiku
import pandas as pd

# create an API client
client = dataiku.api_client()

# get a reference to the current project
project = client.get_default_project()

# the variable we want to work with
variable_name = 'the-variable'

# retrieve a project's variables
p_vars = project.get_variables()

# retrieving the value or a default
variable_value = 'default-value'
if variable_name in p_vars['standard']:
    variable_value = p_vars['standard'][variable_name]
    
print(f'variable value: {variable_value}')

# update the variable value
p_vars['standard'][variable_name] = 'new_value'

# committing it to the project
project.set_variables(p_vars)