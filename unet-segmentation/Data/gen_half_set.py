with open('train-set.txt', 'r') as f:
    with open('train-set-half.txt', 'a') as t:
        lines = f.readlines()
        for i, line in enumerate(lines):
            if i%2==0:
                t.write(line)

with open('val-set.txt', 'r') as f2:
    with open('val-set-half.txt', 'a') as t2:
        lines = f2.readlines()
        for i, line in enumerate(lines):
            if i%2==0:
                t2.write(line)