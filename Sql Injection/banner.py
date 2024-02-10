import argparse

def banner():
    # ANSI escape codes for color formatting
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RESET = '\033[0m'  # Reset to default color
    
    print(RED + """
 $$$$$$\  $$$$$$\ $$\      $$$$$$\        $$$$$$\  $$$$$$\  $$$$$$\ $$\   $$\$$\   $$\$$$$$$$$\$$$$$$$\  
$$  __$$\$$  __$$\$$ |     \_$$  _|      $$  __$$\$$  __$$\$$  __$$\$$$\  $$ $$$\  $$ $$  _____$$  __$$\ 
$$ /  \__$$ /  $$ $$ |       $$ |        $$ /  \__$$ /  \__$$ /  $$ $$$$\ $$ $$$$\ $$ $$ |     $$ |  $$ |
\$$$$$$\ $$ |  $$ $$ |       $$ |        \$$$$$$\ $$ |     $$$$$$$$ $$ $$\$$ $$ $$\$$ $$$$$\   $$$$$$$  |
 \____$$\$$ |  $$ $$ |       $$ |         \____$$\$$ |     $$  __$$ $$ \$$$$ $$ \$$$$ $$  __|  $$  __$$< 
$$\   $$ $$ $$\$$ $$ |       $$ |        $$\   $$ $$ |  $$\$$ |  $$ $$ |\$$$ $$ |\$$$ $$ |     $$ |  $$ |
\$$$$$$  \$$$$$$ /$$$$$$$$\$$$$$$\       \$$$$$$  \$$$$$$  $$ |  $$ $$ | \$$ $$ | \$$ $$$$$$$$\$$ |  $$ |
 \______/ \___$$$\\________\______|       \______/ \______/\__|  \__\__|  \__\__|  \__\________\__|  \__|
              \___|                                                                                      """ + RESET)
    
    parser = argparse.ArgumentParser(description="Scans SQLi Vulnerability")
    parser.add_argument("-u", "--url", type=str, help="URL to fetch content from", required=True)

    args = parser.parse_args()
    return args.url

if __name__ == "__main__":
    banner()
