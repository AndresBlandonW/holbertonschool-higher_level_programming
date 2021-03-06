#!/usr/bin/python3
"""changes the name of a State object from the database"""

if __name__ == "__main__":
    import sys
    from model_state import Base, State
    from sqlalchemy.orm import sessionmaker
    from sqlalchemy import (create_engine)

    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost/{}'.format
            (sys.argv[1], sys.argv[2], sys.argv[3]),
            pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    sql = session.query(State).filter(State.id == 2).all()
    sql[0].name = "New Mexico"
    session.commit()
