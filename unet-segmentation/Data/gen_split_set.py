with open('train-set.txt', 'r') as f:
    with open('train-set-female.txt', 'a') as t:
        with open('train-set-male.txt', 'a') as t2:
            lines = f.readlines()
            for line in lines:
                if line.endswith('F.nii') or line.endswith('F.nii\n'):
                    t.write(line)
                else:
                    t2.write(line)
with open('val-set.txt', 'r') as f2:
    with open('val-set-female.txt', 'a') as t:
        with open('val-set-male.txt', 'a') as t2:
            lines = f2.readlines()
            for line in lines:
                if line.endswith('F.nii') or line.endswith('F.nii\n'):
                    t.write(line)
                else:
                    t2.write(line)

