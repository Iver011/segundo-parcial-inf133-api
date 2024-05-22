from database import db

class Tarea(db.Model):
    __tablename__ = "tareas"

    id=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(50), nullable=False)
    description=db.Column(db.String(50), nullable=False)
    status=db.Column(db.String(50), nullable=False)
    created_at=db.Column(db.String(50), nullable=False)
    assigned_to=db.Column(db.String(50), nullable=False)


    def __init__(self, title, description, status, created_at, assigned_to):
        self.title=title
        self.description=description
        self.status=status
        self.created_at=created_at
        self.assigned_to=assigned_to

    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_all():
        return Tarea.query.all()
    
    @staticmethod
    def get_by_id(id):
        return Tarea.query.get(id)
    
    def update(self, title=None,description=None,  status=None, created_at=None, assigned_to=None):
        if title is not None:
            self.title=title
        if status is not None:
            self.status=status
        if description is not None:
            self.description=description
        if created_at is not None:
            self.create_at=created_at
        if assigned_to is not None:
            self.assigned_to=assigned_to
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()