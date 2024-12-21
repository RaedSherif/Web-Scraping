# Web Scraping Project

This project is a Python-based web scraper built using **Scrapy** to extract raw job related data from **wuzzuf.com**. It focuses on extracting details like job titles, experience requirements, and other key data for analysis or display.

---

## Features

- **Paignation**: Effectively navigate and parse through multiple pages.
- **Dynamic Content Handling**: Effectively navigates and extracts data from complex, structured pages.
- **CSS and XPath Selectors**: Targets specific elements within HTML to ensure accurate scraping.
- **Export Formats**: Saves data in JSON or CSV for further analysis.
- **Error Handling**: Detects and skips missing or malformed elements without crashing.
- **Optimized for Scalability**: Designed for scraping multiple pages or sites with minimal modifications.

---

## Installation

### Prerequisites

1. **Python 3.7+**
2. **pip**: Python package installer
3. Install dependencies:

```bash
pip install scrapy
```

---

## Usage

1. **Clone the Repository**:

```bash
git clone https://github.com/yourusername/your-repo.git
cd your-repo
```

2. **Run the Scraper**:

```bash
scrapy crawl job_spider
```

3. **Export Data** (optional):

```bash
scrapy crawl job_spider -o output.json
```

---

## Project Highlights

### Libraries Used

- **Scrapy**: For handling the scraping process.
- **CSS Selectors and XPath**: To target specific elements on the page.
- **JSON/CSV**: For data export.

### Challenges Faced

- Handling **duplicate classes**: Solved using nth-child and sibling/child selectors.
- Working with **JavaScript-rendered content**: Adjusted scraping logic for better compatibility.
- Managing **dynamic content**: Focused on specific, nested elements to ensure data accuracy.

### Comparison of Tools

| Tool          | Strength                                   | Weakness                             |
|---------------|-------------------------------------------|--------------------------------------|
| **Scrapy**    | High performance, asynchronous scraping    | Steep learning curve                |
| **BeautifulSoup** | Easy to use for static pages            | Limited for JavaScript content      |
| **Selenium**  | Handles JavaScript and dynamic pages       | Resource-intensive and slower       |

---

## Example Output

```json
[
  {
    "job_title": "Software Engineer",
    "experience": "4 to 6 years",
    "type": "Full-time",
    "location": "Remote"
  },
  {
    "job_title": "Data Scientist",
    "experience": "2 to 4 years",
    "type": "Part-time",
    "location": "New York"
  }
]
```

---

## Future Plans

- Add **proxy rotation** to handle website bans.
- Integrate **Selenium** for JavaScript-heavy pages.
- Implement **AI/ML** to categorize and analyze scraped job data.

---

## Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## Contact

Created by [Your Name](https://github.com/yourusername). Feel free to reach out for collaboration or questions!
