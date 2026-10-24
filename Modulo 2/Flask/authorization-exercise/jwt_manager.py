
from datetime import datetime, timedelta, timezone
from pathlib import Path

import jwt


KEYS_DIRECTORY = Path(__file__).resolve().parent / "keys"

PRIVATE_KEY_PATH = KEYS_DIRECTORY / "private.pem"
PUBLIC_KEY_PATH = KEYS_DIRECTORY / "public.pem"


class JWTManager:
    def __init__(self, access_expiration, refresh_expiration):
        self.access_expiration = access_expiration
        self.refresh_expiration = refresh_expiration

        self.private_key = PRIVATE_KEY_PATH.read_text(encoding="utf-8")
        self.public_key = PUBLIC_KEY_PATH.read_text(encoding="utf-8")

    def encode(self, data, expires_in):
        payload = {
            **data,
            "exp": datetime.now(timezone.utc)
            + timedelta(seconds=expires_in),
        }

        return jwt.encode(
            payload,
            self.private_key,
            algorithm="RS256",
        )

    def decode(self, token):
        try:
            return jwt.decode(
                token,
                self.public_key,
                algorithms=["RS256"],
            )
        except jwt.PyJWTError:
            return None

    def generate_tokens(self, user_id, role="user"):
        access_token = self.encode(
            {"id": user_id, "type": "access", "role": role},
            self.access_expiration,
        )

        refresh_token = self.encode(
            {"id": user_id, "type": "refresh", "role": role},
            self.refresh_expiration,
        )

        return access_token, refresh_token

    def decode_token(self, token, expected_type):
        decoded = self.decode(token)

        if decoded is None or decoded.get("type") != expected_type:
            return None

        return decoded


jwt_manager = JWTManager(
    access_expiration=900,
    refresh_expiration=604800,
)
