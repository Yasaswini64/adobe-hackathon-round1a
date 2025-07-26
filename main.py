import fitz  # PyMuPDF
import os
import json
from collections import Counter

INPUT_DIR = "input"
OUTPUT_DIR = "output"


def extract_outline(pdf_path):
    doc = fitz.open(pdf_path)
    spans = []

    # Collect all spans from all pages
    for page_num in range(len(doc)):
        page = doc[page_num]
        blocks = page.get_text("dict")["blocks"]

        for block in blocks:
            for line in block.get("lines", []):
                for span in line.get("spans", []):
                    if span["text"].strip():
                        spans.append({
                            "text": span["text"].strip(),
                            "size": span["size"],
                            "page": page_num + 1
                        })

    # Determine font size ranks (global)
    size_counts = Counter([round(s["size"]) for s in spans])
    top_sizes = [size for size, _ in size_counts.most_common(3)]

    size_to_level = {}
    if len(top_sizes) >= 1: size_to_level[top_sizes[0]] = "H1"
    if len(top_sizes) >= 2: size_to_level[top_sizes[1]] = "H2"
    if len(top_sizes) >= 3: size_to_level[top_sizes[2]] = "H3"

    # Extract outline entries
    outline = []
    for span in spans:
        size = round(span["size"])
        if size in size_to_level:
            outline.append({
                "level": size_to_level[size],
                "text": span["text"],
                "page": span["page"]
            })

    # First H1 is title
    title = next((item["text"] for item in outline if item["level"] == "H1"), "Untitled Document")

    return {
        "title": title,
        "outline": outline
    }


def main():
    for filename in os.listdir(INPUT_DIR):
        if filename.lower().endswith(".pdf"):
            input_path = os.path.join(INPUT_DIR, filename)
            result = extract_outline(input_path)
            output_filename = os.path.splitext(filename)[0] + ".json"
            output_path = os.path.join(OUTPUT_DIR, output_filename)

            with open(output_path, "w", encoding="utf-8") as f:
                json.dump(result, f, ensure_ascii=False, indent=2)


if __name__ == "__main__":
    main()
