import subprocess
import os
import sys


def main():
    # Get database location.
    location = "C:\\data\\db"
    if len(sys.argv) == 2:
        location = sys.argv[1]

    # Create database directory.
    if not os.path.exists(location):
        os.makedirs(location)

    # Start server.
    subprocess.Popen(
        ["start", "Avalon MongoDB", "mongod", "--dbpath", location],
        shell=True
    )


if __name__ == "__main__":
    main()
