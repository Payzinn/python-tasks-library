import subprocess

def run_prog():
    res = subprocess.run(['python3', "./test_programm.py"], input=b'some input\notherinput')
    print(res)

if __name__ == "__main__":
    run_prog()