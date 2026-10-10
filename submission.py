def read_submission(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()
    return content