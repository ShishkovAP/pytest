
def stop_codons():
    stop_set = {'UAA', 'UAG', 'UGA'}
    return stop_set


def codon_dictionary():
    codon_dict = {'AUG': 'Methionine',
                  'UUU': 'Phenylalanine',
                  'UUC': 'Phenylalanine',
                  'UUA': 'Leucine',
                  'UUG': 'Leucine',
                  'UCU': 'Serine',
                  'UCC': 'Serine',
                  'UCA': 'Serine',
                  'UCG': 'Serine',
                  'UAU': 'Tyrosine',
                  'UAC': 'Tyrosine',
                  'UGU': 'Cysteine',
                  'UGC': 'Cysteine',
                  'UGG': 'Tryptophan'}
    return codon_dict


def codon_processing(codon):

    codon_translation   = ''
    codon_dict          = codon_dictionary()
    stop_set            = stop_codons()

    if codon in stop_set:
        return ''
    else:
        try:
            codon_translation = codon_dict[codon]
        except KeyError:
            print("Кодона с именем " + codon + " не существует.")
    return codon_translation


def rna_processing(sequence):
    protein_translation = ''

    while sequence != '':
        string_processing = sequence[:3]
        codon_translation = codon_processing(string_processing)

        if codon_translation == '':
            break
        if not protein_translation:
            protein_translation = '"' + codon_translation + '"'
        else:
            protein_translation = protein_translation + ', ' + '"' + codon_translation + '"'

        sequence = sequence[3:]
    print(protein_translation)


if __name__ == '__main__':
    def main():
        RNA_Sequence = input("Введите последовательность РНК: ")
        rna_processing(RNA_Sequence)


 


main()
