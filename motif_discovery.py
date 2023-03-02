


def create_pwm(seqs):
    # Initialize an empty PWM with zeros
    pwm = [[0 for i in range(len(seqs[0]))] for j in range(4)]
    # Count the occurrences of each nucleotide at each position in the sequences
    for i in range(len(seqs[0])):
        for j in range(len(seqs)):
            if seqs[j][i] == 'A':
                pwm[0][i] += 1
            elif seqs[j][i] == 'C':
                pwm[1][i] += 1
            elif seqs[j][i] == 'G':
                pwm[2][i] += 1
            elif seqs[j][i] == 'T':
                pwm[3][i] += 1
    # Convert the counts to probabilities by dividing by the total number of sequences
    for i in range(len(pwm)):
        total = sum(pwm[i])
        for j in range(len(pwm[i])):
            pwm[i][j] /= total
    return pwm




def create_consensus(seqs):
    # Initialize an empty consensus sequence
    consensus = ''
    # Find the most common nucleotide at each position in the sequences
    for i in range(len(seqs[0])):
        counts = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
        for j in range(len(seqs)):
            counts[seqs[j][i]] += 1
        consensus += max(counts, key=counts.get)
    return consensus



create_pwm()