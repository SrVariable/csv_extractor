import sys

def get_valid_csv_filename(csv_filename):
    extension = csv_filename.split(".")[-1]
    if extension != "csv":
        return ""

    return (csv_filename)


def extract_field_values(file, field_name):
    line = file.readline()
    found = False
    field_values = []
    column_number = 0
    while line:
        fields = line.split(",")
        if not found:
            for field in fields:
                if field.lower().strip() == field_name:
                    found = True
                    break
                column_number += 1
        else:
            if fields[column_number] != "":
                field_values.append(fields[column_number].strip())
        line = file.readline()
    file.seek(0, 0)

    return field_values


def assert_length(fields):
    expected_length = 0
    for value in fields.values():
        if expected_length == 0:
            expected_length = len(value)
        if (len(value) != expected_length):
            print(f"Expected {expected_length} values, got {len(value)}")
            sys.exit(1)


def get_fields(csv_filename, names):
    fields = {}
    with open(csv_filename, "r") as file:
        for name in names:
            values = extract_field_values(file, name)
            fields[name] = values
    assert_length(fields)

    return fields


def get_rows(fields):
    rows = []
    n_rows = 0
    for value in fields.values():
        n_rows = len(value)
        break

    for i in range(n_rows):
        row = []
        for value in fields.values():
            row.append(value[i])
        rows.append(row)

    return rows


if __name__ == "__main__":
    program_name = sys.argv[0]
    if len(sys.argv) == 1:
        print(f"Usage: {program_name} [CSV FILE]")
        sys.exit(1)

    csv_filename = get_valid_csv_filename(sys.argv[1])
    #field_names = ["persona", "razón", "pagado", "desde", "hasta"]
    field_names = ["plataforma", "total", "miembros"]
    fields = get_fields(csv_filename, field_names)
    rows = get_rows(fields)

    for row in rows:
        print(row)
