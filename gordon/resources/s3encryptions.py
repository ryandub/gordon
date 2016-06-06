from .base import BaseResource


class s3Encryption(BaseResource):

    grn_type = 's3encryption'

    required_settings = (
        'type',
    )
