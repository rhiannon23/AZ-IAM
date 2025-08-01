from graph_api import get_users

users = get_users()

for user in users.get("value", []):
    print(user["displayName"], "-", user.get("userPrincipalName"))