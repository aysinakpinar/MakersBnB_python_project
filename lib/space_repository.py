from lib.space import Space

class SpaceRepository:
    def __init__(self, connection):
        self.connection = connection
        
    def add_space(self, space):
        self.connection.execute("INSERT INTO spaces\
                                (space_name, space_address, space_description, space_price, space_lister_id, space_active)\
                                VALUES(%s, %s, %s, %s, %s, %s)", [space.name, space.address, space.description, space.price, space.lister_id, space.active])

    def get_spaces_for_id(self, user_id):
        rows = self.connection.execute('SELECT * FROM spaces WHERE space_lister_id=%s', [user_id])
        spaces = []
        for row in rows:
            space = Space(row['space_id'], row['space_name'], row['space_address'], row['space_description'], row['space_price'], row['space_lister_id'], row['space_active'], row['space_created_at'], row['space_updated_at'], )
            spaces.append(space)
        return spaces
    
    def get_spaces_by_status(self, space_status):
        rows = self.connection.execute('SELECT * FROM spaces WHERE space_active=%s', [space_status])
        spaces = []
        for row in rows:
            space = Space(row['space_id'], row['space_name'], row['space_address'], row['space_description'], row['space_price'], row['space_lister_id'], row['space_active'], row['space_created_at'], row['space_updated_at'], )
            spaces.append(space)
        return spaces
    
    def get_spaces_by_id_and_status(self, user_id, space_status):
        rows = self.connection.execute('SELECT * FROM spaces WHERE space_lister_id=%s AND space_active=%s', [user_id, space_status])
        spaces = []
        for row in rows:
            space = Space(row['space_id'], row['space_name'], row['space_address'], row['space_description'], row['space_price'], row['space_lister_id'], row['space_active'], row['space_created_at'], row['space_updated_at'], )
            spaces.append(space)
        return spaces