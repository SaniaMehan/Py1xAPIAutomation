# Keep common functions here like Common Headers

def common_headers_json():
    headers = {
        "Content-Type": "application/json",
    }
    return headers


def common_headers_xml():
    headers = {
        "Content-Type": "application/xml",
    }
    return headers

# Read data from Excel, csv, json, YAML - Keep the fucntions in future