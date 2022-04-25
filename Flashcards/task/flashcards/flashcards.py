class FlashCard:
    def __init__(self):
        self.term_def = {}
        self.def_term = {}

    def add_card(self):
        term = input(f'The card:\n')
        while self.term_def.get(term) is not None:
            term = input(f'The card "{term}" already exists. Try again:\n')
        definition = input(f'The definition of the card:\n')
        while self.def_term.get(definition) is not None:
            definition = input(f'The definition "{definition}" already exists. Try again:\n')
        self.term_def[term] = definition
        self.def_term[definition] = term
        print(f'The pair ("{term}":"{definition}") has been added.')

    def remove_card(self):
        term = input('Which card?\n')
        if self.term_def.get(term) is not None:
            del self.term_def[term]
            print('The card has been removed.')
        else:
            print(f'Can\'t remove "{term}": there is no such card.')

    def export_cards(self):
        file_name = input('File name:')
        with open(file_name, 'w') as card_file:
            n = 0
            for term in self.term_def:
                n += 1
                card_file.write(f'{term}:{self.term_def[term]}\n')
        print(f'{n} cards have been saved.')

    def import_cards(self):
        file_name = input('File name:')
        try:
            with open(file_name, 'r') as card_file:
                cards = card_file.readlines()
            for card in cards:
                term, definition = card.strip('\n').split(':')
                self.term_def[term] = definition
            print(f'{len(cards)} cards have been loaded.')
        except FileNotFoundError:
            print('File not found.')

    def ask(self):
        card_num = input('How many times to ask?\n')
        n = 1
        while n <= int(card_num):
            for term in self.term_def:
                if n > int(card_num):
                    break
                n += 1
                answer = input(f'Print the definition of "{term}":\n')
                if answer == self.term_def[term]:
                    print("Correct!")
                elif self.def_term.get(answer) is not None:
                    print(f'Wrong. The right answer is "{self.term_def[term]}", but your definition is correct for "{self.def_term[answer]}".')
                else:
                    print(f'Wrong. The right answer is "{self.term_def[term]}".')

    def menu(self):
        action = input('Input the action (add, remove, import, export, ask, exit):\n')
        while action != 'exit':
            if action == 'add':
                self.add_card()
            if action == 'remove':
                self.remove_card()
            if action == 'import':
                self.import_cards()
            if action == 'export':
                self.export_cards()
            if action == 'ask':
                self.ask()
            action = input('Input the action (add, remove, import, export, ask, exit):\n')
        print('bye bye')


flash_card = FlashCard()
flash_card.menu()
