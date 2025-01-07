import json


def load_data(file_path):
    """ Loads a JSON file """
    with open(file_path, "r") as handle:
        return json.load(handle)

def read_animals_html(file_path):
    """This function load the animals_template.html file"""
    with open(file_path, "r") as handle:
        return handle.read()

def serialize_animal(animal_obj):
    """ This function handle a single animal serialization"""
    # define an empty string
    output = ""
    animal_type = animal_obj["characteristics"].get("type")
    animal_color = animal_obj["characteristics"].get("color")
    # append information to each string
    output += "<li class='cards__item'>\n\t"
    output += f"<div class='card__title'>{animal_obj['name']}</div>\n\t"
    output += "<p class='card__text'>\n\t\t"
    output += "<ul>\n\t\t\t"
    output += (f"<li><strong>Scientific Name:</strong> {animal_obj['taxonomy']['scientific_name']}"
               f"</li>\n\t\t\t")
    output += f"<li><strong>Diet:</strong> {animal_obj['characteristics']['diet']}</li>\n\t\t\t"
    output += f"<li><strong>Location:</strong> {animal_obj["locations"][0]}</li>\n\t\t\t"
    if animal_color is not None:
        output += f"<li><strong>Color:</strong> {animal_color}</li>\n\t\t\t"
    if animal_type is not None:
        output += f"<li><strong>Type:</strong> {animal_type}</li>\n\t\t"
    output += "</ul>\n\t"
    output += "</p>\n"
    output += "</li>\n"
    return output

def write_new_content(file_path, content):
    """ This function write the content to a new file"""
    with open(file_path, "w") as f:
        f.write(content)

def main():
    animals_data = load_data("animals_data.json")
    html_content = read_animals_html("animals_template.html")
    output = ""
    # Serialization of a single animal object to a different function.
    for animal in animals_data:
        output += serialize_animal(animal)
    new_html_content = html_content.replace("__REPLACE_ANIMALS_INFO__", output)
    write_new_content("animals.html", new_html_content)


if __name__ == "__main__":
    main()