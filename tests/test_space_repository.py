from lib.space_repository import SpaceRepository
from lib.space import Space
from datetime import datetime

def test_return_all_spaces_for_specific_user_id(db_connection):
    db_connection.seed("seeds/makers_bnb_seed.sql")
    repository = SpaceRepository(db_connection)
    spaces = repository.get_spaces_for_id(1)
    for space in spaces:
        if isinstance(space.created_at, datetime) and isinstance(space.updated_at, datetime):
            space.created_at = None
            space.updated_at = None
            
    assert spaces == [
        Space(1, 'Downtown Loft', '123 Main St, Manchester, Greater Manchester, United Kingdom', 'A stylish 2-bedroom loft in the heart of downtown.', 450, 1, 'Available', None, None),
        Space(6, 'Urban Studio', '78 High St, Manchester, Greater Manchester, United Kingdom', 'A chic and compact studio apartment in the city center, ideal for young professionals.', 200, 1, 'Available', None, None),
        Space(7, 'Riverside Cottage', '34 River Rd, Oxford, Oxfordshire, United Kingdom', 'A quaint cottage by the river with a peaceful garden and walking trails.', 300, 1, 'Requested', None, None),
        Space(8, 'Country Estate', '543 Greenfield Rd, Surrey, South East England, United Kingdom', 'An expansive 5-bedroom estate with private gardens, a pool, and a tennis court.', 150, 1, 'Available', None, None),
        Space(9, 'Lochside Lodge', '123 Loch Rd, Inverness, Scotland, United Kingdom', 'A serene lodge overlooking a loch, perfect for nature lovers and outdoor enthusiasts.', 200, 1, 'Unavailable', None, None),
        Space(10, 'Downtown Condo', '56 Park Ave, Edinburgh, Scotland, United Kingdom', 'A modern 2-bedroom condominium with great views and close proximity to shops and restaurants.', 300, 1, 'Available', None, None)
    ]


def test_add_new_space(db_connection):
    db_connection.seed("seeds/makers_bnb_seed.sql")
    repository = SpaceRepository(db_connection)
    repository.add_space(Space(None, "new_name", "new_address", "new_description", 200, 1, "Unavailable", None, None))
    spaces = repository.get_spaces_for_id(1)
    retrieved_space = spaces[6]
    assert retrieved_space.id == 11
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
    for space in spaces:
        if isinstance(space.created_at, datetime) and isinstance(space.updated_at, datetime):
            space.created_at = None
            space.updated_at = None

    assert spaces == [
        Space(1, 'Downtown Loft', '123 Main St, Manchester, Greater Manchester, United Kingdom', 'A stylish 2-bedroom loft in the heart of downtown.', 450, 1, 'Available', None, None),
        Space(4, 'City Penthouse', '101 Skyline Blvd, London, Greater London, United Kingdom', 'A modern penthouse with panoramic city views and top-tier amenities.', 900, 4, 'Available', None, None),
        Space(6, 'Urban Studio', '78 High St, Manchester, Greater Manchester, United Kingdom', 'A chic and compact studio apartment in the city center, ideal for young professionals.', 200, 1, 'Available', None, None),
        Space(8, 'Country Estate', '543 Greenfield Rd, Surrey, South East England, United Kingdom', 'An expansive 5-bedroom estate with private gardens, a pool, and a tennis court.', 150, 1, 'Available', None, None),
        Space(10, 'Downtown Condo', '56 Park Ave, Edinburgh, Scotland, United Kingdom', 'A modern 2-bedroom condominium with great views and close proximity to shops and restaurants.', 300, 1, 'Available', None, None)
        ]

def test_return_spaces_by_status_and_id(db_connection):
    db_connection.seed("seeds/makers_bnb_seed.sql")
    repository = SpaceRepository(db_connection)
    spaces = repository.get_spaces_by_id_and_status(3, "Requested")
    if spaces:
        if isinstance(spaces[0].created_at, datetime) and isinstance(spaces[0].updated_at, datetime):
            spaces[0].created_at = None
            spaces[0].updated_at = None
    assert spaces == [
        Space(3, 'Mountain Retreat', '789 Alpine Rd, Snowdonia, Gwynedd, Wales, United Kingdom', 'A cozy cabin retreat perfect for a weekend getaway.', 1000, 3, 'Requested', None, None),
        ]
        
def test_return_all_spaces(db_connection):
    db_connection.seed("seeds/makers_bnb_seed.sql")
    repository = SpaceRepository(db_connection)
    spaces = repository.get_all_spaces()
    for space in spaces:
        if isinstance(space.created_at, datetime) and isinstance(space.updated_at, datetime):
            space.created_at = None
            space.updated_at = None
            
    assert spaces == [
        Space(1, 'Downtown Loft', '123 Main St, Manchester, Greater Manchester, United Kingdom', 'A stylish 2-bedroom loft in the heart of downtown.', 450, 1, 'Available', None, None),
        Space(2, 'Seaside Villa', '456 Ocean Ave, Brighton, East Sussex, United Kingdom', 'A luxurious seaside villa with an infinity pool and ocean views.', 850, 2, 'Unavailable', None, None),
        Space(3, 'Mountain Retreat', '789 Alpine Rd, Snowdonia, Gwynedd, Wales, United Kingdom', 'A cozy cabin retreat perfect for a weekend getaway.', 1000, 3, 'Requested', None, None),
        Space(4, 'City Penthouse', '101 Skyline Blvd, London, Greater London, United Kingdom', 'A modern penthouse with panoramic city views and top-tier amenities.', 900, 4, 'Available', None, None),
        Space(5, 'Suburban House', '202 Maple Dr, Birmingham, West Midlands, United Kingdom', 'A spacious 4-bedroom family home with a large backyard and garage.', 600, 5, 'Unavailable', None, None),
        Space(6, 'Urban Studio', '78 High St, Manchester, Greater Manchester, United Kingdom', 'A chic and compact studio apartment in the city center, ideal for young professionals.', 200, 1, 'Available', None, None),
        Space(7, 'Riverside Cottage', '34 River Rd, Oxford, Oxfordshire, United Kingdom', 'A quaint cottage by the river with a peaceful garden and walking trails.', 300, 1, 'Requested', None, None),
        Space(8, 'Country Estate', '543 Greenfield Rd, Surrey, South East England, United Kingdom', 'An expansive 5-bedroom estate with private gardens, a pool, and a tennis court.', 150, 1, 'Available', None, None),
        Space(9, 'Lochside Lodge', '123 Loch Rd, Inverness, Scotland, United Kingdom', 'A serene lodge overlooking a loch, perfect for nature lovers and outdoor enthusiasts.', 200, 1, 'Unavailable', None, None),
        Space(10, 'Downtown Condo', '56 Park Ave, Edinburgh, Scotland, United Kingdom', 'A modern 2-bedroom condominium with great views and close proximity to shops and restaurants.', 300, 1, 'Available', None, None)
        ]
