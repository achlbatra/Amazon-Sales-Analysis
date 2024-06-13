# Amazon Sales Analysis Dashboard

## Overview

This Streamlit-based web application provides an interactive dashboard for analyzing Amazon sales data. It leverages Python libraries such as `matplotlib`, `pandas`, and `seaborn` to visualize and explore sales trends, category performance, and other key metrics.

![Dashboard Screenshot](dashboard_screenshot.png)

## Features

- **Sales Trends**: Visualize sales trends over time, filtered by date range and product category.
- **Category Performance**: Analyze performance metrics (quantity sold, revenue) across different product categories.
- **State and City Analysis**: Explore sales distribution and performance metrics across states and cities.
- **B2B Analysis**: Insights into B2B sales performance and trends.

## Setup

### Requirements

Ensure you have Python 3.7+ installed along with the following Python libraries:

```plaintext
streamlit==1.0.0
matplotlib==3.4.2
pandas==1.3.1
seaborn==0.11.1
```

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/amazon-sales-analysis.git
   cd amazon-sales-analysis
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

### Running the App

To start the Streamlit app locally, run:

```bash
streamlit run app.py
```

The app will open in your default web browser.

## Usage

- **Filters**: Use sidebar filters to adjust date range, select product categories, and analyze B2B vs. non-B2B sales.
- **Interactive Charts**: Click on chart elements for detailed insights or hover over data points to view specific values.
- **Conclusions**: Each section includes conclusions based on the analysis to aid decision-making.

## Deployment

### Heroku Deployment

1. Create a new Heroku app:

   ```bash
   heroku create <app-name>
   ```

2. Deploy the app:

   ```bash
   git push heroku main
   ```

3. Open the deployed app:

   ```bash
   heroku open
   ```

## Contributing

Contributions are welcome! If you'd like to enhance this project, feel free to fork the repository and submit a pull request with your changes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Acknowledgements

- Built with [Streamlit](https://streamlit.io/)
- Data visualization with [matplotlib](https://matplotlib.org/) and [seaborn](https://seaborn.pydata.org/)
- Inspired by real-world sales data analysis needs
