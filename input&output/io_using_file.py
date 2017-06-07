peom = '''\
Programming is fun
When the work is done
if you wanna make your work also fun:
    use Python!
'''

# open for 'w'riting
f = open("peom.txt", 'w')
# write text to file
f.write(peom)
# close the file
f.close()

# if no mode is specified,
# 'r'ead mode is assumed by default
f = open('peom.txt')
while True:
    line = f.readline()
    # Zero length indicates EOF
    if len(line) == 0:
        break
    # The 'line' already has new line
    # at the end of each line
    # since it is reading from a file
    print(line, end='')
# close the file
f.close()
