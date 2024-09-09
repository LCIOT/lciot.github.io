AUTHOR = "LCIOT"
SITENAME = "Queen Mary at LCIOT Info Page"
SITESUBTITLE = "Info Page for LCIOT"
TIMEZONE = "Europe/London"
THEME="sidecar"
# can be useful in development, but set to False when you're ready to publish
RELATIVE_URLS = False
REVERSE_CATEGORY_ORDER = True
LOCALE = "C"
DEFAULT_PAGINATION = 4
DEFAULT_DATE = (2012, 12, 21, 14, 1, 1)
LINKS = (
    ("QM Degree Apprenticeships", "https://www.qmul.ac.uk/degreeapprenticeships/"),
    )
SOCIAL =  ()
# global metadata to all the contents
DEFAULT_METADATA = {"yeah": "it is"}

# path-specific metadata
EXTRA_PATH_METADATA = {
    "extra/robots.txt": {"path": "robots.txt"},
    'extra/favicon.ico': {'path': 'favicon.ico'},
}

# static paths will be copied without parsing their contents
STATIC_PATHS = [
    "images",
    "extra",
    ".theme",
]

# there is no other HTML content
READERS = {"html": None}

# code blocks with line numbers
PYGMENTS_RST_OPTIONS = {"linenos": "table"}


