from sqlalchemy import func
from db import User, Subject
from db import DBSession


# Function to test uniqueness constraint
def test_uniqueness_constraint(session):
    # Creating a new user with a subject that already exists
    user1 = User(username='Brian.M', subject_id=1)
    session.add(user1)
    session.commit()

    # Creating another user with the same subject
    user2 = User(username='Cassie', subject_id=1)
    session.add(user2)
    try:
        session.commit()
    except Exception as e:
        print(f"Error: {str(e)}")

    # Querying the database for duplicate subjects
    duplicate_subjects = session.query(Subject.name). \
        group_by(Subject.name). \
        having(func.count(Subject.name) > 1).all()

    if duplicate_subjects:
        print("Duplicate subjects found:")
        for subject in duplicate_subjects:
            print(subject.name)
    else:
        print("No duplicate subjects found.")

# Usage example
session = DBSession()
test_uniqueness_constraint(session)
session.close()
