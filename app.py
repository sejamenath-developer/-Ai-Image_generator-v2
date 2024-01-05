import subprocess

# Install pygit2 version 1.12.2
subprocess.run(["pip", "install", "pygit2==1.12.2"])

# Change directory to /content
subprocess.run(["cd", "/content"], shell=True)

# Clone the repository from GitHub
subprocess.run(["git", "clone", "https://github.com/lllyasviel/Fooocus.git"])

# Change directory to /content/Fooocus
subprocess.run(["cd", "/content/Fooocus"], shell=True)

# Run the Python script entry_with_update.py with the --share flag
subprocess.run(["python", "entry_with_update.py", "--share"])
