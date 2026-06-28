import os
import pytest
import requests
from dotenv import load_dotenv
from projects_api import ProjectsAPI

load_dotenv()

REAL_URL = os.getenv("YOUGILE_URL", "https://yougile.com")
LOGIN = os.getenv("YOUGILE_LOGIN")
PASSWORD = os.getenv("YOUGILE_PASSWORD")


@pytest.fixture(scope="session")
def api_client():
    if not LOGIN or not PASSWORD:
        pytest.fail(
            "Ошибка: Переменные YOUGILE_LOGIN или YOUGILE_PASSWORD не заданы в .env"
        )

    return ProjectsAPI(url=REAL_URL, login=LOGIN, password=PASSWORD)


@pytest.fixture
def temp_project(api_client):
    project_id = api_client.create_project(title="Тестовый проект")
    yield project_id
    my_headers = api_client._get_headers()
    requests.delete(
        f"{api_client.url}/api-v2/projects/{project_id}", headers=my_headers
    )


# 1. create_project
def test_create_project_positive(api_client):
    # Позитивный тест: создание проекта с валидным названием
    title = "Автотест: Новый проект"
    project_id = api_client.create_project(title=title)
    assert project_id is not None
    assert isinstance(project_id, (int, str))

    # Удаляем созданный вручную проект
    my_headers = api_client._get_headers()
    requests.delete(
        f"{api_client.url}/api-v2/projects/{project_id}", headers=my_headers
    )


def test_create_project_negative(api_client):
    # Негативный тест: создание проекта без авторизации,неверный токен
    bad_client = ProjectsAPI(url=REAL_URL, login=LOGIN, password="wrong_password")

    with pytest.raises((KeyError, requests.exceptions.HTTPError)):
        bad_client.create_project(title="Проект-призрак")


# 2. update_project
def test_update_project_positive(api_client, temp_project):
    # Позитивный тест: изменение названия существующего проекта
    new_title = "Измененное название проекта"
    updated_id = api_client.update_project(id=temp_project, new_title=new_title)
    assert updated_id == temp_project


def test_update_project_negative(api_client):
    # Негативный тест: изменение проекта с несуществующим или невалидным ID
    invalid_id = "non-existent-id-12345"
    with pytest.raises(KeyError):
        api_client.update_project(id=invalid_id, new_title="Новое имя")


# 3. get_project_id
def test_get_project_id_positive(api_client, temp_project):
    # Позитивный тест: получение информации о существующем проекте
    project_data = api_client.get_project_id(id=temp_project)
    assert isinstance(project_data, dict)
    assert "id" in project_data or "title" in project_data
    if "id" in project_data:
        assert project_data["id"] == temp_project


def test_get_project_id_negative(api_client):
    # Негативный тест: запрос информации о несуществующем ID
    invalid_id = "00000000000"
    project_data = api_client.get_project_id(id=invalid_id)
    assert "title" not in project_data
