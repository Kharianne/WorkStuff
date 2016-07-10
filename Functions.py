import argparse

def urlParser():
    parser = argparse.ArgumentParser(description="Fill in url")
    parser.add_argument('--url', action = "store", type = str)
    args = parser.parse_args()
    values = vars(args)
    url = (values['url'])
    return url

