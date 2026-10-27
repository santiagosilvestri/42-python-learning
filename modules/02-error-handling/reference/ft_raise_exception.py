def input_temperature(temp_str: str) -> int:
    temperature = int(temp_str)

    if temperature > 40:
        raise ValueError(f"{temperature}°C is too hot for plants (max 40°C)")

    if temperature < 0:
        raise ValueError(f"{temperature}°C is too cold for plants (min 0°C)")

    return temperature


def test_temperature() -> None:
    print("=== Garden Temperature Checker ===")

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

    print("\nInput data is '100'")
    try:
        temperature = input_temperature("100")
        print(f"Temperature is now {temperature}°C")
    except ValueError as error:
        print(f"Caught input_temperature error: {error}")

    print("\nInput data is '-50'")
    try:
        temperature = input_temperature("-50")
        print(f"Temperature is now {temperature}°C")
    except ValueError as error:
        print(f"Caught input_temperature error: {error}")

    print("\nAll tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()
