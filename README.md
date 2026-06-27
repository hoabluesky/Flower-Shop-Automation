# 🌸 Flower Shop Test Automation Framework

A UI automation framework built with **Python**, **Playwright**, and **Pytest** to automate testing of a sample Flower Shop web application.

This project demonstrates modern Quality Engineering practices including the **Page Object Model (POM)**, **data-driven testing**, **HTML reporting**, and **Continuous Integration (CI)** using **Jenkins Pipeline as Code**.

---

# 🚀 Technologies

* Python 3
* Playwright
* Pytest
* Pytest-HTML
* Jenkins
* Jenkins Pipeline (`Jenkinsfile`)
* Git
* GitHub

---

# 📌 Features

* UI automation using Playwright
* Page Object Model (POM)
* Data-driven testing
* HTML test reporting
* Jenkins Continuous Integration
* Jenkins Pipeline as Code (`Jenkinsfile`)
* Clean and maintainable automation framework

---

# 📂 Project Structure

```text
Flower-Shop-Automation/
│── pages/
├── images/
├── tests/
├── test_data/
├── reports/
├── conftest.py
├── pytest.ini
├── requirements.txt
├── Jenkinsfile
└── README.md
```

---

# ▶️ Getting Started

## Clone the repository

```bash
git clone <repository-url>
cd Flower-Shop-Automation
```

## Create a virtual environment

```bash
python -m venv venv
```

## Activate the virtual environment (Windows)

```bash
venv\Scripts\activate
```

## Install project dependencies

```bash
pip install -r requirements.txt
```

## Install Playwright browsers

```bash
playwright install
```

---

# 🧪 Running the Tests

Run the complete test suite

```bash
pytest
```

Run in headed mode

```bash
pytest --headed
```

Generate an HTML report

```bash
pytest --html=reports/report.html --self-contained-html
```

---

# ✅ Current Automated Test Scenarios

The current UI automation suite includes:

* Login
* User Registration
* Product Search
* Shopping Cart

These scenarios demonstrate end-to-end UI automation using the Page Object Model and Pytest.

---

# ⚙️ Continuous Integration

This project includes a Jenkins Pipeline (`Jenkinsfile`).

The pipeline performs the following steps:

1. Installs project dependencies from `requirements.txt`.
2. Installs the Playwright Chromium browser.
3. Executes the Pytest automation suite.
4. Generates an HTML test report.
5. Archives the generated report after execution.

The pipeline configuration is stored in the repository as a `Jenkinsfile`, allowing the CI process to be version controlled together with the test automation framework.

---

# 🏗 Framework Design

The automation framework follows the **Page Object Model (POM)** design pattern.

Benefits include:

* Separation of page interactions from test logic
* Improved maintainability
* Better code reusability
* Easier scalability
* Cleaner and more readable test cases

---

# 📊 Test Reporting

The framework generates self-contained HTML reports using **Pytest-HTML**, providing:

* Test execution summary
* Passed / Failed statistics
* Execution duration
* Failure details

---

# 🚧 Planned Enhancements

The following improvements are planned:

* REST API automation using Python Requests
* Logging framework
* BDD using Gherkin
* GitHub Actions workflow
* Screenshot capture on test failure
* Expanded regression coverage

---

# 💡 Skills Demonstrated

* Python
* Playwright
* Pytest
* UI Test Automation
* Page Object Model (POM)
* Data-driven Testing
* HTML Reporting
* Jenkins
* Jenkins Pipeline
* Continuous Integration (CI)
* Git
* GitHub

---

# 👨‍💻 Author

Developed as a personal learning project to strengthen practical Software Quality Engineering skills, focusing on automation framework design, UI automation, and Continuous Integration using Python, Playwright, and Jenkins.
