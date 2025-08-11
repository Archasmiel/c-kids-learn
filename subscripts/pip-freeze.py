import subprocess
import os

if __name__ == "__main__":
    print(os.getcwd())

    # Run pip freeze, capture output, split, strip versions
    result = subprocess.run(
        ["./python-win/python.exe", "-m", "pip", "freeze", "--disable-pip-version-check"],
        capture_output=True,
        text=True,
        check=True
    )

    packages = []
    for line in result.stdout.splitlines():
        packages.append(line)

    # Save to requirements.txt
    with open("requirements.txt", "w", encoding="utf-8") as f:
        f.write("\n".join(packages))

    print("requirements.txt created with versions.")
