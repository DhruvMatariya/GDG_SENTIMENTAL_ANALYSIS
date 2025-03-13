```markdown
# Reddit Sentiment Analysis Project

This project fetches Reddit posts, analyzes their sentiment using a pre-trained LSTM model, and displays the results in a web interface.

## Prerequisites

Before you begin, make sure you have the following:

*   **Python:** Python 3.7 or higher installed on your system.
*   **Anaconda or Miniconda:** A package and environment management system. You can download it from [https://www.anaconda.com/products/distribution](https://www.anaconda.com/products/distribution) or [https://docs.conda.io/en/latest/miniconda.html](https://docs.conda.io/en/latest/miniconda.html).
*   **Reddit API Credentials:** A Reddit app created with the necessary API credentials (client ID, client secret, username, password, user agent). See [https://www.reddit.com/prefs/apps](https://www.reddit.com/prefs/apps).

## Installation

Follow these steps to set up and run the project:

1.  **Clone the Repository:**

    Clone this GitHub repository to your local machine:

    ```bash
    git clone <repository_url>
    cd <repository_name>
    ```

    Replace `<repository_url>` with the URL of your GitHub repository and `<repository_name>` with the name of the cloned directory.

2.  **Create a Conda Environment:**

    Create a new Conda environment with Python 3.9:

    ```bash
    conda create -n tf python=3.9
    ```

3.  **Activate the Conda Environment:**

    Activate the newly created environment:

    ```bash
    conda activate tf
    ```

    Your terminal prompt should now show `(tf)` to indicate that the environment is active.

4.  **Install Dependencies:**

    Install the required Python packages using `pip`:

    ```bash
    pip install -r requirements.txt
    ```

    This will install all the packages listed in the `requirements.txt` file, including TensorFlow, praw, pandas, etc.

5.  **Configure Reddit API Credentials:**(NOTE: For now you can use my config file and skip step 5 )

    Create a `config.ini` file in your project directory with the following structure:

    ```ini
    [reddit]
    client_id = YOUR_REDDIT_CLIENT_ID
    client_secret = YOUR_REDDIT_CLIENT_SECRET
    username = YOUR_REDDIT_USERNAME
    password = YOUR_REDDIT_PASSWORD
    user_agent = SentimentAnalysisApp (by /u/YourRedditUsername)
    ```

    Replace `YOUR_REDDIT_CLIENT_ID`, `YOUR_REDDIT_CLIENT_SECRET`, `YOUR_REDDIT_USERNAME`, `YOUR_REDDIT_PASSWORD`, and `YourRedditUsername` with your actual Reddit API credentials.

    **Important:** Do not share your API keys or commit the `config.ini` file to public repositories.

6.  **Download NLTK Data:**

    Run the following Python code to download the necessary NLTK data:

    ```python
    import nltk
    nltk.download('stopwords')
    nltk.download('punkt')
    ```

    You can add these lines to the beginning of your `reddit_sentiment.py` script or run them in a separate Python interpreter.

## Running the Project

1.  **Run the Reddit Sentiment Analysis Script:**

    In the same terminal window (with the `tf` environment activated), run the `reddit_sentiment.py` script:

    ```bash
    python reddit_sentiment.py
    ```

    This will start fetching Reddit posts and analyzing their sentiment.

2.  **Run the Flask Web Application:**

    Open a *new* terminal window (leave the `reddit_sentiment.py` script running in the first terminal). Activate the `tf` environment in the new terminal:

    ```bash
    conda activate tf
    ```

    Then, run the Flask web application:

    ```bash
    python app.py
    ```

    This will start the Flask web server. You should see a message like "Running on http://127.0.0.1:5000/".

3.  **Access the Web Application:**

    Open your web browser and go to the address shown in the terminal (usually `http://127.0.0.1:5000/`). You should now see the Reddit sentiment analysis results displayed in your browser.

## Project Structure

The project directory has the following structure:

```
Project Directory/
├── config.ini
├── reddit_sentiment.py
├── app.py
├── index.html
├── sentiment_model.h5
├── tokenizer.pickle
├── requirements.txt
└── README.md
```

*   `config.ini`: Contains your Reddit API credentials.
*   `reddit_sentiment.py`: Fetches Reddit posts, analyzes their sentiment, and stores the results.
*   `app.py`: The Flask web application that displays the sentiment analysis results.
*   `index.html`: The HTML template for the web application.
*   `sentiment_model.h5`: The pre-trained LSTM model for sentiment analysis.
*   `tokenizer.pickle`: The tokenizer used to preprocess the text data.
*   `requirements.txt`: A list of Python packages required to run the project.
*   `README.md`: This file.

## Troubleshooting

*   **ModuleNotFoundError:** If you get this error, it means you haven't installed the necessary libraries. Double-check that your virtual environment is activated and that you've run `pip install -r requirements.txt`.
*   **praw Errors:** If you get errors related to `praw`, verify that your Reddit API credentials in `config.ini` are correct and that you've created a Reddit app correctly.
*   **Connection Errors:** If you can't connect to the Reddit API, check your internet connection and make sure your Reddit Developer account is in good standing.
*   **"This TensorFlow binary is optimized..." message:** This is not an error. It's an informational message from TensorFlow. You can ignore it.

## License

This project is licensed under the [License Name] License - see the `LICENSE.md` file for details.

## Acknowledgments

*   This project uses the Python Reddit API Wrapper (PRAW).
*   The sentiment analysis model is based on LSTM networks implemented with TensorFlow and Keras.

**Key Points:**

*   **Replace Placeholders:** Make sure to replace the placeholder values (e.g., `<repository_url>`, `YOUR_REDDIT_CLIENT_ID`, `[License Name]`) with your actual values.
*   **Include All Necessary Files:** Ensure that all the necessary files (especially `sentiment_model.h5` and `tokenizer.pickle`) are included in your repository.
*   **Clear Instructions:** Provide clear, step-by-step instructions for installation and running the project.
*   **Troubleshooting Section:** Include a troubleshooting section to address common issues that users might encounter.
*   **Folder Structure:** Make sure that the folder structure you display in the file also matches the folder structure of the files in the repository.
