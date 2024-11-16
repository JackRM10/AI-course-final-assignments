import requests

def fetch_posts():
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    
    if response.status_code == 200:
        posts = response.json()
        return posts
    else:
        print(f"Failed to fetch posts. Status code: {response.status_code}")
        return None

def display_posts(posts, num=5):
    """Display the first 'num' posts."""
    if not posts:
        print("No posts to display.")
        return
    
    for i, post in enumerate(posts[:num], start=1):
        print(f"Post {i}:")
        print(f"Title: {post['title']}")
        print(f"Body: {post['body']}\n")

if __name__ == "__main__":
    posts = fetch_posts()
    display_posts(posts)
