import httpx


def main() -> None:
    response = httpx.get("https://httpbin.org/uuid", timeout=10)
    response.raise_for_status()  # turn 4xx/5xx replies into an exception
    print(response.status_code, response.json()["uuid"])


if __name__ == "__main__":
    main()