card_num = input("Input the number of cards:\n")
term_def = {}
def_term = {}
for i in range(int(card_num)):
    term = input(f"The term for card #{i + 1}:\n")
    while term_def.get(term) is not None:
        term = input(f'The term "{term}" already exists. Try again:\n')
    definition = input(f"The definition for card #{i + 1}:\n")
    while def_term.get(definition) is not None:
        definition = input(f'The definition "{definition}" already exists. Try again:\n')
    term_def[term] = definition
    def_term[definition] = term
for term in term_def:
    answer = input(f'Print the definition of "{term}"\n')
    if answer == term_def[term]:
        print("Correct!")
    elif def_term.get(answer) is not None:
        print(f'Wrong. The right answer is "{term_def[term]}", but your definition is correct for "{def_term[answer]}".')
    else:
        print(f'Wrong. The right answer is "{term_def[term]}".')
