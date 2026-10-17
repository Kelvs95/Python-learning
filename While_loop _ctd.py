# Verifying confirmed users
# Start with a list of users that needs to be verified
# and an empty list for confirmed users

unconfirmed_users = ['mike', 'rose', 'arpitha']
confirmed_users = []

# Verify each user until they are no more unconfirmed users:
# move each verified useer into the list of confirmed users

while unconfirmed_users:
    current_user = unconfirmed_users.pop()

    print(f"Verifying user: {current_user}")
    confirmed_users.append(current_user)
# Display all confirmed users
print("\nThe following users have been confirmed:")
for users in confirmed_users:
    print(users.title())