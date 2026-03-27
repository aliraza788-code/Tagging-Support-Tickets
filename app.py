from transformers import pipeline
from labels import labels

# Load zero-shot classifier
classifier = pipeline(
    "zero-shot-classification",
    model="facebook/bart-large-mnli"
)

def classify_ticket(ticket):
    result = classifier(ticket, labels)

    # Top 3 tags
    top_tags = result['labels'][:3]
    scores = result['scores'][:3]

    return list(zip(top_tags, scores))


# ===== REAL-TIME INPUT =====
if __name__ == "__main__":
    print("🎯 Support Ticket Classifier (Zero-Shot)")
    print("Type 'exit' to quit\n")

    while True:
        ticket = input("Enter ticket: ")

        if ticket.lower() == "exit":
            print("Exiting... 👋")
            break

        tags = classify_ticket(ticket)

        print("\nTop 3 Tags:")
        for tag, score in tags:
            print(f"{tag} ({score:.2f})")

        print("-" * 40)