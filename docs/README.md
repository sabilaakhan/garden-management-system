Garden Management System

A complete database-driven web application developed for the Database Lab Project. This system helps users efficiently manage gardens, plants, growth records, and reminders using a fully normalized relational database.

Project Overview:

The Garden Management System allows users to: Create and manage gardens Add and organize plants Track plant growth over time Store growth logs Schedule plant care reminders Maintain structured and normalized database records

Project Highlights This project includes:

✔ ERD Design ✔ Database Normalization (1NF → 3NF) ✔ Synthetic Dataset Generation ✔ Dataflow Documentation ✔ DDL Scripts (SQL Schema) ✔ DML Scripts (Data Population) ✔ Validation Queries ✔ GitHub Version Control

Technologies Used: Technology Purpose MySQL Workbench Database Design & Execution SQL Database Queries Mockaroo Synthetic Dataset Generation Git & GitHub Version Control Flask (Python) Backend Framework CSV Files Data Storage & Import

Database Schema USERS: Stores user account information. user_id (PK) username (Unique) email (Unique) password_hash

GARDENS: Stores gardens created by users. garden_id (PK) user_id (FK → USERS) name location

PLANTS: Stores plant details linked to users and gardens. plant_id (PK) garden_id (FK → GARDENS) user_id (FK → USERS) name species planted_date notes

GROWTH_LOGS: Tracks plant growth over time. log_id (PK) plant_id (FK → PLANTS) height leaf_count notes recorded_at

REMINDERS: Stores plant care reminders. reminder_id (PK) plant_id (FK → PLANTS) reminder_type due_date status (Pending/Completed/Missed)

Entity Relationships USERS → GARDENS → One-to-Many USERS → PLANTS → One-to-Many GARDENS → PLANTS → One-to-Many PLANTS → GROWTH_LOGS → One-to-Many PLANTS → REMINDERS → One-to-Many

Database Normalization The database follows: ✔ First Normal Form (1NF) ✔ Second Normal Form (2NF) ✔ Third Normal Form (3NF)

Benefits: Reduced redundancy Improved consistency Strong referential integrity Efficient query performance

Dataflow Description Data Input Users enter data through the web application: User Registration Garden Creation Plant Records Growth Tracking Reminder Scheduling ⚙ Data Processing Flow User data stored in USERS table Gardens linked using user_id Plants linked to USERS and GARDENS Growth logs linked to PLANTS Reminders linked to PLANTS

Data Output The system provides: Dashboard summaries Plant listings Garden details Growth history Reminder schedules Exportable reports

Project Structure garden-management-system/ │ ├── app.py ├── README.md ├── requirements.txt │ ├── models/ ├── routes/ ├── templates/ ├── static/ │ ├── database/ │ ├── schema.sql │ ├── dml.sql │ ├── users.csv │ ├── gardens.csv │ ├── plants.csv │ ├── growth_logs.csv │ └── reminders.csv │ └── documentation/ ├── ERD.png ├── normalization.pdf ├── dataflow.pdf Milestones Completed Milestone Description Status Milestone 1 ERD Design ✅ Completed Milestone 2 Normalization ✅ Completed Milestone 3 Dataset & Dataflow ✅ Completed Milestone 4 DDL Scripts ✅ Completed Milestone 5 DML & Validation ✅ Completed

Validation Queries The project includes: COUNT(*) checks NULL validation checks JOIN integrity checks UPDATE operations DELETE operations

These ensure:

✔ Correct row counts ✔ No missing values in key fields ✔ Proper foreign key relationships ✔ Database integrity maintained

🚀 How to Run the Project 📌 Step 1 — Clone Repository git clone https://github.com/sabilaakhan/garden-management-system.git cd garden-management-system 📌 Step 2 — Install Requirements pip install -r requirements.txt

If not available:

pip install flask flask_sqlalchemy flask_login pymysql 📌 Step 3 — Setup Database Open MySQL Workbench Run schema.sql This will create: Database Tables Constraints Indexes 📌 Step 4 — Load Data

Run:

dml.sql

This will:

Insert data Populate tables Execute validation queries 📌 Step 5 — Run Flask App python app.py 📌 Step 6 — Open in Browser

Open:

http://127.0.0.1:5000

Requirements Software Requirements: Software Version Python 3.10+ MySQL Server 8.0+ MySQL Workbench Latest Git Latest VS Code / PyCharm Recommended 📦 Python Libraries Flask Flask-SQLAlchemy Flask-Login PyMySQL

Features; User Management System Garden Tracking System Plant Management System Growth Monitoring System Reminder System Fully Normalized Database Strong Foreign Key Relationships SQL Constraints & Indexing

🔗 GitHub Repository

Garden Management System Repository