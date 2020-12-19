from random import randint

class Nucleic_acid:
    complementary_bases = {}

    def __init__(self, sequence: str):
        for c in sequence:
            if c not in self.complementary_bases:
                raise ValueError(f"{c} is not a valid base")
        self.seq = sequence

    def __add__(self, other):
        if type(self) == type(other):
            return type(self)(self.seq + other.seq)
        else:
            return NotImplemented

    def __mul__(self, other):
        if not type(self) == type(other):
            return NotImplemented

        new_sequence = ""
        for pair in zip(self.seq, other.seq):
            new_sequence += pair[randint(0, 1)]
        if len(self.seq) > len(other.seq):
            new_sequence += self.seq[len(new_sequence):]
        else:
            new_sequence += other.seq[len(new_sequence):]

        return type(self)(new_sequence)

    def __eq__(self, other):
        if type(self) == type(other):
            return self.seq == other.seq
        else:
            raise ValueError("incomparable types")

    def __getitem__(self, item):
        return self.seq[item]

    def __str__(self):
        return self.seq

    def compl_sequence(self):
        complement = ""
        for c in self.seq:
            complement += self.complementary_bases[c]
        return complement


class Rna(Nucleic_acid):
    complementary_bases = {'A': 'T', 'U': 'A', 'G': 'C', 'C': 'G'}

    def __init__(self, sequence):
        super().__init__(sequence)

    def complement(self):
        return Dna(self.compl_sequence())


class Dna(Nucleic_acid):
    complementary_bases = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}

    def __init__(self, sequence):
        super().__init__(sequence)

    def __getitem__(self, item):
        return [self.seq[item], self.complementary_bases[self.seq[item]]]

    def __str__(self):
        return self.seq + "|" + self.compl_sequence()