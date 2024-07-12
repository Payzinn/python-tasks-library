from subprocess import Popen
import subprocess

with Popen('sleep 10', stdout=subprocess.PIPE) as process:
    print(process.stdout.read())
print('Return code: {}'.format(process.returncode))