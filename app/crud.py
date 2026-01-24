# простое временное хранилище
grants_db = []

def get_grants():
    return grants_db

def create_grant(grant):
    grants_db.append(grant.dict())
    return grant.dict()
