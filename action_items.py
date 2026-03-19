def extract_actions(text):
    keywords = ["will", "should", "need to", "assigned"]
    sentences = text.split(".")
    actions = []
    for sentence in sentences:
        for word in keywords:
            if word in sentence.lower():
                actions.append(sentence.strip())

    return actions
