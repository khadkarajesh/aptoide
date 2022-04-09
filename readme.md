# aptoide
Aptoide is web application built in flask to crawl information from [aptoide](https://en.aptoide.com/) about android application using beautifulsoup

## Run Application
### Install Dependencies
1. Create a virtual environment with python3
   ```shell
   python3 -m venv venv
   ```
2. Activate the virtual environment:
   ```shell
   cd venv
   source /bin/activate
   ```
3. Install dependencies
   ```shell
   pip install -r requirements.txt
   ```
   
### Prepare Environment Variable
Create `.env` file from `.env_example`

### Run Flask App
```shell
python app.py
```

## Run Tests

```shell
cd aptoide
pytest
```
