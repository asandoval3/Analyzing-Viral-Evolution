import random

# Defining the genetic sequence space
codons = ['AAA', 'AAT', 'AAC', 'AAG', 'ATA', 'ATT', 'ATC', 'ATG', 
          'ACA', 'ACT', 'ACC', 'ACG', 'AGA', 'AGT', 'AGC', 'AGG', 
          'TAA', 'TAT', 'TAC', 'TAG', 'TTA', 'TTT', 'TTC', 'TTG', 
          'TCA', 'TCT', 'TCC', 'TCG', 'TGA', 'TGT', 'TGC', 'TGG', 
          'CAA', 'CAT', 'CAC', 'CAG', 'CTA', 'CTT', 'CTC', 'CTG', 
          'CCA', 'CCT', 'CCC', 'CCG', 'CGA', 'CGT', 'CGC', 'CGG', 
          'GAA', 'GAT', 'GAC', 'GAG', 'GTA', 'GTT', 'GTC', 'GTG', 
          'GCA', 'GCT', 'GCC', 'GCG', 'GGA', 'GGT', 'GGC', 'GGG']

# Defining the fitness function
def fitness(sequence):
    # Count the number of 'G' nucleotides in the sequence
    return sequence.count('G')

# Generate a random initial sequence
initial_sequence = ''.join(random.choices(codons, k=9))

# Find the highest fitness sequence
best_sequence = initial_sequence
best_fitness = fitness(best_sequence)

# Create the titer table
titer_table = []
for i in range(5):
    row = []
    for j in range(6):
        max_fitness = 0
        for k in range(50):  # 50 mutations for each position
            # Generate a new sequence by randomly mutating a sequence of 3 codons
            new_sequence = list(best_sequence)
            index = random.randint(0, 5)  # Choose the first codon in the sequence to mutate
            new_codons = random.choices(codons, k=3)
            new_sequence[index:index+9] = new_codons
            new_sequence = ''.join(new_sequence)

            # Calculate the fitness of the new sequence
            new_fitness = fitness(new_sequence)

            # If the new sequence has higher fitness than the previous mutations, update the max fitness
            if new_fitness > max_fitness:
                max_fitness = new_fitness

        # Add the max fitness value to the row
        row.append(max_fitness)

    # Add the row to the titer table
    titer_table.append(row)

print("Best sequence:", best_sequence)
print("Best fitness:", best_fitness)

# Print the titer table
for row in titer_table:
    print(row)