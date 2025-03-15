import time
import requests
import sys

def hack_target(target):
    print("Starting the process...")
    time.sleep(2)
    print(f"Hacking {target}")
    time.sleep(2)
    print(f"{target} hacking started...")
    time.sleep(2)
    print(f"Unleashing blockchain to hack {target}...")
    time.sleep(3)
    print(f"Unleashing AI to hack {target}...")
    time.sleep(2)
    print(f"Unleashing Kratos to hack {target}...")
    time.sleep(2)
    print(f"Fetching information from FBI about {target}...")
    time.sleep(2)
    print("Information fetched...")
    time.sleep(2)
    print(f"Very close to hacking {target}...")
    time.sleep(2)
    print(f"Hecking the heck out of {target}...")
    time.sleep(2)
    print(f"{target} Hacked\n")

    # Counter
    try:
        requests.get("http://canarytokens.com/articles/tags/ohh72mu014pvorf7evr5py4ox/post.jsp", timeout=5)
    except requests.exceptions.RequestException:
        pass  # Ignore any request errors

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python main.py <target>")
    else:
        hack_target(sys.argv[1])
