class Space:
    def __init__(self, id, name, address, description, price, lister_id, active, space_path, created_at, updated_at):
        self.id = id
        self.name = name
        self.address = address
        self.description = description
        self.price = price
        self.lister_id = lister_id
        self.active = active
        self.path = space_path
        self.created_at = created_at
        self.updated_at = updated_at
    
    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    def __repr__(self):
        return f'Space({self.id}, {self.name}, {self.address}, {self.description}, {self.price}, {self.lister_id}, {self.active}, {self.path}, {self.created_at}, {self.updated_at})'