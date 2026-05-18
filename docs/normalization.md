Milestone 2 — Normalization Report
Introduction:
The database schema for Garden Management System is normalized up to Third Normal Form (3NF) to reduce redundancy, improve consistency, and maintain data integrity.

1.USERS Table:
Attributes:
user_id (PK)
username
email
password_hash

1NF:
The table satisfies 1NF because all attributes contain atomic values and there are no repeating groups.
2NF:
The table satisfies 2NF because the primary key is a single attribute (user_id), and all non-key attributes fully depend on it.
3NF:
The table satisfies 3NF because there are no transitive dependencies between non-key attributes.

2.GARDENS Table:
Attributes:
garden_id (PK)
user_id (FK)
name
location

1NF:
All columns contain atomic values and each garden record is unique.
2NF:
The table satisfies 2NF because all non-key attributes depend entirely on the primary key (garden_id).
3NF:
The table satisfies 3NF because there are no unnecessary dependencies between non-key attributes.

3.PLANTS Table:
Attributes:
plant_id (PK)
user_id (FK)
garden_id (FK)
name
species
planted_date
notes
1NF:
The table satisfies 1NF because all fields contain single atomic values.
2NF:
The table satisfies 2NF because all attributes depend fully on the primary key (plant_id).
3NF:
The table satisfies 3NF because non-key attributes do not depend on other non-key attributes.

4.GROWTH_LOGS Table:
Attributes:
log_id (PK)
plant_id (FK)
height
leaf_count
notes
recorded_at
1NF:
All values are atomic and each record is unique.
2NF:
The table satisfies 2NF because all attributes depend fully on the primary key (log_id).
3NF:
The table satisfies 3NF because there are no transitive dependencies.

5.REMINDERS Table:
Attributes:
reminder_id (PK)
plant_id (FK)
reminder_type
due_date
status
1NF:
The table satisfies 1NF because all attributes contain atomic values.
2NF:
The table satisfies 2NF because all attributes depend fully on the primary key (reminder_id).
3NF:
The table satisfies 3NF because there are no dependencies among non-key attributes.

Duplicate and Redundancy Review:
The schema was reviewed for duplicate or redundant data. No major redundancies were found. Relationships between entities were separated using foreign keys to avoid repeated information and ensure normalization.

Conclusion:
The Garden Management System database schema successfully satisfies First Normal Form (1NF), Second Normal Form (2NF), and Third Normal Form (3NF). The schema is structured to reduce redundancy, maintain consistency, and support efficient data management.