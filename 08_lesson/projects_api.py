import requests


class ProjectsAPI:

    # Сохраняем URL, логин и пароль при создании объекта класса
    def __init__(self, url, login, password) -> None:
        self.url = url
        self.login = login
        self.password = password

    def get_keys_list(self):
        body = {"login": self.login, "password": self.password}
        resp = requests.post(self.url + "/api-v2/auth/keys/get", json=body)

        response_data = resp.json()
        if isinstance(response_data, list) and len(response_data) > 0:
            return response_data[0]["key"]
        elif isinstance(response_data, dict):
            return response_data.get("key")

        raise ValueError(f"Неожиданный формат ответа авторизации: {response_data}")

    def _get_headers(self):
        my_token = self.get_keys_list()
        return {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {my_token}",
        }

    def create_project(self, title):
        my_headers = self._get_headers()
        project = {"title": title}
        resp = requests.post(
            self.url + "/api-v2/projects", json=project, headers=my_headers
        )

        response_data = resp.json()
        if isinstance(response_data, list):
            return response_data[0]["id"]
        return response_data["id"]

    def update_project(self, id, new_title):
        my_headers = self._get_headers()
        new_project = {"title": new_title}
        resp = requests.put(
            self.url + f"/api-v2/projects/{id}", json=new_project, headers=my_headers
        )

        response_data = resp.json()
        if isinstance(response_data, list):
            return response_data[0]["id"]
        return response_data["id"]

    def get_project_id(self, id):
        my_headers = self._get_headers()
        resp = requests.get(self.url + f"/api-v2/projects/{id}", headers=my_headers)
        return resp.json()
