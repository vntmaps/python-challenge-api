def test_get_all_tasks(client, seed_data):
    """
    Given a user with access to a dataset containing multiple tasks
    When the user requests all tasks without any filters
    Then the response status is 200 OK and all tasks are returned.
    """
    response = client.get('/tasks')
    data = response.get_json()

    assert response.status_code == 200
    assert len(data) == 2
    assert data[0]['title'] == "Task One"
    assert data[1]['status'] == "completed"

def test_get_tasks_filter_pending(client, seed_data):
    """
    Given a user with access to a dataset containing tasks with different statuses
    When the user requests tasks filtered by status 'pending'
    Then the response status is 200 OK and only pending tasks are returned.
    """
    response = client.get('/tasks?status=pending')
    data = response.get_json()

    assert response.status_code == 200
    assert len(data) == 1
    assert data[0]['status'] == "pending"
    assert data[0]['title'] == "Task One"

def test_get_tasks_filter_empty_result(client, seed_data):
    """
    Given a user with access to the dataset
    When the user requests tasks with a status filter that has no matches (e.g., 'archived')
    Then the response status is 200 OK and an empty list is returned.
    """
    response = client.get('/tasks?status=archived')
    data = response.get_json()

    assert response.status_code == 200
    assert len(data) == 0

def test_get_tasks_no_data(client):
    """
    Given a user and an empty database
    When the user requests all tasks
    Then the response status is 200 OK and an empty list is returned.
    """
    response = client.get('/tasks')
    data = response.get_json()

    assert response.status_code == 200
    assert data == []