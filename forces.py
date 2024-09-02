import requests

def fetch(username):
    # Fetch the rating history of the
    url = f"https://codeforces.com/api/user.rating?handle={username}"
    response = requests.get(url)
    data = response.json()
    
    if data['status'] == 'OK':
        ratings = data['result']
        if ratings:
            # Find the rating with the most recent 'ratingUpdateTimeSeconds'
            latest = ratings[0]
            for rating in ratings:
                if rating['ratingUpdateTimeSeconds'] > latest['ratingUpdateTimeSeconds']:
                    latest = rating
            return latest['newRating']
    return None

name = input("Enter the Codeforces username: ")

# Fetch and display the rating
latest_rating = fetch(name)
if latest_rating is not None:
    print(f"The latest rating for user '{name}' is: {latest_rating}")
else:
    print(f"Could not retrieve rating for user '{name}'.")
