def generate_id(todos):
    if len(todos) == 0:
        return 1

    return max([todo["id"] for todo in todos]) + 1
