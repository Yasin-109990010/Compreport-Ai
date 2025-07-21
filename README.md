# Compreport AI

**Compreport AI** is an intelligent reporting tool designed to monitor and analyze industrial, construction, and economic developments across Nigeria and more. It fetches news articles using SerpAPI, categorizes them into relevant sectors, and presents a paginated, searchable, and filterable report for business and policy insight.

---

## 🌍 Features

* Google News fetching via SerpAPI
* Auto-categorization by sector (Construction, Energy, Finance, etc.)
* Responsive HTML report with:

  * Pagination
  * Date and keyword filtering
  * Collapsible summaries and suggestions
  * Category tags with icons
* Lazy-loaded article rendering
* Scroll-to-top and dynamic section toggling

---

## 📁 Project Structure

```
Compreport-AI/
├── main.py                  # Backend: fetches, processes, and generates report
├── templates/
│   └── report_template.html # Jinja2 HTML template for the report
├── static/
│   ├── style.css            # Optional: additional styling
│   ├── rotors.mp4           # Background video for homepage
│   └── articles.json        # JSON data used by frontend JS
├── nigeria.html             # Final generated HTML report
├── .env                     # Your SerpAPI key (SERPAPI_KEY=...)
├── README.md                # This file
└── LICENSE                  # MIT License
```

---

## ⚙️ Setup Instructions

1. Clone the repo
2. Create a `.env` file with your SerpAPI key:

   ```
   SERPAPI_KEY=your_api_key_here
   ```
3. Run the report generator:

   ```bash
   python main.py
   ```
4. Open `nigeria.html` in your browser to view the report.

---

## 🧠 Built With

* Python 3.10+
* Jinja2
* SerpAPI (Google News engine)
* Vanilla JS + HTML + CSS

---

## 📜 License

See `LICENSE` file for full details.

---

## 🙋 Author

**Ahmed Muhammad Yasin**
[MIT Licensed](./LICENSE)
