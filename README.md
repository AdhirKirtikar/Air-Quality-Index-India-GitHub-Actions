# Air-Quality-Index-India-GitHub-Actions
## Repo for 2021 GitHub Actions Hackathon on DEV
### GitHub Action "[run-python.yml](https://github.com/AdhirKirtikar/Air-Quality-Index-India-GitHub-Actions/blob/master/.github/workflows/run-python.yml)"
- Google credentials are stored in GitHub Actions Environment Secrets.
- data.gov.in API Key is also stored in GitHub Actions Environment Secrets.
- A GitHub Action is created that can run manually or on a schedule [12PM UTC (8PM SGT)]
- Python 3.9 is setup using [actions/setup-python@v2.3.0](https://github.com/actions/setup-python) and the pip packages are cached
- Dependencies are installed using [py-actions/py-dependency-install@v2](https://github.com/marketplace/actions/python-dependency-installation)  based on requirements.txt (google auth, pygsheets & pandas).
- The Environment Secrets are exported to environment variables.
- Finally, the Python script is run with the environment variables passed as parameters.
### Python script "[Air Quality Index India.py](https://github.com/AdhirKirtikar/Air-Quality-Index-India-GitHub-Actions/blob/master/Air%20Quality%20Index%20India.py)"
- The script connects to data.gov.in API using API Key passed as a parameter.
- Then it pulls the latest AQI data for India and stores in pandas dataframe.
- The data is cleaned, formatted and the columns are renamed. Nulls are replaced by 0.
- Google sheet is authenticated and connected using pygsheets.
- The pandas dataframe is then saved to a Google doc.
### Tableau Public Dashboard "[Air Quality - Pollutant Index - India](https://public.tableau.com/views/AirQuality-PollutantIndex-India/PollutantIndexDashboard?:language=en-US&:display_count=n&:origin=viz_share_link)"
- The Google doc is used as a source for Tableau Public dashboard.
- The data is refreshed automatically from the Google doc once a day in the dashboard.
