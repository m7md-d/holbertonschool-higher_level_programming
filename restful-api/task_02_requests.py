#!/usr/bin/env python3
"""
2. Consuming and processing data from an API using Python
"""
import requests
import csv


def fetch_and_print_posts():
    """
    Fetches all post from JSONPlaceholder and prints titles.
    """
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    print(f"Status Code: {response.status_code}")
    if response.status_code == 200:
        posts = response.json()
        for i in posts:
            print(i.get("title"))


def fetch_and_save_posts():
    """
    Fetches all post from JSONPlaceholder and saves them to a CSV file.
    """
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    if response.status_code == 200:
        posts = response.json()

        data = [
            {'id': i['id'], 'title': i['title'], 'body': i['body']}
            for i in posts
        ]
        keys = ['id', 'title', 'body']
        with open("posts.csv", "w") as f:
            w = csv.DictWriter(f, fieldnames=keys)
            w.writeheader()
            w.writerows(data)
