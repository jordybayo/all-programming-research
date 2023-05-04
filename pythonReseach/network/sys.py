import sys

sys.stderr.write('this is stderr text\n')
sys.stderr.flush()
sys.stdout.write('this is a stdout text\n')

print(sys.argv)