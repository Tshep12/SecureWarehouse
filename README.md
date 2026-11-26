# SecureWarehouse

### A Cybersecure Warehouse Management System

**SecureWarehouse** is a web-based Warehouse Management System (WMS) developed using Python and Flask. It combines warehouse operations, inventory management, logistics principles and cybersecurity practices to demonstrate how secure technology can support modern warehouse environments.

The project brings together concepts from **Logistics and Supply Chain Management** and **Cybersecurity**, with a focus on inventory accuracy, access control, transaction integrity and secure warehouse operations.

> **Project Status:** Under Active Development

---

## 1. Project Overview

Warehouse management systems handle important business information, including inventory levels, stock movements, product records and employee activities.

SecureWarehouse aims to address these operational requirements while incorporating security controls that help protect warehouse data and prevent unauthorised activities.

The project is being developed as a practical portfolio application to demonstrate skills in software development, warehouse management, database design and cybersecurity.

## 2. Project Objectives

The main objectives of SecureWarehouse are to:

- Develop a functional warehouse inventory management system.
- Manage product registration and inventory records.
- Record incoming and outgoing stock transactions.
- Maintain traceable stock movement history.
- Implement secure user authentication and role-based access control.
- Apply cybersecurity principles to warehouse operations.
- Improve transaction validation and database integrity.
- Introduce barcode-based product identification and scanning.
- Develop reporting and analytics capabilities for inventory monitoring.

## 3. Implemented Features

The following features have been developed and tested during the current development phase.

### Warehouse Management

- Product registration and management.
- Inventory listing and stock quantity monitoring.
- Stock receiving and issuing.
- Stock movement history.
- Transaction reference validation.
- Insufficient stock validation to prevent invalid stock issues.

### Authentication and Access Control

- User login and logout functionality.
- Password hashing and verification.
- Role-based access control.
- Support for three user roles:
  - Administrator
  - Warehouse Manager
  - Employee
- Restricted access to authorised warehouse functions.

### Security Controls

- CSRF protection using Flask-WTF.
- Secure password storage using Werkzeug password hashing.
- HTTP-only session cookies.
- SameSite session cookie configuration.
- Login-protected application routes.
- Server-side role and permission checks.
- Application-level duplicate transaction reference checks.

## 4. Technology Stack

| Technology | Purpose |
|---|---|
| Python | Backend programming |
| Flask | Web application framework |
| Flask-SQLAlchemy | Database integration and ORM |
| SQLite | Relational database |
| Flask-Login | Authentication and session management |
| Flask-WTF | CSRF protection |
| Werkzeug | Password hashing and security utilities |
| HTML and CSS | User interface |
| Git | Version control |
| GitHub | Source code hosting and project management |

## 5. Application Structure

```text
SecureWarehouse/
│
├── app/
│   ├── templates/
│   │   ├── index.html
│   │   ├── login.html
│   │   ├── dashboard.html
│   │   ├── add_product.html
│   │   ├── inventory.html
│   │   ├── receive_stock.html
│   │   ├── issue_stock.html
│   │   └── stock_history.html
│   │
│   ├── __init__.py
│   ├── auth.py
│   ├── commands.py
│   ├── decorators.py
│   ├── models.py
│   └── routes.py
│
├── docs/
├── tests/
│
├── .gitignore
├── requirements.txt
├── README.md
└── run.py
```

**Note:** The SQLite database, local virtual environment and Python cache files are excluded from version control.

## 6. Installation and Setup

Follow these instructions to run SecureWarehouse locally on a Windows computer.

### Prerequisites

- Python installed.
- Git installed.
- A Windows terminal or Command Prompt.

### Step 1: Clone the repository

```bash
git clone https://github.com/Tshep12/SecureWarehouse.git
```

Navigate into the project directory:

```bash
cd SecureWarehouse
```

### Step 2: Create a virtual environment

```bash
python -m venv .venv
```

### Step 3: Activate the virtual environment

```bash
.venv\Scripts\activate
```

### Step 4: Install dependencies

```bash
python -m pip install -r requirements.txt
```

### Step 5: Configure the application secret key

Set a strong secret key using an environment variable.

PowerShell example:

```powershell
$env:SECRET_KEY = "your-strong-random-secret-key"
```

Use a securely generated secret in your own environment. Never commit secret keys or credentials to GitHub.

### Step 6: Start the application

```bash
python run.py
```

### Step 7: Open the application

Visit the following address in your browser:

```text
http://127.0.0.1:5000
```

The application initialises its local SQLite database when it starts.

Create an initial user account using the registered Flask CLI command:

```bash
python -m flask --app run.py create-user
```

Follow the prompts to create an administrator or other authorised user.

## 7. Development Roadmap

SecureWarehouse is being developed incrementally. The following roadmap outlines completed functionality and planned improvements.

### Completed

- [x] Flask application foundation.
- [x] Database initialisation.
- [x] User authentication.
- [x] Password hashing.
- [x] Role-based access control.
- [x] Product registration.
- [x] Inventory management.
- [x] Stock receiving.
- [x] Stock issuing.
- [x] Stock movement history.
- [x] CSRF protection.
- [x] Duplicate transaction reference validation.
- [x] Initial GitHub repository and documentation.

### In Progress

- [ ] Database integrity improvements.
- [ ] Stronger transaction constraints.
- [ ] Security hardening.
- [ ] Barcode integration.

### Planned

- [ ] Barcode generation and product identification.
- [ ] USB barcode scanner integration.
- [ ] Smartphone camera barcode scanning.
- [ ] Automated unit and integration testing.
- [ ] Red Team security assessment.
- [ ] Vulnerability identification and remediation.
- [ ] Low-stock and critical-stock alerts.
- [ ] Inventory forecasting and analytics.
- [ ] Annual stock performance comparisons.
- [ ] Downloadable inventory reports.
- [ ] Production deployment.
- [ ] Technical and security documentation.

## 8. Cybersecurity Approach

Cybersecurity is a core development consideration rather than an additional feature.

SecureWarehouse incorporates security controls intended to protect application access, warehouse information and transaction operations.

The security development objectives include:

- **Authentication:** Ensure users must authenticate before accessing protected functionality.
- **Authorisation:** Restrict operations according to assigned user roles.
- **Data protection:** Protect passwords through secure hashing and avoid exposing sensitive configuration.
- **Input validation:** Validate transaction data and reject invalid stock operations.
- **Transaction integrity:** Prevent repeated transaction references and improve database consistency.
- **Auditability:** Maintain stock movement records for operational traceability.
- **Security testing:** Assess the application for vulnerabilities and document remediation.

A future Red Team assessment will evaluate the application's security against realistic attack scenarios.

## 9. Project Scope and Learning Outcomes

This project demonstrates the integration of:

- Warehouse Management Systems.
- Inventory control and stock movement management.
- Logistics and Supply Chain Management.
- Database design and application development.
- Authentication and access control.
- Cybersecurity principles.
- Secure software development practices.
- Security testing and vulnerability assessment.

The long-term objective is to develop a functional, secure and extensible warehouse management application.

## 10. Project Status

SecureWarehouse is an educational and professional portfolio project currently under active development.

Features, security controls, testing procedures and documentation will continue to evolve throughout development.

## 11. Author

**Tshep12**

GitHub: [https://github.com/Tshep12](https://github.com/Tshep12)

Project Repository: [https://github.com/Tshep12/SecureWarehouse](https://github.com/Tshep12/SecureWarehouse)

---

*SecureWarehouse — Integrating warehouse management, supply chain operations and cybersecurity.*

