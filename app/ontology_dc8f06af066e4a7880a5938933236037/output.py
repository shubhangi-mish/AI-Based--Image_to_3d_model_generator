from dataclasses import dataclass
from marshmallow import Schema, fields, post_load

from openfabric_pysdk.fields import Resource
from openfabric_pysdk.utility import SchemaUtil


################################################################
# Output concept class - AUTOGENERATED
################################################################
@dataclass
class OutputClass:
    message: str = None


################################################################
# OutputSchema concept class - AUTOGENERATED
################################################################
class OutputClassSchema(Schema):
    message = fields.Str(allow_none=True)

    @post_load
    def create(self, data, **kwargs):
        return SchemaUtil.create(OutputClass(), data)
