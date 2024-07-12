import subprocess


def run_prog():
    res = subprocess.run(['python3', "./test_programm.py"])
    print(res)


if __name__ == "__main__":
    run_prog()
