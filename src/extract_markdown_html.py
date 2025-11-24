
def extract_title(markdown):
    """
    Extract the H1 title from a markdown string.
    The H1 title is the first line that starts with a single '# '.
    """
    for line in markdown.splitlines():
        line = line.strip()
        if line.startswith("# "):
            return line[2:].strip()
        elif line.startswith("#") and not line.startswith("##"):
            # "#Title" (no space) is still allowed
            return line[1:].strip()
        
    raise Exception("No H1 Title found in the markdown.")
