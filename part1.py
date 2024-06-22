reviews = [
        "This product is really good. I'm impressed with its quality.",
        "The performance of this product is excellent. Highly recommended!",
        "I had a bad experience with this product. It didn't meet my expectations.",
        "Poor quality product. Wouldn't recommend it to anyone.",
        "The product was average. Nothing extraordinary about it."
    ]
keywords = ["good", "excellent", "bad", "poor", "average"]

def keyword_highlighter():
   for review in reviews:
        words = review.split()
        highlighted_words = []
        for word in words:
            chosen_word = word.strip(".,!?\"'").lower()
            if chosen_word in keywords:
                highlighted_words.append(chosen_word.upper())
            else:
                highlighted_words.append(word)
        highlighted_word_final = " ".join(highlighted_words)
        print(highlighted_word_final)

keyword_highlighter()

def sentiment_tally(review):
    positive_words = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing"]
    negative_words = ["bad", "poor", "terrible", "horrible", "awful", "disappointing", "subpar"]

    num_positive_words = 0
    num_negative_words = 0

    words = review.lower().split()

    for word in words:
        if word in positive_words:
            num_positive_words += 1
        elif word in negative_words:
            num_negative_words += 1
    
    return num_positive_words, num_negative_words
    

for idx, review in enumerate(reviews):
    num_positive_words, num_negative_words = sentiment_tally(review)
    print(f"Review {idx + 1}:")
    print(f"Positive words: {num_positive_words}")
    print(f"Negative words: {num_negative_words}")
    print()

def  review_summary(review):
    if len(review)<= 30:
        return review
    else:
        last_space_index = review[:30].rfind(" ")
        if last_space_index == -1:
            return review[:30] + "..."
        else:
            return review[:last_space_index] + "..."

for idx, review in enumerate(reviews):
    summary = review_summary(review)
    print(f"Review {idx + 1} summary: {summary}")