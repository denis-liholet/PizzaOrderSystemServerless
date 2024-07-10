from typing import Any

import boto3
from botocore.exceptions import ClientError

from commons.pos_exception import POSNotFoundException
from services import COUNTER_SSM_PARAM_NAME


class SSMService:

    def __init__(self):
        self._client = boto3.client('ssm')

    def get_param(self, param_name: str) -> int:
        try:
            parameter = self._client.get_parameter(Name=param_name)
            return parameter['Parameter']['Value']
        except ClientError as e:
            raise POSNotFoundException(
                f"Parameter with name {param_name} not found")

    def put_param(self, param_name: str, param_value: Any) -> bool:
        try:
            self._client.put_parameter(
                Name=param_name,
                Value=str(param_value),
                Type='String',
                Overwrite=True
            )
        except ClientError as e:
            return False
        return True

    def get_pk_increment(self) -> int:
        try:
            value = self.get_param(COUNTER_SSM_PARAM_NAME)
            inc_value = int(value) + 1
            self.put_param(
                param_name=COUNTER_SSM_PARAM_NAME,
                param_value=inc_value
            )
            return inc_value
        except POSNotFoundException:
            self.put_param(
                param_name=COUNTER_SSM_PARAM_NAME,
                param_value=1
            )
            return 1
