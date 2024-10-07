import sqlite3
import csv


def erase_test_bank():
    conn = sqlite3.connect('question_bank.db')
    cursor = conn.cursor()

    cursor.execute("DELETE FROM questions")
    conn.commit()

    cursor.execute("DELETE FROM sqlite_sequence WHERE name = 'questions'")
    conn.commit()

    conn.close()
    print("Test bank deleted successfully.")


def insert_questions_from_csv(csv_file):
    conn = sqlite3.connect('question_bank.db')
    cursor = conn.cursor()

    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file)

        for row in reader:
            cursor.execute('''
                INSERT INTO questions (subject, question, option_a, option_b, option_c, option_d, correct_answer)
                VALUES (?, ?, ?, ?, ?, ?, ?)''',
                           (
                               row["subject"],
                               row['question'],
                               row['option_a'],
                               row['option_b'],
                               row['option_c'],
                               row['option_d'],
                               row['correct_answer']
                           )
                           )
    conn.commit()
    conn.close()
    print(f'Inserted questions from {csv_file} successfully.')


erase_test_bank()
insert_questions_from_csv('test_bank_sample.csv')
