import subprocess
print ("Starting add-commit-push")
print ("git status")
subprocess.run(["git", "status"])

print ("git add -A")
subprocess.run(["git", "add", "-A"])
