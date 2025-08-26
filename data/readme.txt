# Raw and processed data


├── **data/**                       # Raw and processed data
│   ├── **raw/**                    # Unprocessed data (PDFs, docs, scraped HTML)
│   │   ├── government_portals/
│   │   ├── books_manuals/
│   │   ├── social_media/
│   │   └── crowdsourced/
│   │
│   ├── **processed/**              # Cleaned and structured data
│   │   ├── **corpora/**            # Training data for chatbot
│   │   │   ├── hindi_farming.yml
│   │   │   ├── tamil_farming.yml
│   │   │   └── ...
│   │   ├── **faqs/**               # FAQs in CSV/JSON
│   │   │   ├── hindi_faq.csv
│   │   │   └── ...
│   │   └── **translations/**       # Translated datasets
│   │
│   └── **scripts/**                # Scripts for data processing
│       ├── scrape_kisan_call_center.py
│       ├── extract_pdf.py
│       ├── clean_data.py
│       └── translate_faq.py

