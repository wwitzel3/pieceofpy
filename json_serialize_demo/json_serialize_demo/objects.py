from decimal import Decimal
from datetime import datetime

class CustomObject(object):
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.timestamp = datetime.utcnow()

    def __json__(self, request):
        return dict(
            name=self.name,
            email=self.email,
            timestamp=self.timestamp.isoformat(),
            )


class ThirdPartyObject(object):
    def __init__(self):
        self.value = Decimal(0.1)

def third_party_adapter(obj, request):
    return dict(
        value=str(obj.value),
        )
