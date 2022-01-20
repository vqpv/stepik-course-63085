def domain_name(url:str) -> str:
    url = url.replace("http://", "")
    url = url.replace("https://", "")
    url = url.replace("www.", "")
    return url.split(".")[0]
