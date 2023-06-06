import dataiku

client = dataiku.api_client()
projects = client.list_projects()

print('Recipes in append mode:')
for project in projects:
    p_name = project["projectKey"]
    proj = client.get_project(p_name)
    recipes = proj.list_recipes()
    for recipe in recipes:
        r = proj.get_recipe(recipe['name'])
        outputs = r.get_definition_and_payload().get_recipe_outputs()
        for o in outputs:
            for item in outputs[o]['items']:
                if item['appendMode'] == True:
                    print(f'- {p_name} / {recipe["name"]}')