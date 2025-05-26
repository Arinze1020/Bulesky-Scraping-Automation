from atproto import Client
import os

from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Retrieve credentials
email = os.getenv('BLUESKY_EMAIL')
password = os.getenv('BLUESKY_PASSWORD')

client = Client()
client.login(email, password)

data = client.get_timeline(cursor='', limit=30)
feed = data.feed
next_page = data.cursor

# Extract unique DIDs from the feed
author_dids = {item.post.author.did for item in feed}

# Fetch profiles for the unique DIDs
profiles_response = client.app.bsky.actor.get_profiles({'actors': list(author_dids)})
profiles = profiles_response.profiles

# Display detailed profile information for each author
for profile in profiles:
    full_name = profile.display_name or profile.handle
    did = profile.did
    handle = profile.handle
    profile_image = profile.avatar or "No image available"
    bio = profile.description or "No bio available"
    join_date = profile.created_at or "No join date available"

    print(f"Full Name: {full_name}")
    print(f"DID: {did}")
    print(f"Handle: {handle}")
    print(f"Profile Image: {profile_image}")
    print(f"Bio: {bio}")
    print(f"Join Date: {join_date}")
    print("-" * 40)

