#!/usr/bin/python3
"""
Module to recursively query the Reddit API and count
occurrences of keywords in hot article titles.
"""

import requests


def count_words(subreddit, word_list, after=None, count_dict=None):
    """
    Recursively queries the Reddit API, parses the titles of all
    hot articles, and prints a sorted count of given keywords.

    Args:
        subreddit (str): The name of the subreddit.
        word_list (list): List of keywords to count.
        after (str): Token for pagination.
        count_dict (dict): Dictionary to store keyword counts.

    Returns:
        None
    """
    if not subreddit:
        return

    if count_dict is None:
        count_dict = {}

    url = (
        f"https://www.reddit.com/r/"
        f"{subreddit}/hot.json?limit=100&after={after}"
    )
    headers = {"User-Agent": "MySubredditKeywordCounter/1.0"}

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        posts = data["data"]["children"]

        if posts:
            for post in posts:
                title = post["data"]["title"].lower()
                for keyword in word_list:
                    keyword_lower = keyword.lower()
                    if keyword_lower in title:
                        count_dict[keyword_lower] = (
                            count_dict.get(keyword_lower, 0) + 1
                        )

            after = data["data"]["after"]

            if after is not None:
                return count_words(subreddit, word_list, after, count_dict)
            else:
                sorted_counts = sorted(count_dict.items(),
                                       key=lambda x: (-x[1], x[0]))
                for keyword, count in sorted_counts:
                    print(f"{keyword}: {count}")
        else:
            return
    else:
        return
