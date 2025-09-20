def convert_to_snake_case(input_string):
    fields = input_string.split(',')
    snake_case_fields = [field.strip().lower().replace(" ", "_") for field in fields]
    return "_".join(snake_case_fields)
input_string = "Web Development, Mobile Application, Data Science"
output_string = convert_to_snake_case(input_string)
print(output_string)
