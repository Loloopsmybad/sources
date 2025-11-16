s = int(input())

# Read stop-words
if s > 0:
    stop_words = set(input().split())
else:
    stop_words = set()
    input()  # Read empty line

# Read hashtags
hashtags_line = input().strip()
if hashtags_line:
    hashtags = hashtags_line.split()
else:
    hashtags = []

# Filter out stop-words and count frequencies
freq = {}
for tag in hashtags:
    if tag not in stop_words:
        freq[tag] = freq.get(tag, 0) + 1

# Sort by hashtag
sorted_freq = dict(sorted(freq.items()))

# Output
print(len(sorted_freq))
if sorted_freq:
    # Format as {key: value, key: value, ...}
    items = [f"{k}: {v}" for k, v in sorted_freq.items()]
    print("{" + ", ".join(items) + "}")
else:
    print("{}")