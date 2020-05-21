from flask_restful import Resource, Api
from flask_wtf.csrf import CSRFProtect
from app.resources.sample_resource import SamplesEndPoint
from app import app


csrf = CSRFProtect(app)
api = Api(app, decorators=[csrf.exempt])

api.add_resource(SamplesEndPoint, '/samples/')


@app.route('/')
def landing_page():
    return 'Welcome!'

from app import manager
from app.models.samples import SampleInformation


if __name__ == '__main__':
    # manager.run() # for DB migration
    app.run()
