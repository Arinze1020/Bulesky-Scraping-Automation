# Bluesky Scraping Automation

This project focuses on developing a scalable and high-performance web scraper to extract large-scale data from the Bluesky social media platform.

## Objectives

1. **Extract User DIDs from the Feed**:
   Fetch the user's feed and extract the Decentralized Identifiers (DIDs) of authors from each post.&#x20;

2. **Profile Mapping and Deduplication**:
    Retrieve detailed profile information for each unique DID, ensuring no duplicates by using a set to filter the feeds.&#x20;

3. **Retrieve Comprehensive Profile Information**:
   For each unique author, extract the following profile details:

   * Full Name (Display Name)
   * DID
   * Handle
   * Profile Image URL
   * Bio (Description)
   * Join Date 

   This is achieved by accessing the respective fields in the profile data returned by the data.&#x20;

4. **Future Enhancements**:
   Plan to develop scripts to gather more extensive data and make sure network connections dosen't break mid way(Proxy rotation and failure/retry handling), in other to enrich the dataset further.



