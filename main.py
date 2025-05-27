import os
from atproto import Client, exceptions
from dotenv import load_dotenv

def load_credentials():
    load_dotenv()
    email = os.getenv('BLUESKY_EMAIL')
    password = os.getenv('BLUESKY_PASSWORD')
    if not email or not password:
        raise ValueError("Missing credentials in check .env")
    return email, password

def fetch_timeline_feed(client, limit=1):
    try:
        return client.get_timeline(limit=limit).feed
    except exceptions.AtProtocolError as e:
        print(f"Error fetching feed: {e}")
        return []

def extract_unique_author_dids(feed):
    return list({item.post.author.did for item in feed})

def fetch_profiles(client, dids):
    try:
        return client.app.bsky.actor.get_profiles({'actors': dids}).profiles
    except exceptions.AtProtocolError as e:
        print(f"Error fetching profiles: {e}")
        return []

def fetch_followers_dids(client, actor_did, limit=100):
    followers_dids = []
    cursor = None
    while True:
        try:
            params = {'actor': actor_did, 'limit': limit}
            if cursor:
                params['cursor'] = cursor
            response = client.app.bsky.graph.get_followers(params)
            followers_dids.extend([f.did for f in response.followers])
            if not (cursor := response.cursor):
                break
        except exceptions.AtProtocolError as e:
            print(f"Error getting followers for {actor_did}: {e}")
            break
    return followers_dids

def display_profile_info(profile, followers_dids):
    full_name = profile.display_name or profile.handle
    print(f"\nAuthor: {full_name}")
    print(f"DID: {profile.did}")
    print(f"Handle: {profile.handle}")
    print(f"Profile Image: {profile.avatar or 'No image available'}")
    print(f"Bio: {profile.description or 'No bio available'}")
    print(f"Join Date: {profile.created_at or 'No join date available'}")
    print(f"Followers Count: {profile.followers_count or 0}")
    print(f"Following Count: {profile.follows_count or 0}")
    print(f"Followers DIDs: {followers_dids}")

def process_followers_profiles(client, followers_dids):
    profiles = fetch_profiles(client, followers_dids)
    for profile in profiles:
        nested_followers_dids = fetch_followers_dids(client, profile.did)
        display_profile_info(profile, nested_followers_dids)

def main():
    email, password = load_credentials()
    client = Client()
    client.login(email, password)

    feed = fetch_timeline_feed(client)
    author_dids = extract_unique_author_dids(feed)
    profiles = fetch_profiles(client, author_dids)

    for profile in profiles:
        followers_dids = fetch_followers_dids(client, profile.did)
        print(f"\n=== Profile: {profile.handle} ===")
        display_profile_info(profile, followers_dids)

        # Process each follower's profile
        process_followers_profiles(client, followers_dids)

if __name__ == "__main__":
    main()
