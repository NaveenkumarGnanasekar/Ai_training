n = int(input("enter number of posts: "))
posts = []
for i in range(n):
    hashtags = set(input(f"enter hashtags for post {i+1} (space-separated): ").split())
    posts.append(hashtags)
all_unique = set()
for p in posts:
    all_unique |= p
common = posts[0].copy()
for p in posts[1:]:
    common &= p
print("all unique hashtags:", all_unique)
print("hashtags used in every post:", common)