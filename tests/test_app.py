from claude_test.app import create_app


def test_index():
    app = create_app()
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    assert b"claude-test" in response.data


def test_dashboard():
    app = create_app()
    client = app.test_client()
    response = client.get("/dashboard")
    assert response.status_code == 200
    assert b"Dashboard" in response.data


def test_settings():
    app = create_app()
    client = app.test_client()
    response = client.get("/settings")
    assert response.status_code == 200
    assert b"Settings" in response.data


def test_health():
    app = create_app()
    client = app.test_client()
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json["status"] == "ok"
