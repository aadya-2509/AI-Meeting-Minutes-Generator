from transformers import pipeline
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def generate_summary(text):
    summary = summarizer(text, max_length=120, min_length=30, do_sample=False)
    return summary[0]["summary_text"]
def extract_action_items(text):

    keywords = ["will", "should", "must", "need to", "deadline"]

    parts = text.split(",")

    seen = set()
    action_items = []

    for p in parts:
        for k in keywords:
            if k in p.lower():
                cleaned = p.strip()
                if cleaned not in seen:
                    action_items.append(cleaned)
                    seen.add(cleaned)
                break

    return action_items

