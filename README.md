# Stock Visualizer

Stock Visualizer is a web application built with Flask that allows users to visualize stock data for multiple tickers. Users can select the tickers from a dropdown menu, and the application fetches the data and displays it using Plotly Express.
check practical implementation at [https://stock-visualizer.onrender.com/](https://stock-visualizer.onrender.com/)
## Features

- Select multiple stock tickers from a dropdown.
- Visualize stock price data over the last month.
- Responsive design for both desktop and mobile devices.
- Simple and clean user interface.

## Technologies Used

- Flask
- Plotly Express
- yfinance
- HTML/CSS

## Getting Started

Follow these instructions to get a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

Make sure you have the following installed:

- Python 3.x
- pip (Python package installer)

### Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/ath34-tech/stock-visualizer.git
    ```

2. **Create a virtual environment:**

    ```bash
    python -m venv venv
    ```

3. **Activate the virtual environment:**

    - On Windows:

      ```bash
      venv\Scripts\activate
      ```

    - On macOS and Linux:

      ```bash
      source venv/bin/activate
      ```

4. **Install the dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

### Running the Application

1. **Start the Flask application:**

    ```bash
    flask run
    ```

2. Open your web browser and go to `http://127.0.0.1:5000/` to see the application in action.


## Webapp interface
![stockvis](https://github.com/ath34-tech/stock-visualizer/blob/main/images/stock_vis.png)

![stockvis2](https://github.com/ath34-tech/stock-visualizer/blob/main/images/stock_vis2.png)


## Contributing

Contributions are welcome! Please fork the repository and submit a pull request for any improvements or bug fixes.

