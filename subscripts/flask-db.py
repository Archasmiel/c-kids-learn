import subprocess
import sys

# Default commands to run if none given
DEFAULT_COMMANDS = [
    ["flask", "db", "init"],
    ["flask", "db", "migrate", "-m", "Auto migration"],
    ["flask", "db", "upgrade"]
]

if __name__ == "__main__":
    if len(sys.argv) > 1:
        # Run any custom command passed in
        subprocess.run(["flask", "db"] + sys.argv[1:], check=True)
    else:
        # Run default migrate + upgrade sequence
        for cmd in DEFAULT_COMMANDS:
            print(f"Running: {' '.join(cmd)}")
            subprocess.run(cmd, check=False)
