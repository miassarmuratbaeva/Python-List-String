def format_name(name):
    parts = name.split()
    formatted_name = f"{' '.join(parts[1:])}, {parts[0]}"
    return formatted_name
input_name = "Aliyev Vali Ganiyevich"
output_name = format_name(input_name)
print(output_name)
