def validate_url(_url):
    if "youtube.com" in _url:
        return True
    else:
        return False


def validate_output_location(_output):
    if _output == "terminal" or _output == "txt" or _output == "csv":
        return True
    else:
        return False