def markdown_to_blocks(markdown):
    split_strings = markdown.split("\n\n")
    strip_strings = []
    for line in split_strings:
        line_stripped = line.strip()
        if line_stripped != "":
            strip_strings.append(line_stripped)
    return strip_strings