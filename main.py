def count_errors(logs):
    error_count = 0
    for log in logs:
        if "ERROR" in log:
            error_count += 1
    return error_count


def detect_login_failures(logs):
    failed_login_count = {}

    for log in logs:
        if "Login failed" in log:
            user_id = log.split("user_id=")[1]
            failed_login_count[user_id] = failed_login_count.get(user_id, 0) + 1

    return failed_login_count


def main():
    logs = [
        "INFO User login success user_id=101",
        "INFO User login success user_id=102",
        "ERROR Login failed user_id=103",
        "ERROR Login failed user_id=103",
        "ERROR Login failed user_id=103",
        "WARNING High response time /api/login",
        "ERROR Login failed user_id=104",
        "INFO User logout user_id=101"
    ]

    error_count = count_errors(logs)
    print("Total Errors:", error_count)

    if error_count >= 3:
        print("ALERT: High number of errors detected!")

    failed_logins = detect_login_failures(logs)
    print("Failed login attempts per user:", failed_logins)

    for user, count in failed_logins.items():
        if count >= 3:
            print(f"SECURITY ALERT: Possible brute force attack on user_id {user}")


if __name__ == "__main__":
    main()
