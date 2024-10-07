import sqlite3
import csv


def erase_TOS():
    conn = sqlite3.connect('tos_testbank.db')
    cursor = conn.cursor()

    cursor.execute("DELETE FROM subjects")
    conn.commit()

    cursor.execute("DELETE FROM sqlite_sequence WHERE name = 'subjects'")
    conn.commit()

    conn.close()
    print("TOS deleted successfully.")


def insert_questions_from_csv(csv_file):
    conn = sqlite3.connect('tos_testbank.db')
    cursor = conn.cursor()

    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file)

        for row in reader:
            cursor.execute('''INSERT INTO subjects (subject, subject_topic, question_total, question_remembering, 
            question_understanding, question_applying, question_analyzing) VALUES (?, ?, ?, ?, ?, ?, ?)''',
                           (
                               row["subject"],
                               row['subject_topic'],
                               row['question_total'],
                               row['question_remembering'],
                               row['question_understanding'],
                               row['question_applying'],
                               row['question_analyzing']
                           )
                           )
    conn.commit()
    conn.close()
    print(f'Inserted TOS data from {csv_file} successfully.')


# erase_test_bank()
insert_questions_from_csv('subjects_tos.csv')
