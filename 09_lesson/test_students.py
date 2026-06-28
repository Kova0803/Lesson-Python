import pytest
from sqlalchemy import create_engine, text

DATABASE_URL = "postgresql://postgres:2zvD45Y4+@localhost:5432/QA"
engine = create_engine(DATABASE_URL)


@pytest.fixture
def db_cleaner():
    created_ids = []
    yield created_ids

    if created_ids:
        with engine.connect() as conn:
            conn.execute(
                text("DELETE FROM student WHERE id IN :ids"),
                {"ids": tuple(created_ids)},
            )
            conn.commit()


def test_add_student(db_cleaner):
    """Тест 1: Добавление сущности (Студента)"""
    test_name = "Гарри Поттер"
    test_age = 17

    with engine.connect() as conn:
        conn.execute(
            text("INSERT INTO student (name, age) VALUES (:name, :age)"),
            {"name": test_name, "age": test_age},
        )
        conn.commit()
        result = conn.execute(text("SELECT max(id) FROM student"))
        student_id = result.scalar()
        db_cleaner.append(student_id)

        check_result = conn.execute(
            text("SELECT name, age FROM student WHERE id = :id"), {"id": student_id}
        )
        student = check_result.mappings().one()

        assert student["name"] == test_name
        assert student["age"] == test_age


def test_edit_student(db_cleaner):
    """Тест 2: Изменение сущности (Студента)"""
    with engine.connect() as conn:
        conn.execute(
            text("INSERT INTO student (name, age) VALUES (:name, :age)"),
            {"name": "Оригинал", "age": 18},
        )
        conn.commit()
        student_id = conn.execute(text("SELECT max(id) FROM student")).scalar()
        db_cleaner.append(student_id)

        new_name = "Модифицирован"
        new_age = 25
        conn.execute(
            text("UPDATE student SET name = :name, age = :age WHERE id = :id"),
            {"name": new_name, "age": new_age, "id": student_id},
        )
        conn.commit()

        check_result = conn.execute(
            text("SELECT name, age FROM student WHERE id = :id"), {"id": student_id}
        )
        student = check_result.mappings().one()

        assert student["name"] == new_name
        assert student["age"] == new_age


def test_delete_student():
    with engine.connect() as conn:
        conn.execute(
            text("INSERT INTO student (name, age) VALUES (:name, :age)"),
            {"name": "Студент на удаление", "age": 21},
        )
        conn.commit()
        student_id = conn.execute(text("SELECT max(id) FROM student")).scalar()

        conn.execute(text("DELETE FROM student WHERE id = :id"), {"id": student_id})
        conn.commit()

        check_result = conn.execute(
            text("SELECT * FROM student WHERE id = :id"), {"id": student_id}
        )
        rows = check_result.fetchall()

        assert len(rows) == 0
