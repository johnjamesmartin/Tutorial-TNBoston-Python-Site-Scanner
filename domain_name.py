# Imports

# tld = Top-Level Domain extractor package:

from tld import get_tld


# Get Top-Level Domain from URL:

def get_domain_name(url):
    domain_name = get_tld(url)
    return domain_name


# print(get_domain_name('http://www.thenewboston.com/'))