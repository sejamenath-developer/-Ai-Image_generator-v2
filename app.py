import subprocess

# Change directory to /content
subprocess.run("cd /content", shell=True)

# Clone the repository
subprocess.run("git clone https://github.com/lllyasviel/Fooocus.git", shell=True)

# Change directory to /content/Fooocus
subprocess.run("cd /content/Fooocus", shell=True)

# Execute the command and capture output to output.html
subprocess.run("python entry_with_update.py --share > output.html", shell=True)
