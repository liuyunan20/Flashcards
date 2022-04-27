import logging
from io import StringIO


class FlashCard:
    def __init__(self):
        self.term_def = {}
        self.def_term = {}
        self.memory_file = StringIO()

    def add_card(self):
        term = input(f'The card:\n')
        log_str = self.memory_file.read()
        self.memory_file.write(f'The card:\n' + log_str + term + '\n')
        while self.term_def.get(term) is not None:
            term = input(f'The card "{term}" already exists. Try again:\n')
            log_str = self.memory_file.read()
            self.memory_file.write(f'The card "{term}" already exists. Try again:\n' + log_str + term + '\n')
        definition = input(f'The definition of the card:\n')
        log_str = self.memory_file.read()
        self.memory_file.write(f'The definition of the card:\n' + log_str + definition + '\n')
        while self.def_term.get(definition) is not None:
            definition = input(f'The definition "{definition}" already exists. Try again:\n')
            log_str = self.memory_file.read()
            self.memory_file.write(f'The definition "{definition}" already exists. Try again:\n' + log_str + definition + '\n')
        self.term_def[term] = [definition, 0]
        self.def_term[definition] = term
        print(f'The pair ("{term}":"{definition}") has been added.')
        print(f'The pair ("{term}":"{definition}") has been added.\n', file=self.memory_file)
        # print(self.memory_file.getvalue())

    def remove_card(self):
        term = input('Which card?\n')
        log_str = self.memory_file.read()
        self.memory_file.write('Which card?\n' + log_str + term + '\n')
        if self.term_def.get(term) is not None:
            del self.term_def[term]
            print('The card has been removed.')
            print('The card has been removed.\n', file=self.memory_file)
        else:
            print(f'Can\'t remove "{term}": there is no such card.')
            print(f'Can\'t remove "{term}": there is no such card.\n', file=self.memory_file)

    def export_cards(self):
        file_name = input('File name:\n')
        log_str = self.memory_file.read()
        self.memory_file.write('File name:\n' + log_str + file_name + '\n')
        with open(file_name, 'w') as card_file:
            n = 0
            for term in self.term_def:
                n += 1
                card_file.write(f'{term}:{self.term_def[term][0]}:{self.term_def[term][1]}\n')
        print(f'{n} cards have been saved.')
        print(f'{n} cards have been saved.\n', file=self.memory_file)

    def import_cards(self):
        file_name = input('File name:\n')
        log_str = self.memory_file.read()
        self.memory_file.write('File name:\n' + log_str + file_name + '\n')
        try:
            with open(file_name, 'r') as card_file:
                cards = card_file.readlines()
            for card in cards:
                term, definition, wrong_time = card.strip('\n').split(':')
                self.term_def[term] = definition, wrong_time
            print(f'{len(cards)} cards have been loaded.')
            print(f'{len(cards)} cards have been loaded.\n', file=self.memory_file)
        except FileNotFoundError:
            print('File not found.')
            print('File not found.\n', file=self.memory_file)

    def ask(self):
        card_num = input('How many times to ask?\n')
        log_str = self.memory_file.read()
        self.memory_file.write('How many times to ask?\n' + log_str + card_num + '\n')
        n = 1
        while n <= int(card_num):
            for term in self.term_def:
                if n > int(card_num):
                    break
                n += 1
                answer = input(f'Print the definition of "{term}":\n')
                log_str = self.memory_file.read()
                self.memory_file.write(f'Print the definition of "{term}":\n' + log_str + answer + '\n')
                if answer == self.term_def[term][0]:
                    print('Correct!')
                    print('Correct!\n', file=self.memory_file)
                elif self.def_term.get(answer) is not None:
                    self.term_def[term][1] += 1
                    print(f'Wrong. The right answer is "{self.term_def[term][0]}", but your definition is correct for "{self.def_term[answer]}".')
                    print(f'Wrong. The right answer is "{self.term_def[term][0]}", but your definition is correct for "{self.def_term[answer]}".\n', file=self.memory_file)
                else:
                    self.term_def[term][1] += 1
                    print(f'Wrong. The right answer is "{self.term_def[term][0]}".')
                    print(f'Wrong. The right answer is "{self.term_def[term][0]}".\n', file=self.memory_file)

    def hardest_card(self):
        hard = 1
        hardest_cards = []
        for term in self.term_def:
            if int(self.term_def[term][1]) >= hard:
                hardest_cards.append(term)
        if len(hardest_cards) == 0:
            print('There are no cards with errors.')
            print('There are no cards with errors.\n', file=self.memory_file)
        elif len(hardest_cards) == 1:
            print(f'The hardest card is "{hardest_cards[0]}". You have {self.term_def[hardest_cards[0]][1]} errors answering it.')
            print(f'The hardest card is "{hardest_cards[0]}". You have {self.term_def[hardest_cards[0]][1]} errors answering it.\n', file=self.memory_file)
        else:
            hardest_terms = '"' + '", "'.join(hardest_cards) + '"'
            print(f'The hardest card is {hardest_terms}. You have {self.term_def[hardest_cards[0]][1]} errors answering it.')
            print(f'The hardest card is "{hardest_terms}". You have {self.term_def[hardest_cards[0]][1]} errors answering it.\n', file=self.memory_file)

    def reset_stats(self):
        for term in self.term_def:
            self.term_def[term][1] = 0
        print('Card statistics have been reset.')
        print('Card statistics have been reset.\n', file=self.memory_file)

    def log(self):
        file_name = input('File name:\n')
        log_str = self.memory_file.read()
        self.memory_file.write('File name:\n' + log_str + file_name + '\n')
        with open(file_name, "w") as log:
            log.write(self.memory_file.getvalue())
            print('The log has been saved.')
            print('The log has been saved.', file=log)

    def menu(self):
        action = input('Input the action (add, remove, import, export, ask, exit, log, hardest card, reset stats):\n')
        log_str = self.memory_file.read()
        self.memory_file.write('Input the action (add, remove, import, export, ask, exit, log, hardest card, reset stats):\n' + log_str + action + '\n')
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
            if action == 'log':
                self.log()
            if action == 'hardest card':
                self.hardest_card()
            if action == 'reset stats':
                self.reset_stats()
            action = input('Input the action (add, remove, import, export, ask, exit, log, hardest card, reset stats):\n')
            log_str = self.memory_file.read()
            self.memory_file.write('Input the action (add, remove, import, export, ask, exit, log, hardest card, reset stats):\n' + log_str + action + '\n')
        print('bye bye')
        print('bye bye\n', file=self.memory_file)


flash_card = FlashCard()
flash_card.menu()
