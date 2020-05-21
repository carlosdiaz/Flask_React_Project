import sqlalchemy
from app.models.samples import SampleInformation
from flask_restful import Resource
from sqlalchemy.orm import class_mapper


class ModelHelper:

    def attribute_names(self, cls):
        """
        This method will allow to iterate over any model so we don't have to pass every single field
        :param cls:
        :return:
        """
        return [field.key for field in class_mapper(cls).iterate_properties
                if isinstance(field, sqlalchemy.orm.ColumnProperty)]


class SamplesEndPoint(Resource, ModelHelper):
    """
    This class will implement the CRUD operations for the backend

    """

    def get(self):

        list_response = list()
        query_samples = SampleInformation.query.all()

        # we retrieve all the fields from the model
        model_props = self.attribute_names(SampleInformation)

        for s in query_samples:
            temp_value = dict()
            for prop in model_props:
                temp_value[prop] = s.__getattribute__(prop)
            list_response.append(temp_value)

        return list_response

