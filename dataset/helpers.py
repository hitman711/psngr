"""
"""
import json
from . import models
from psngr.helpers import validate_image


def load_data_in_db(pd_data):
    if not pd_data.empty:
        response = pd_data.to_json(
            orient="records",
            date_format="epoch",
            double_precision=10,
            force_ascii=True,
            date_unit="ms", default_handler=None)
        response = json.loads(response)
        for x in response:
            if not x['image']:
                continue
            try:
                models.DataSet.objects.get_or_create(
                    image=validate_image(x['image']),
                    description=x['description'],
                    title=x['title']
                )
            except Exception as e:
                raise e
