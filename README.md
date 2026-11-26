\# SecureWarehouse



\### A Secure Warehouse Management System



SecureWarehouse is a web-based Warehouse Management System (WMS) developed using Python and Flask. The project combines warehouse inventory management, logistics operations and cybersecurity principles to demonstrate how secure software can support modern warehouse environments.



\*\*Project Status:\*\* Under Active Development



\## Project Objectives



\- Manage warehouse products and inventory.

\- Record incoming and outgoing stock transactions.

\- Maintain a history of warehouse stock movements.

\- Implement secure authentication and role-based access control.

\- Apply cybersecurity principles to warehouse management processes.

\- Explore barcode-based inventory identification and scanning.



\## Current Features



\- User authentication and password hashing.

\- Role-based access control for administrators, warehouse managers and employees.

\- Product registration and inventory management.

\- Stock receiving and issuing.

\- Stock movement history.

\- Duplicate transaction reference protection.

\- CSRF protection on forms.

\- Secure session cookie configuration.



\## Technology Stack



| Technology | Purpose |

|---|---|

| Python | Backend programming |

| Flask | Web application framework |

| Flask-SQLAlchemy | Database integration |

| SQLite | Database |

| Flask-Login | User authentication |

| Flask-WTF | CSRF protection |

| HTML/CSS | User interface |

| Git and GitHub | Version control |



\## Project Structure



```text

SecureWarehouse/

├── app/

│   ├── templates/

│   ├── static/

│   ├── \_\_init\_\_.py

│   ├── auth.py

│   ├── commands.py

│   ├── decorators.py

│   ├── models.py

│   └── routes.py

├── docs/

├── tests/

├── instance/

├── requirements.txt

├── run.py

└── .gitignore

```



The local virtual environment and database are excluded from version control.



\## Installation and Setup



\### 1. Clone the repository



```bash

git clone https://github.com/Tshep12/SecureWarehouse.git

cd SecureWarehouse

```



\### 2. Create a virtual environment



```bash

python -m venv .venv

```



\### 3. Activate the environment



Windows:



```bash

.venv\\Scripts\\activate

```



\### 4. Install dependencies



```bash

python -m pip install -r requirements.txt

```



\### 5. Configure the application



Set a strong secret key using an environment variable before running the application.



PowerShell example:



```powershell

$env:SECRET\_KEY = "replace-with-a-strong-random-secret"

```



\### 6. Run the application



```bash

python run.py

```



Open your browser at:



```text

http://127.0.0.1:5000

```



A local SQLite database is initialized automatically when the application starts. Create your first user using the application's Flask CLI command.



\## Development Roadmap



\- \[x] Flask application foundation.

\- \[x] Authentication and user roles.

\- \[x] Product registration.

\- \[x] Inventory management.

\- \[x] Stock receiving and issuing.

\- \[x] Stock movement history.

\- \[x] Initial GitHub repository.

\- \[ ] Database integrity improvements.

\- \[ ] Barcode generation and scanning.

\- \[ ] Automated testing.

\- \[ ] Red Team security assessment.

\- \[ ] Reporting and analytics.

\- \[ ] Production deployment and documentation.



\## Cybersecurity Focus



Security is an important part of SecureWarehouse. The project incorporates password hashing, role-based authorization, CSRF protection and transaction validation.



Future development will explore security monitoring, vulnerability assessment, audit integrity and secure deployment practices.



\## Project Status



SecureWarehouse is an educational and portfolio project under active development. Features and documentation will evolve as development progresses.



\## Author



\*\*Tshep12\*\*



GitHub: https://github.com/Tshep12



\---



\*SecureWarehouse — Bringing warehouse management and cybersecurity together.\*

