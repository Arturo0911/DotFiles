import json

def load_theme():
    # theme = "dark-grey"

    # config = path.join(qtile_path, "config.json")
    # if path.isfile(config):
    #     with open(config) as f:
    #         theme = json.load(f)["theme"]
    # else:
    #     with open(config, "w") as f:
    #         f.write(f'{{"theme": "{theme}"}}\n')


    # theme_file = path.join(qtile_path, "themes", f'{theme}.json')
    # if not path.isfile(theme_file):
    #     raise Exception(f'"{theme_file}" does not exist')

    with open("../config.json", "r") as f:
        return json.load(f)

colors = load_theme()