def input_temperature(temp_str: str) -> int:
    temp = int(temp_str)
    return temp


def test_temperature() -> None:
    print("=== Garden Temperature ===")

    print("\nInput data is '25'")
    try:
        temperature = input_temperature("25")
        print(f"Temperature is now {temperature}°C")
    except ValueError as error:
        print(f"Caught input_temperature error: {error}")

    print("\nInput data is 'abc'")
    try:
        temperature = input_temperature("abc")
        print(f"Temperature is now {temperature}°C")
    except ValueError as error:
        print(f"Caught input_temperature error: {error}")

    print("\nAll tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()
