import requests
import pandas as pd

def fetch(username):
    url = f"https://codeforces.com/api/user.rating?handle={username}"
    response = requests.get(url)
    data = response.json()
    
    if data['status'] == 'OK':
        ratings = data['result']
        if ratings:
            latest_rating = ratings[0]
            for rating in ratings:
                if rating['ratingUpdateTimeSeconds'] > latest_rating['ratingUpdateTimeSeconds']:
                    latest_rating = rating
            return latest_rating['newRating']
    return None

def process_usernames(input_csv, output_csv):
    df = pd.read_csv(input_csv)
    
    if 'username' not in df.columns:
        print("Input CSV must contain a 'username' column.")
        return
    
    results = []

    for username in df['username']:
        latest_rating = fetch(username)
        results.append({'username': username, 'latest_rating': latest_rating})
    
    result_df = pd.DataFrame(results)
    result_df = result_df.sort_values(by='latest_rating', ascending=False)
    result_df.to_csv(output_csv, index=False)
    print(f"Results saved to {output_csv}")

input_csv_path = 'names.csv'
output_csv_path = 'ratings.csv'

process_usernames(input_csv_path, output_csv_path)
