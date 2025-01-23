from lib.space_repository import SpaceRepository
from lib.space import Space
from datetime import datetime

def test_return_all_spaces_for_specific_user_id(db_connection):
    db_connection.seed("seeds/makers_bnb_seed.sql")
    repository = SpaceRepository(db_connection)
    spaces = repository.get_spaces_for_id(1)
    retrieved_space = spaces[0]
    assert retrieved_space.id == 1
    assert retrieved_space.name == 'Downtown Loft'
    assert retrieved_space.address == '123 Main St, Manchester, Greater Manchester, United Kingdom'
    assert retrieved_space.description == 'A stylish 2-bedroom loft in the heart of downtown.'
    assert retrieved_space.price == 2500
    assert retrieved_space.lister_id == 1
    assert retrieved_space.active == 'Available'
    assert isinstance(retrieved_space.created_at, datetime)
    assert isinstance(retrieved_space.updated_at, datetime)

def test_add_new_space(db_connection):
    db_connection.seed("seeds/makers_bnb_seed.sql")
    repository = SpaceRepository(db_connection)
    repository.add_space(Space(None, "new_name", "new_address", "new_description", 200, 1, "Unavailable", None, None))
    spaces = repository.get_spaces_for_id(1)
    retrieved_space = spaces[4]
    assert retrieved_space.id == 9
    assert retrieved_space.name == 'new_name'
    assert retrieved_space.address == 'new_address'
    assert retrieved_space.description == 'new_description'
    assert retrieved_space.price == 200
    assert retrieved_space.lister_id == 1
    assert retrieved_space.active == 'Unavailable'
    assert isinstance(retrieved_space.created_at, datetime)
    assert isinstance(retrieved_space.updated_at, datetime)

def test_return_spaces_by_status(db_connection):
    db_connection.seed("seeds/makers_bnb_seed.sql")
    repository = SpaceRepository(db_connection)
    spaces = repository.get_spaces_by_status("Available")
    if spaces:
        if isinstance(spaces[0].created_at, datetime) and isinstance(spaces[0].updated_at, datetime):
            spaces[0].created_at = None
            spaces[0].updated_at = None
        if isinstance(spaces[1].created_at, datetime) and isinstance(spaces[1].updated_at, datetime):
            spaces[1].created_at = None
            spaces[1].updated_at = None

    assert spaces == [
        Space(1, 'Downtown Loft', '123 Main St, Manchester, Greater Manchester, United Kingdom', 'A stylish 2-bedroom loft in the heart of downtown.', 2500.00, 1, 'Available', None, None),
        Space(4, 'City Penthouse', '101 Skyline Blvd, London, Greater London, United Kingdom', 'A modern penthouse with panoramic city views and top-tier amenities.', 5000.00, 4, 'Available', None, None)
        ]

def test_return_spaces_by_status_and_id(db_connection):
    db_connection.seed("seeds/makers_bnb_seed.sql")
    repository = SpaceRepository(db_connection)
    spaces = repository.get_spaces_by_id_and_status(3, "Requested")
    if spaces:
        if isinstance(spaces[0].created_at, datetime) and isinstance(spaces[0].updated_at, datetime):
            spaces[0].created_at = None
            spaces[0].updated_at = None
    assert 1 ==2
    assert spaces == [
        Space(3,'Mountain Retreat', '789 Alpine Rd, Snowdonia, Gwynedd, Wales, United Kingdom', 'A cozy cabin retreat perfect for a weekend getaway.', 1500.00, 3, 'Requested', None, None),
        ]
        
    
