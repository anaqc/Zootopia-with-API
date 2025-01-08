import data_fetcher


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
    output += f"<div class='card__title'>{animal_obj.get('name')}</div>\n\t"
    output += "<p class='card__text'>\n\t\t"
    output += "<ul>\n\t\t\t"
    output += (f"<li><strong>Scientific Name:</strong> "
               f"{animal_obj['taxonomy'].get('scientific_name')}</li>\n\t\t\t")
    output += f"<li><strong>Diet:</strong> {animal_obj['characteristics'].get('diet')}</li>\n\t\t\t"
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


def animals_data_not_found(name):
    """ This function create a new site if the animal searched doesn't exist"""
    output = ""
    output += "<h2><strong>Error Message:</strong> Oops! Animal Not Found</h2>\n"
    output += "<li class='cards__item'>\n\t"
    output += f"<div class='card__title'> We couldn't find the animal you're looking for</div>\n\t"
    output += "<p class='card__text'>\n\t\t"
    output += "<ul>\n\t\t\t"
    output += "<li>Double - check your spelling.</li>\n\t\t\t"
    output += f"<li>Try searching for another animal.</li>\n\t\t\t"
    output += "</ul>\n\t"
    output += "</p>\n"
    output += "</li>\n"
    return output

def get_animal_name_from_user():
    while True:
        try:
            animal_name = input("Enter a name of an animal: ")
            if animal_name == "" or animal_name.isdigit():
                print("You entered something that is not a animal name")
                continue
            return animal_name
        except Exception as e:
            print("You entered something that is not a animal name", e)
def main():
    new_file_path = "animals.html"
    animal_name = get_animal_name_from_user()
    data = data_fetcher.fetch_data(animal_name)
    html_content = read_animals_html("animals_template.html")
    output = ""
    if len(data) == 0:
        output += animals_data_not_found(animal_name)
        new_html_content = html_content.replace("__REPLACE_ANIMALS_INFO__", output)
    else:
        # Serialization of a single animal object to a different function.
        for animal in data:
            output += serialize_animal(animal)
        new_html_content = html_content.replace("__REPLACE_ANIMALS_INFO__", output)
    write_new_content(new_file_path, new_html_content)
    print(f"Website was successfully generated to the file {new_file_path}")


if __name__ == "__main__":
    main()