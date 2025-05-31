import os
msg = input("Enter your commit message: ")
os.system('git add .')
os.system(f'git commit -m "{msg}"')
os.system('git push origin main')