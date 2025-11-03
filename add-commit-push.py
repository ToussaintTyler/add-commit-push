import subprocess
print ("Starting add-commit-push")
print ("git status")
subprocess.run(["git", "status"])

print ("git add -A")
subprocess.run(["git", "add", "-A"])

print ("git commit -m")
subprocess.run(["git", "commit", "-m", "\"update files\""])

print ("git push")
subprocess.run(["git", "push"])
