# docker-python-template
Template for starting a new python app


### Create image
`docker build -t streamlit-example .`

### Create container
`docker run -dit -p 8501:8501 --name streamlit-example streamlit-example`

### Stop container
`docker container stop streamlit-example-container`

### Start container
`docker container start streamlit-example-container`