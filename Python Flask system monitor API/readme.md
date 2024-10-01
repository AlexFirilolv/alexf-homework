How to run:

1. Recommendation: first create a virtual enviornment and activate it.

    Install the python requirements from the requirements.txt via -
    pip install -r requirements.txt

2. After installing the requirements, run the main.py file in the terminal to initizalize the Flask server.
    you can access the Api's docs in the browser: http://localhost:5000/apidocs

3. After verifying that Flask is running, open another terminal, and run the Streamlit frameworks web GUI via:
    streamlit run .\streamlit_app.py
    Your browser should open the streamlit server on http://localhost:8501, and showcase a synopsis of your systems usage.

