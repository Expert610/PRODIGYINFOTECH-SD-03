import mysql.connector

# Connect to MySQL Database
def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="password",
        database="cms"
    )

# Create (Insert)
def add_contact(name, phone, email):
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute("INSERT INTO contactinfo (name, phone, email) VALUES (%s, %s, %s)", (name, phone, email))
    conn.commit()
    print("Contact added.")
    cursor.close()
    conn.close()
    return True

# Read (Fetch All)
def get_all_contacts():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM contactinfo")
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return rows

# Update
def update_contact(contact_id, name=None, phone=None, email=None):
    conn = get_connection()
    cursor = conn.cursor()
    updates = []
    values = []

    if name:
        updates.append("name=%s")
        values.append(name)
    if phone:
        updates.append("phone=%s")
        values.append(phone)
    if email:
        updates.append("email=%s")
        values.append(email)

    values.append(contact_id)
    sql = f"UPDATE contactinfo SET {', '.join(updates)} WHERE id=%s"
    cursor.execute(sql, tuple(values))
    conn.commit()
    print("Contact updated.")
    cursor.close()
    conn.close()

# Delete
def delete_contact(contact_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM contactinfo WHERE id=%s", (contact_id,))
    conn.commit()
    print("Contact deleted.")
    cursor.close()
    conn.close()
