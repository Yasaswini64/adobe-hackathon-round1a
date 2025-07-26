# Adobe India Hackathon – Round 1A

## 🚀 Challenge: Connecting the Dots – Understand Your Document

### 📌 Objective

Extract a structured outline from a PDF including:

- Title
- Headings with levels: H1, H2, H3
- Page numbers

Output format:

```json
{
  "title": "Document Title",
  "outline": [
    { "level": "H1", "text": "Section Name", "page": 1 },
    { "level": "H2", "text": "Subsection", "page": 2 }
  ]
}
```

---

## 🛠️ Approach

We used **PyMuPDF (fitz)** to process the document. The key steps were:

- Extract all text spans along with their font sizes using `page.get_text("dict")`.
- Determine heading levels (H1, H2, H3) by identifying the most frequently used larger font sizes.
- Classify text spans into headings based on font size ranks.
- Filter out short or non-heading lines.
- Assign the first detected H1 as the document title.
- Output the structured data in a JSON format as required.

This approach works without relying on fixed font size values, making it robust for different PDFs.

---

## 📦 Tech Stack

- Python 3.10
- PyMuPDF (fitz)

---

## 🐳 Docker Build Instructions

### 📁 Folder Structure

```
.
├── Dockerfile
├── main.py
├── requirements.txt
├── README.md
├── input/         # PDF input folder
└── output/        # JSON output folder
```

### 🔧 Build the Image

```bash
docker build --platform linux/amd64 -t adobe_solution:local .
```

### ▶️ Run the Container

**For Linux/macOS:**

```bash
docker run --rm \
-v "$(pwd)/input:/app/input" \
-v "$(pwd)/output:/app/output" \
--network none \
adobe_solution:local
```

**For Windows PowerShell:**

```powershell
docker run --rm `
-v "${PWD}\input:/app/input" `
-v "${PWD}\output:/app/output" `
--network none `
adobe_solution:local
```

---

## 🔒 Offline Compliance

- ✅ Works fully offline (no API calls or web access)
- ✅ CPU-only (no GPU required)
- ✅ No external ML models used
- ✅ Runs within 10 seconds for 50-page PDFs
- ✅ Docker image size < 200MB

---

## 📄 Sample Output

```json
{
  "title": "Connecting the Dots",
  "outline": [
    { "level": "H1", "text": "Round 1A: Understand Your Document", "page": 3 },
    { "level": "H2", "text": "Your Mission", "page": 3 },
    { "level": "H2", "text": "Why This Matters", "page": 3 }
  ]
}
```

---

## 👨‍💻 Author

- **Yasaswini Chundru**
- Adobe Hackathon Participant – Round 1A (2025)
