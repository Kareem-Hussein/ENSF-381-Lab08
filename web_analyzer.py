import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import re

url = "https://en.wikipedia.org/wiki/University_of_Calgary"

try:
    response = requests.get(url)
    response.raise_for_status() # Ensures the request was successful
    soup = BeautifulSoup(response.text, 'html.parser')
    print(f"Successfully fetched content from {url}")
    headings = len(soup.find_all(["h1", "h2", "h3", "h4", "h5", "h6"]))
    links = len(soup.find_all('a'))
    paragraphs = len(soup.find_all('p'))
    print(f"Number of headings: {headings}")
    print(f"Number of links: {links}")
    print(f"Number of paragraphs: {paragraphs}")
    word = input(f"Please enter a keyword: ").strip().lower()
    page_text = soup.get_text().lower()
    count = page_text.count(word)
    print(f"There are {count} instances of the keyword {word}")

    # Step 5: 5 Word Frequency Analysis
    text = soup.get_text().lower()
    
    words = re.findall(r'\b[a-z0-9]+\b', text)  # Split by word boundaries, keep only alphanumeric characters

    # Filter out very short words (like 'a', 'an', 'the', etc.)
    filtered_words = [word for word in words if len(word) > 2]

    # Count word frequencies
    word_counts = {}
    for word in filtered_words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1

    # Get top 5 most frequent words
    frequent_words = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)[:5]

    print("\nMost Frequent Words:")
    for word, count in frequent_words:
        print(f"{word}: {count}")

    # Step 6: Longest Paragraph
    paragraph_text = [p.get_text().strip() for p in soup.find_all('p')]  # Added () to strip
    valid_paragraphs = [p for p in paragraph_text if len(p.split()) >= 5]

    if valid_paragraphs:
        longest_para = max(valid_paragraphs, key=lambda p: len(p.split()))
        word_count = len(longest_para.split())
        print("\nLongest Paragraph:")
        print(longest_para)
        print(f"\nWord Count: {word_count}")
    else:
        print("\nNo suitable paragraphs found.")
        

    # Step 7: Data Visualization
    labels = ['Headings', 'Links', 'Paragraphs']
    values = [headings, links, paragraphs]
    plt.bar(labels, values)
    plt.title('Group 25')
    plt.ylabel('Count')
    plt.show()

except Exception as e:
    print(f"Error fetching content: {e}")



