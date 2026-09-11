# 💰📊 AI Sales Dashboard

## Turning Sales Data into Clear, Actionable Business Insights

The **AI Sales Dashboard** is an interactive sales analytics application built with **Python and Streamlit** to help business stakeholders quickly understand sales performance across **regions, products, and sales statuses**.

Instead of manually reviewing large spreadsheets or static reports, users can interact with the dashboard, filter relevant business information, visualize sales performance, and receive automatically generated insights to support faster decision-making.

##  Business Problem

Sales teams and business leaders often have large volumes of transaction data but struggle to quickly answer questions such as:

* Which products are generating the most sales?
* How is a specific region performing?
* What is the status of current sales transactions?
* Where are the strongest or weakest areas of performance?
* What insights can be extracted from the data without manually analyzing every row?

This project addresses that challenge by transforming raw sales data into an **interactive decision-support dashboard**.

---

##  Solution

The AI Sales Dashboard provides stakeholders with a simple interface where they can:

✅ Filter sales records by **Region**

✅ Analyze performance by **Product**

✅ Review transactions by **Status**

✅ View detailed filtered sales records

✅ Visualize **Total Sales by Product**

✅ Compare sales performance across transaction statuses

✅ Receive automatically generated **AI-style business insights**

The objective is to make sales information easier to understand and enable stakeholders to move from **data → insight → action**.

---

##  Dashboard Features

###  Region Analysis

Users can select a specific region from the sidebar and instantly view sales records associated with that location.

This allows management to understand geographical sales performance and identify regions that may require additional attention or investment.

---

###  Product Analysis

Users can filter the dataset by product to understand how individual products are performing.

This can help stakeholders identify:

* High-performing products
* Low-performing products
* Product sales patterns
* Areas requiring stronger sales or marketing efforts

---

###  Sales Status Analysis

The dashboard allows users to explore sales transactions based on their current status.

This provides greater visibility into the sales pipeline and helps stakeholders understand the distribution of transactions across different stages.

---

##  Interactive Sales Visualization

The dashboard uses **Plotly** to create an interactive bar chart showing:

> **Total Sales by Product and Status**

This makes it easier for stakeholders to visually compare product performance and identify meaningful sales trends.

---

##  AI-Generated Insights

One of the key features of the project is the **AI Insight section**.

Using a custom `generate_insight()` function, the application analyzes the selected data and provides a simplified business insight.

This demonstrates how analytics applications can go beyond displaying numbers and begin helping decision-makers **interpret what the numbers mean**.

---

##  Technology Stack

| Technology                  | Purpose                                  |
| --------------------------- | ---------------------------------------- |
| **Python**                  | Core programming language                |
| **Pandas**                  | Data loading, filtering and manipulation |
| **Streamlit**               | Interactive web application development  |
| **Plotly Express**          | Interactive data visualization           |
| **Custom Python Functions** | Automated insight generation             |
| **CSV**                     | Sales data source                        |

---

##  Skills Demonstrated            

This project demonstrates practical experience in:

* Data Analytics
* Data Manipulation
* Business Intelligence
* Dashboard Development
* Data Visualization
* Python Programming
* Pandas
* Streamlit
* Plotly
* Business KPI Analysis
* Interactive Data Filtering
* Insight Generation
* Translating business requirements into analytical solutions

---

##  Project Structure

```text
AI-Sales-Dashboard/
│
├── dash.py
│
├── data/
│   └── sales_data.csv
│
├── utils/
│   ├── __init__.py
│   └── insights.py
│
├── requirements.txt
└── README.md
```

### `dash.py`

Contains the main Streamlit application, filters, tables, visualization, and dashboard interface.

### `data/sales_data.csv`

Contains the sales dataset used by the dashboard.

### `utils/insights.py`

Contains the custom `generate_insight()` function responsible for generating analytical insights from the selected data.

---

##  How to Run the Project

### 1. Clone the repository

```bash
git clone <your-repository-url>
```

### 2. Navigate to the project directory

```bash
cd AI-Sales-Dashboard
```

### 3. Install the required libraries

```bash
pip install -r requirements.txt
```

Or install the major dependencies directly:

```bash
pip install streamlit pandas plotly
```

### 4. Run the Streamlit application

```bash
streamlit run dash.py
```

The application will open in your browser.

---

##  Who Can Use This Dashboard?

This solution can be useful for:

* CEOs and Business Owners
* Sales Managers
* Commercial Teams
* Business Analysts
* Data Analysts
* Product Managers
* Operations Managers
* Finance Teams
* Business Intelligence Teams

---

##  Business Value

The dashboard demonstrates how organizations can move away from static spreadsheets toward interactive analytics applications.

With a solution like this, stakeholders can:

* Reduce time spent manually analyzing sales reports
* Gain faster visibility into sales performance
* Identify product and regional trends
* Improve sales monitoring
* Support data-driven decision-making
* Make business data easier for non-technical stakeholders to understand

---

## Future Improvements

Future versions of the dashboard could include:

* Combined Region, Product and Status filtering
* Date-range filtering
* Executive KPI cards
* Revenue growth analysis
* Month-over-month sales trends
* Regional performance rankings
* Product profitability analysis
* Sales forecasting
* Customer segmentation
* AI-powered natural-language questions
* Database integration
* Automated data refresh
* Downloadable management reports
* User authentication and role-based access

---

## Project Goal

The goal of this project was not simply to build a dashboard.

It was to demonstrate how **Python, Business Intelligence, Data Visualization, and AI-driven analytics can work together to transform raw business data into useful information for decision-makers.**

---

## Author

**Funmi Gbokoyi**

Financial Analyst | Data Analyst | Analytics Engineer | Financial Analytics & AI

I build analytical solutions that transform business data into actionable insights and help organizations make better financial and operational decisions.

---

⭐ **If you found this project useful, consider starring the repository.**

