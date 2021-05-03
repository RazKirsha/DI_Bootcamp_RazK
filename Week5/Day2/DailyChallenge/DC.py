import random


class Genes:

    def __init__(self):
        self.gene_value = random.choice([True, False])


class Chromosomes:

    def __init__(self):
        self.chromo_value = []

        number_of_genes = random.choices(range(20),
                                         weights=[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 19, 1, 1, 1, 1, 1, 1, 1, 1, 1], k=1)
        for gene in range(number_of_genes[0]):
            created_gene = Genes()
            self.chromo_value.append(created_gene.gene_value)


class DNA:

    def __init__(self):
        self.dna_value = []

        number_of_chromo = random.choices(range(20),
                                          weights=[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 19, 1, 1, 1, 1, 1, 1, 1, 1, 1], k=1)
        for gene in range(number_of_chromo[0]):
            created_chromo = Chromosomes()
            self.dna_value.append(created_chromo.chromo_value)


d = DNA()
print(d.dna_value)


class Organism:
    counter = 0
    d_counter = 0
    keep = True
    while keep:
        d = DNA()
        for dna in d:
            if false


o = Organism
print(o)
