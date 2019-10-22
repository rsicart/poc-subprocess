import sys
import subprocess


if __name__ == '__main__':

    proc = subprocess.Popen('python3 ./read_input.py',
            shell=True,
            universal_newlines=True,
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT
           )



    while proc.poll() is None:
        line = proc.stdout.readline()
        print(line)
        if 'Name' in line:
            print('found name in stdout line')
            proc.stdin.write('toto\n')
            proc.stdin.flush()


    """
    try:
        outs, errs = proc.communicate(input="toto", timeout=15)
    except TimeoutExpired:
        proc.kill()
        outs, errs = proc.communicate()

    print(outs)
    """

    sys.exit(0)
