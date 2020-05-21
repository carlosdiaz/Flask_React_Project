from app import db


class SampleInformation(db.Model):

    __tablename__ = 'sample'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, index=True)
    name = db.Column(db.String(100), nullable=True, index=True, unique=False)
    date = db.Column(db.DateTime, nullable=True)
    type = db.Column(db.String(100), nullable=True)
    volume = db.Column(db.String(10), nullable=False)
    volume_unit = db.Column(db.String(5), nullable=True)

    def __init__(self, **kwargs):
        self.sample_field_dict = {'name': '', 'date': None, 'volume': '', 'type': '', 'volume_unit': ''}

        for field, value in self.sample_field_dict.items():
            setattr(self, field, kwargs.get(field))

    def __repr__(self):
        return "<Sample Information %s %s %s %s %s>" % (self.name, self.date, self.type, self.volume, self.volume_unit)
