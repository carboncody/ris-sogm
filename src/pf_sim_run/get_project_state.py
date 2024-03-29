import csv

def get_project_state(app):
    # Get existing busbars
    existing_busbars = app.GetCalcRelevantObjects("*.ElmTerm")
    existing_busbar_names = [busbar.GetNodeName() for busbar in existing_busbars]
    
    # Get existing lines
    existing_lines = app.GetCalcRelevantObjects("*.ElmLne")
    
    filtered_types = ['koereledning','uic60']

    existing_lines_fullname = []
    for line in existing_lines:
        type = str(line.GetType()).lower()
        # Check if any element in filtered_types is a substring in type
        if any(ftype in type for ftype in filtered_types):
            existing_lines_fullname.append(line.GetFullName())

    existing_line_names = []
    for fullname in existing_lines:
        existing_line_names.append(fullname.loc_name)
    
    # with open('utils/existing_lines.csv', mode='w', newline='', encoding='utf-8') as file:
    #     writer = csv.writer(file)
    #     writer.writerows([[item] for item in existing_line_names])

    return [existing_busbars, existing_lines, existing_line_names]
