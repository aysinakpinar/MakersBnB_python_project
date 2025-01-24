from lib.space import Space

def test_space_constructs():
    space = Space(id=1, name="new_space", address="new_address", description="new_description", price=2500, lister_id=1, active=True, space_path=None, created_at="2025-01-21 11:46:06", updated_at="2025-01-21 11:56:06")
    assert space.id == 1
    assert space.name == "new_space"
    assert space.address == "new_address"
    assert space.description == "new_description"
    assert space.price == 2500
    assert space.path == None
    assert space.lister_id == 1
    assert space.active == True
    assert space.created_at == "2025-01-21 11:46:06"
    assert space.updated_at == "2025-01-21 11:56:06"
    
def test_space_format():
    space = Space(id=1, name="new_space", address="new_address", description="new_description", price=2500, lister_id=1, active="Available", space_path=None, created_at="2025-01-21 11:46:06", updated_at="2025-01-21 11:56:06")
    assert str(space) == "Space(1, new_space, new_address, new_description, 2500, 1, Available, None, 2025-01-21 11:46:06, 2025-01-21 11:56:06)"

def test_spaces_are_equal():
    space1 = Space(id=1, name="new_space", address="new_address", description="new_description", price=2500, lister_id=1, active="Available", space_path=None, created_at="2025-01-21 11:46:06", updated_at="2025-01-21 11:56:06")
    space2 = Space(id=1, name="new_space", address="new_address", description="new_description", price=2500, lister_id=1, active="Available", space_path=None, created_at="2025-01-21 11:46:06", updated_at="2025-01-21 11:56:06")
    assert space1 == space2


