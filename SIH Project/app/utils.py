def format_name(name:str) -> str:
    if not isinstance(name,str):
        return name
    return name.strip().capitalize()