# Book Scraper Project 🕷📚

This project is a Dockerized Scrapy crawler that scrapes data from a book website and stores the results in a CSV file. The CSV can then be converted to JSON for data analysis or training machine learning models. This setup ensures a reproducible, isolated environment perfect for scraping tasks.

---

## 🔧 Tech Stack

- **Python 3**
- **Scrapy 2.12**
- **Docker & Docker Compose**

---

## 📁 Directory Structure

```
book-scraper/
│
├── scraper/               # Scrapy project with spiders
│   └── spiders/
│       └── books_spider.py
│   └── jobs.csv           # Original scraped data (renamed later)
│
├── Dockerfile             # Defines Python/Scrapy image
├── docker-compose.yml     # Defines services
├── requirements.txt       # Python dependencies
└── README.md              # You're here!
```

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/book-scraper.git
cd book-scraper
```

### 2. Build the Docker Image

```bash
docker-compose build
```

### 3. Run the Spider

This command runs the spider and outputs the scraped data to `books.csv`.

```bash
docker-compose run scraper scrapy crawl books -o books.csv
```

---

## 🔄 Convert CSV to JSON

Use this Python script to convert your data:

```python
import csv, json

with open('books.csv', 'r', encoding='utf-8') as infile:
    reader = csv.DictReader(infile)
    rows = list(reader)

with open('books.json', 'w', encoding='utf-8') as outfile:
    json.dump(rows, outfile, indent=4)
```

---

## 📉 Use Case

The resulting dataset in `books.json` can be used to:
- Train ML models (e.g., category prediction, clustering).
- Analyze pricing, reviews, or availability patterns.
- Build recommendation systems.

---

## ⚠️ Challenges Faced & How I Solved Them

### 1. **Docker Compose inside container not found**
- **Issue**: When running `docker-compose` inside the container, it failed with `sh: docker-compose: not found`.
- **Fix**: Realized `docker-compose` should only be run from the host machine, not inside the container shell.

### 2. **CSV File Rename Confusion**
- **Issue**: I had an output file called `jobs.csv` but I wanted to rename it to `books.csv`.
- **Fix**: Renamed it using shell commands and updated spider output filename:  
  `docker-compose run scraper scrapy crawl books -o books.csv`

### 3. **Scrapy "no active project" error**
- **Issue**: Running Scrapy directly without the right working directory or context showed:
  `Scrapy 2.12.0 - no active project`
- **Fix**: Ensured I'm in the correct directory (`/app/scraper` inside the container) and that the spider is properly structured with a `scrapy.cfg` file.

### 4. **Orphan Containers Warning**
- **Issue**: Docker reported multiple orphan containers:
  ```
  Found orphan containers [...]
  ```
- **Fix**: Cleaned them using:
  ```bash
  docker-compose down --remove-orphans
  ```

---

## 🧠 Future Plans

- Add more scraping targets (e.g., price comparison, book summaries).
- Build a dashboard using Streamlit or Dash.
- Train a basic NLP model on book descriptions.

---

## 📜 License

This project is open source and available under the [MIT License](LICENSE).

---

## 🤝 Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you’d like to change.

---

## 📫 Contact

For questions or collaborations: [your.email@example.com](mailto:your.email@example.com)

---

**Happy Scraping!** 🕷💻📖
