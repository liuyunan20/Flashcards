card_num = input("Input the number of cards:\n")
term_def = {}
for i in range(int(card_num)):
    term = input(f"The term for card #{i + 1}:\n")
    definition = input(f"The definition for card #{i + 1}:\n")
    term_def[term] = definition
for term in term_def:
    answer = input(f'Print the definition of "{term}"\n')
    if answer == term_def[term]:
        print("Correct!")
    else:
        print(f'Wrong. The right answer is "{term_def[term]}".')
