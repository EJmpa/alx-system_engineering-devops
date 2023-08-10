#!/usr/bin/python3
"""
Module to recursively query the Reddit API and retrieve titles
of all hot articles for a subreddit.
"""

import requests


def recurse(subreddit, hot_list=[]):
    """
    Recursively queries the Reddit API and retrieves
    titles of all hot articles for a subreddit.

    Args:
        subreddit (str): The name of the subreddit.
        hot_list (list): List to store the titles of hot articles.

    Returns:
        list: List containing the titles of hot articles.
        Returns None if subreddit is invalid or no results are found.
    """
    if not subreddit:
        return None

    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=100"
    headers = {"User-Agent": "MySubredditHotArticleFetcher/1.0"}

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        posts = data["data"]["children"]

        if posts:
            for post in posts:
                title = post["data"]["title"]
                hot_list.append(title)

            after = data["data"]["after"]

            if after is not None:
                return recurse(subreddit, hot_list)
            else:
                return hot_list
        else:
            return None
    else:
        return None
