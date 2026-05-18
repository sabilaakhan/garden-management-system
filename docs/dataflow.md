Milestone 3 — Dataflow Description
Introduction:
The Garden Management System collects, stores, processes, and retrieves user and plant management data through a relational database structure.

1.Data Input

Data enters the system through web application forms where users register accounts, create gardens, add plants, record plant growth, and schedule reminders.
Synthetic data was generated using Mockaroo to simulate realistic system usage and populate the database tables.

2.Data Processing Flow

1. User information is stored in the USERS table during registration.
2. Gardens created by users are stored in the GARDENS table and linked through the user_id foreign key.
3. Plant records are stored in the PLANTS table and associated with both users and gardens using foreign keys.
4. Growth tracking information such as plant height and leaf count is stored in the GROWTH_LOGS table and linked to plants.
5. Reminder schedules for watering or fertilizing are stored in the REMINDERS table and connected to the corresponding plant records.

3.Data Output
The system retrieves and displays information through:
Dashboard summaries
Plant and garden listings
Growth history records
Reminder schedules
The data can also be exported for future reporting and database analysis.

Conclusion:
The database design ensures structured data movement between interconnected tables while maintaining data integrity and consistency.