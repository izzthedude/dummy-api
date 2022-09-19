# Dummy API

## Description

This project is for creating dummy APIs for development purposes which involve calls to servers/APIs. It acts as a 'test
server' of sorts to ensure that we don't constantly make calls to actual production servers in the wild and annoy them.

I started this project while working on another project (see [Corona Info](https://github.com/izzthedude/corona-info))
which involves web-scraping, and thus constantly makes calls to a server. I haven't actually had any problems with that
yet, but I don't wanna take any chances and potentially get myself blacklisted from the website.

## Using

```bash
# Clone project and enter project
git clone https://github.com/izzthedude/dummy-api.git
cd dummy-api

# Setup Python virtual environment and dependencies
python -m venv venv
source venv/bin/activate
which python; which pip  # OPTIONAL: Verify that you're using the virtual environment
pip install -r requirements.txt

# Running
python main.py
```
