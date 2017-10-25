#Recursive function string permutation

def permute(s):
    out = []

    # Base Case
    if len(s) == 1:
        out = [s]

    else:
        # For every letter in string
        for i, let in enumerate(s):
            for perm in permute(s[:i] + s[i+1:]):
                # Add it to output
                out += [let + perm]
    return out

print(permute('abc'))
