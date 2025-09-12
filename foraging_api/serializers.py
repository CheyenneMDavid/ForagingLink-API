# File based on the "Moments" walkthrough project by Code Institute.
# This serializer customises what the /dj-rest-auth/user/ endpoint returns.
# Extending dj-rest-auth’s built-in UserDetailsSerializer, it adds two fields
# from the related Profile model and explicitly defines them as read-only,
# while omitting "email", thereby making email writable.

from dj_rest_auth.serializers import UserDetailsSerializer
from rest_framework import serializers


class CurrentUserSerializer(UserDetailsSerializer):
    profile_id = serializers.ReadOnlyField(source="profile.id")
    profile_image = serializers.ReadOnlyField(source="profile.image.url")

    class Meta(UserDetailsSerializer.Meta):
        fields = UserDetailsSerializer.Meta.fields + (
            "profile_id",
            "profile_image",
        )

        # 'email' becomes writable due to its ommittance when redefining the read_only_fields.
        read_only_fields = ("profile_id", "profile_image")
