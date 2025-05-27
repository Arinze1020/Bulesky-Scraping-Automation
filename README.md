# Bluesky Scraping Automation

This project is focused on building a scalable and high-performance web scraper to extract large-scale data from the Bluesky social media platform.

## Objectives

1. **Extract User DIDs from Feed**
   Fetch user feeds and extract Decentralized Identifiers (DIDs) of post authors.

2. **Profile Mapping with Deduplication**
   Retrieve detailed profile information for each unique DID. Deduplication is handled using a `set` to ensure each profile is processed only once.

3. **Collect Comprehensive Profile Data**
   For each unique user, extract the following information:

   * Display Name (Full Name)
   * DID
   * Handle
   * Profile Image URL
   * Bio (Description)
   * Join Date

   This data is accessed through the profile fields returned in the API response.

4. **Planned Enhancements**

   * Expand data collection scripts to cover broader areas of user activity


5. **Complete Follower/Following Graph Scraper**
   Current scripts collect DIDs from user feeds and extract profile data for each. The next step is to recursively scrape followers of each DID, collecting all possible interactions (posts, likes, reposts, etc.).
   To scale this effectively:

   * Use multiple accounts in parallel
   * Implement de-duplication mechanisms for DIDs
   * Prioritize the DID as the central identifier to map the entire user graph robustly without redundancy


