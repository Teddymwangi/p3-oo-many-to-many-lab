class Author:
    members = []

    def __init__(self, name):
        self.name = name
        self.contracts_list = []
        self.members.append(self)

    def contracts(self):
        return self.contracts_list

    def books(self):
        books_list = []
        for contract in self.contracts_list:
            books_list.append(contract.book)
        return books_list

    def sign_contract(self, book, date, royalties):
        contract = Contract(self, book, date, royalties)
        self.contracts_list.append(contract)
        return contract

    def total_royalties(self):
        total = 0
        for contract in self.contracts_list:
            total += contract.royalties
        return total
