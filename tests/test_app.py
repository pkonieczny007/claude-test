from claude_test.models import User


def test_index(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"claude-test" in response.data


def test_dashboard(client):
    response = client.get("/dashboard")
    assert response.status_code == 200
    assert b"Dashboard" in response.data


def test_dashboard_user_count(client, db):
    db.session.add(User(username="alice", theme="light"))
    db.session.add(User(username="bob", theme="dark"))
    db.session.commit()
    response = client.get("/dashboard")
    assert b"2 registered users" in response.data


def test_settings_get(client):
    response = client.get("/settings")
    assert response.status_code == 200
    assert b"Settings" in response.data


def test_settings_post_saves_user(client, db):
    response = client.post(
        "/settings",
        data={"username": "alice", "theme": "dark"},
    )
    assert response.status_code == 200
    assert b"Settings saved!" in response.data
    assert b"alice" in response.data

    user = User.query.filter_by(username="alice").first()
    assert user is not None
    assert user.theme == "dark"


def test_settings_post_updates_existing_user(client, db):
    db.session.add(User(username="alice", theme="light"))
    db.session.commit()

    response = client.post(
        "/settings",
        data={"username": "alice", "theme": "dark"},
    )
    assert response.status_code == 200
    assert User.query.count() == 1
    assert User.query.first().theme == "dark"


def test_settings_post_empty_username(client, db):
    response = client.post(
        "/settings",
        data={"username": "", "theme": "dark"},
    )
    assert response.status_code == 200
    assert User.query.count() == 0


def test_health(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json["status"] == "ok"
