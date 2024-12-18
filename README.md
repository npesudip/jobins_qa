jobins_qa_testing
Run Tests Via Terminal

Steps to Run the Project:

Install Python (if not installed): Download Python, make sure to add it to your PATH.

Download Project:

Clone or download the project to your computer.

**Set Up Virtual Environment: ** Open a terminal or command prompt. And Navigate to the project directory.

Run: python -m venv venv

**Activate the virtual environment: **On Windows: .\venv\Scripts\activate On macOS/Linux: source venv/bin/activate

Install Dependencies: Run the following command:

pip install -r requirements.txt

Run Tests: python -m pytest tests/ --html=reports/report.html --self-contained-html

View the Results: After running the tests, you can see the results in the terminal, or if you've set up HTML reporting, check the generated report.html
