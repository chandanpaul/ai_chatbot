# Project overview and setup

chatterbot/
│
├── **config/**                     # Configuration files
│   ├── __init__.py
│   ├── settings.py                 # API keys, paths, and global settings
│   └── languages.py                # Supported languages and codes
│
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
│
├── **models/**                     # Chatbot and ML models
│   ├── __init__.py
│   ├── chatbot.py                  # ChatterBot initialization and training
│   ├── translator.py               # Google Translate/other translation logic
│   └── api_integrations.py         # Agmarknet, weather API, etc.
│
├── **utils/**                      # Helper functions
│   ├── __init__.py
│   ├── file_utils.py               # File handling (PDF, DOCX, CSV)
│   ├── text_utils.py               # Text cleaning, spell-checking
│   └── logging_utils.py            # Logging setup
│
├── **app/**                        # Flask/SocketIO application
│   ├── __init__.py
│   ├── routes.py                   # Flask routes
│   ├── socket_events.py            # SocketIO event handlers
│   ├── templates/                  # HTML templates
│   │   └── index.html
│   └── static/                     # CSS, JS, images
│
├── **tests/**                      # Unit and integration tests
│   ├── test_chatbot.py
│   ├── test_scraping.py
│   └── ...
│
├── **logs/**                       # Log files
│   ├── scraping.log
│   ├── chatbot.log
│   └── ...
│
├── **docs/**                       # Documentation
│   ├── data_collection.md          # How data is collected/processed
│   ├── api_integration.md          # API endpoints and usage
│   └── deployment.md               # Deployment instructions
│
├── **requirements.txt**            # Python dependencies
├── **README.md**                   # Project overview and setup
└── **main.py**                     # Entry point for the application
