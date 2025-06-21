
def assert_status_code(response, expected_status):
    actual_status = str(response.status_code)
    assert actual_status == expected_status, f"Expected {expected_status}, but got {actual_status}"
    print(f"Validated Status Code: {actual_status}")