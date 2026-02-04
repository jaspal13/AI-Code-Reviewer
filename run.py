from app.reviewer import generate_review

def main():
    with open("examples/sample_diff.txt") as f:
        diff = f.read()

    review = generate_review(diff)
    print(review.model_dump_json(indent=2))

if __name__ == "__main__":
    main()