# Imports

import os


# Run command with OS shell:

def get_ip_address(url):
    command = "host " + url
    process = os.popen(command)
    results = str(process.read())

    # Find index of "has address" in string and extract IP address:

    marker = results.find('has address') + 12

    # Get first IP address (sometimes there are multiple IPs for multiple servers):

    return results[marker:].splitlines()[0]


print(get_ip_address('google.com'))