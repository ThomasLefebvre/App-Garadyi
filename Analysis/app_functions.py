from django.core import serializers



def makeJSONFile(obj):
    # assuming obj is a model instance
    serialized_obj = serializers.serialize('json', [ obj, ])
    print(serialized_obj)
