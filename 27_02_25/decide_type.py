def decide(item: str) -> str:
    """Return an appropriate SQLite type based on keywords in column_name."""
    
    lower_name = item.lower()

    if 'price' in lower_name:
        return "REAL"
    elif 'cost' in lower_name:
        return "REAL"
    elif 'profit' in lower_name:
        return "REAL"
    elif 'id' in lower_name:
        return "INTEGER"
    else:
        return 'TEXT'