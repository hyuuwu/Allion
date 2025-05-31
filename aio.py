# AIO
import platform
import random
import string
import math
from datetime import datetime, timedelta
from collections import Counter
import re 
import os

# --- String Utilities ---

def reverse_string(s: str) -> str:
    """Reverses a given string."""
    return s[::-1]

def is_palindrome(s: str) -> bool:
    """Checks if a string is a palindrome (reads the same forwards and backwards)."""
    processed_s = ''.join(filter(str.isalnum, s)).lower()
    return processed_s == processed_s[::-1]

def count_vowels(s: str) -> int:
    """Counts the number of vowels (a, e, i, o, u) in a string, case-insensitive."""
    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char in vowels)

def generate_random_string(length: int, charset: str = string.ascii_letters + string.digits) -> str:
    """Generates a random string of a specified length from a given charset."""
    if length < 0:
        raise ValueError("Length cannot be negative.")
    return ''.join(random.choice(charset) for _ in range(length))

def simple_slugify(text: str) -> str:
    """Converts a string into a URL-friendly slug (lowercase, words separated by hyphens)."""
    text = text.lower()
    text = re.sub(r'[^\w\s-]', '', text) # Remove special characters except whitespace and hyphen
    text = re.sub(r'\s+', '-', text)    # Replace whitespace with hyphens
    text = re.sub(r'--+', '-', text)   # Replace multiple hyphens with a single one
    text = text.strip('-')
    return text

# --- Mathematical Utilities ---

def calculate_factorial(n: int) -> int:
    """Calculates the factorial of a non-negative integer."""
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    return math.factorial(n)

def is_prime(num: int) -> bool:
    """Checks if a number is a prime number (basic version)."""
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def get_fibonacci_sequence(n_terms: int) -> list:
    """Generates the Fibonacci sequence up to n_terms."""
    if n_terms <= 0:
        return []
    elif n_terms == 1:
        return [0]
    sequence = [0, 1]
    while len(sequence) < n_terms:
        next_val = sequence[-1] + sequence[-2]
        sequence.append(next_val)
    return sequence

def calculate_mean(numbers: list) -> float:
    """Calculates the arithmetic mean (average) of a list of numbers."""
    if not numbers:
        return 0.0
    return sum(numbers) / len(numbers)

def calculate_median(numbers: list) -> float:
    """Calculates the median of a list of numbers."""
    if not numbers:
        return 0.0
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_numbers[mid - 1] + sorted_numbers[mid]) / 2
    else:
        return float(sorted_numbers[mid])

# --- List/Collection Utilities ---

def flatten_list(nested_list: list) -> list:
    """Flattens a list of lists into a single list."""
    return [item for sublist in nested_list for item in sublist]

def remove_duplicates_from_list(input_list: list) -> list:
    """Removes duplicate elements from a list while preserving order."""
    seen = set()
    result = []
    for item in input_list:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

def get_random_element(input_list: list) -> any:
    """Returns a random element from a list."""
    if not input_list:
        return None
    return random.choice(input_list)

def chunk_list(input_list: list, chunk_size: int) -> list:
    """Splits a list into smaller chunks of a specified size."""
    if chunk_size <= 0:
        raise ValueError("Chunk size must be positive.")
    return [input_list[i:i + chunk_size] for i in range(0, len(input_list), chunk_size)]

# --- Date/Time Utilities ---

def get_current_datetime_iso() -> str:
    """Returns the current date and time in ISO 8601 format."""
    return datetime.now().isoformat()

def get_days_between_dates(date_str1: str, date_str2: str, fmt: str = "%Y-%m-%d") -> int:
    """Calculates the number of full days between two dates given as strings."""
    dt1 = datetime.strptime(date_str1, fmt)
    dt2 = datetime.strptime(date_str2, fmt)
    return abs((dt2 - dt1).days)

# --- Conversion Utilities ---

def celsius_to_fahrenheit(celsius: float) -> float:
    """Converts temperature from Celsius to Fahrenheit."""
    return (celsius * 9/5) + 32

def kilograms_to_pounds(kg: float) -> float:
    """Converts weight from kilograms to pounds."""
    return kg * 2.20462

# --- Miscellaneous Utilities ---

def simple_dice_roll(sides: int = 6) -> int:
    """Simulates rolling a dice with a specified number of sides."""
    if sides <= 0:
        raise ValueError("Number of sides must be positive.")
    return random.randint(1, sides)

def generate_random_hex_color() -> str:
    """Generates a random hex color code."""
    return f"#{random.randint(0, 0xFFFFFF):06x}"


def get_pc_specs() -> dict:
    """
    Gathers basic PC specifications using built-in Python modules.
    For more detailed info (RAM, specific CPU model details, disk usage),
    consider using a third-party library like 'psutil'.
    """
    specs = {
        "System Information": {
            "OS": platform.system(),
            "OS Release": platform.release(),
            "OS Version": platform.version(),
            "Hostname": platform.node(),
            "Architecture": platform.machine(),
        },
        "Processor Information": {
            "Processor": platform.processor(), # Note: May be empty or generic on some systems/OS
            "CPU Cores": os.cpu_count(),
        },
        "Python Environment": {
            "Python Version": platform.python_version(),
            "Python Implementation": platform.python_implementation(),
            "Python Compiler": platform.python_compiler(),
            "Python Build No": platform.python_build()[0],
            "Python Build Date": platform.python_build()[1],
        }
    }
    return specs

def print_pc_specs(specs: dict = None) -> None:
    """
    Prints PC specifications in a readable format.
    If no specs are provided, it calls get_pc_specs() first.
    """
    if specs is None:
        specs = get_pc_specs()



# --- 1st Example Usage 
if __name__ == "__main__":
    print("--- String Utilities ---")
    print(f"Reverse of 'hello': {reverse_string('hello')}")
    print(f"Is 'madam' a palindrome? {is_palindrome('madam')}")
    print(f"Is 'Race car!' a palindrome? {is_palindrome('Race car!')}")
    print(f"Vowels in 'Programming': {count_vowels('Programming')}")
    print(f"Random string (10 chars): {generate_random_string(10)}")
    print(f"Slugify 'My Awesome Title!': {simple_slugify('My Awesome Title!')}")

    print("\n--- Mathematical Utilities ---")
    print(f"Factorial of 5: {calculate_factorial(5)}")
    print(f"Is 17 prime? {is_prime(17)}")
    print(f"Is 1 prime? {is_prime(1)}")
    print(f"Fibonacci (10 terms): {get_fibonacci_sequence(10)}")
    nums = [1, 5, 2, 8, 3, 9, 4, 7, 6]
    print(f"Mean of {nums}: {calculate_mean(nums)}")
    print(f"Median of {nums}: {calculate_median(nums)}")
    print(f"Median of {nums + [10]}: {calculate_median(nums + [10])}")


    print("\n--- List/Collection Utilities ---")
    nested = [[1, 2], [3, 4, 5], [6]]
    print(f"Flatten {nested}: {flatten_list(nested)}")
    dupes = [1, 2, 2, 3, 4, 4, 4, 5, 1]
    print(f"Remove duplicates from {dupes}: {remove_duplicates_from_list(dupes)}")
    print(f"Random element from {dupes}: {get_random_element(dupes)}")
    print(f"Chunk {dupes} by 3: {chunk_list(dupes, 3)}")

    print("\n--- Date/Time Utilities ---")
    print(f"Current ISO datetime: {get_current_datetime_iso()}")
    print(f"Days between 2023-01-01 and 2023-01-10: {get_days_between_dates('2023-01-01', '2023-01-10')}")

    print("\n--- Conversion Utilities ---")
    print(f"25°C in Fahrenheit: {celsius_to_fahrenheit(25)}°F")
    print(f"70kg in pounds: {kilograms_to_pounds(70)} lbs")

    print("\n--- Miscellaneous Utilities ---")
    print(f"Dice roll (d6): {simple_dice_roll()}")
    print(f"Dice roll (d20): {simple_dice_roll(20)}")
    print(f"Random hex color: {generate_random_hex_color()}")
    

#pt2,like kanye omari west

import uuid 
import time 

# --- More String Utilities ---

def capitalize_words(s: str) -> str:
    """Capitalizes the first letter of each word in a string."""
    return ' '.join(word.capitalize() for word in s.split())

def count_substring(text: str, sub: str) -> int:
    """Counts occurrences of a substring within a string."""
    return text.count(sub)

def truncate_string(s: str, max_length: int, suffix: str = "...") -> str:
    """Truncates a string to a maximum length, appending a suffix if truncated."""
    if len(s) <= max_length:
        return s
    return s[:max_length - len(suffix)] + suffix

def is_blank(s: str) -> bool:
    """Checks if a string is None, empty, or contains only whitespace."""
    return s is None or not s.strip()

# --- More Mathematical Utilities ---

def find_gcd(a: int, b: int) -> int:
    """Finds the Greatest Common Divisor (GCD) of two integers using Euclidean algorithm."""
    while(b):
        a, b = b, a % b
    return abs(a)

def find_lcm(a: int, b: int) -> int:
    """Finds the Least Common Multiple (LCM) of two integers."""
    if a == 0 or b == 0:
        return 0
    return abs(a * b) // find_gcd(a, b)

def is_perfect_square(n: int) -> bool:
    """Checks if a non-negative integer is a perfect square."""
    if n < 0:
        return False
    if n == 0:
        return True
    sqrt_n = int(math.sqrt(n))
    return sqrt_n * sqrt_n == n

def degrees_to_radians(degrees: float) -> float:
    """Converts an angle from degrees to radians."""
    return math.radians(degrees)

def radians_to_degrees(radians: float) -> float:
    """Converts an angle from radians to degrees."""
    return math.degrees(radians)

# --- More List/Collection Utilities ---

def get_most_common_element(input_list: list) -> any:
    """Finds the most common element in a list. Returns None if list is empty."""
    if not input_list:
        return None
    # Counter from collections module 
    counts = Counter(input_list)
    return counts.most_common(1)[0][0]

def shuffle_list_inplace(input_list: list) -> None:
    """Shuffles the elements of a list in-place."""
    random.shuffle(input_list) # Modifies the original list

def find_intersection(list1: list, list2: list) -> list:
    """Returns a list containing common elements between two lists (intersection)."""
    return list(set(list1) & set(list2))

def find_difference(list1: list, list2: list) -> list:
    """Returns a list containing elements present in list1 but not in list2."""
    return list(set(list1) - set(list2))

# --- More Date/Time Utilities ---

def add_time_to_date(date_obj: datetime, days: int = 0, hours: int = 0, minutes: int = 0, seconds: int = 0) -> datetime:
    """Adds a specified amount of time (days, hours, minutes, seconds) to a datetime object."""
    return date_obj + timedelta(days=days, hours=hours, minutes=minutes, seconds=seconds)

def get_day_of_week(date_str: str, fmt: str = "%Y-%m-%d") -> str:
    """Returns the day of the week (e.g., 'Monday') for a given date string."""
    dt_obj = datetime.strptime(date_str, fmt)
    return dt_obj.strftime("%A")

def is_leap_year(year: int) -> bool:
    """Checks if a year is a leap year."""
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def get_current_year() -> int:
    """Returns the current year."""
    return datetime.now().year

def get_current_month() -> int:
    """Returns the current month (1-12)."""
    return datetime.now().month

def get_current_day() -> int:
    """Returns the current day of the month."""
    return datetime.now().day

# --- Validation Utilities ---

def is_valid_email_simple(email: str) -> bool:
    """Performs a simple validation for an email address format using regex."""
    # This is a basic regex and might not cover all edge things
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return bool(re.match(pattern, email))

def is_integer_string(s: str) -> bool:
    """Checks if a string represents a valid integer."""
    if s is None: return False
    return s.strip().lstrip('-+').isdigit()

def is_float_string(s: str) -> bool:
    """Checks if a string represents a valid floating-point number."""
    if s is None: return False
    try:
        float(s)
        return True
    except ValueError:
        return False

# --- Miscellaneous Utilities ---

def generate_uuid4_string() -> str:
    """Generates a random UUID4 string."""
    return str(uuid.uuid4())

def measure_execution_time(func, *args, **kwargs) -> tuple:
    """
    Measures the execution time of a given function.
    Returns a tuple: (result_of_function, time_taken_in_seconds).
    """
    start_time = time.perf_counter()
    result = func(*args, **kwargs)
    end_time = time.perf_counter()
    return result, end_time - start_time

# --- Example Shi
if __name__ == "__main__":
   
    print("\n--- More String Utilities ---")
    print(f"Capitalize 'hello world example': {capitalize_words('hello world example')}")
    print(f"Count 'l' in 'hello world': {count_substring('hello world', 'l')}")
    print(f"Truncate 'This is a long string' to 10 chars: {truncate_string('This is a long string', 10)}")
    print(f"Is '   ' blank? {is_blank('   ')}")
    print(f"Is '' blank? {is_blank('')}")
    print(f"Is 'not blank' blank? {is_blank('not blank')}")


    print("\n--- More Mathematical Utilities ---")
    print(f"GCD of 48 and 18: {find_gcd(48, 18)}")
    print(f"LCM of 48 and 18: {find_lcm(48, 18)}")
    print(f"Is 25 a perfect square? {is_perfect_square(25)}")
    print(f"Is 26 a perfect square? {is_perfect_square(26)}")
    print(f"180 degrees in radians: {degrees_to_radians(180)}")
    print(f"Pi radians in degrees: {radians_to_degrees(math.pi)}")

    print("\n--- More List/Collection Utilities ---")
    common_list = [1, 2, 2, 3, 3, 3, 4, 'a', 'a', 'a', 'a']
    print(f"Most common in {common_list}: {get_most_common_element(common_list)}")
    shuffle_me = [1, 2, 3, 4, 5]
    shuffle_list_inplace(shuffle_me)
    print(f"Shuffled list (in-place): {shuffle_me}")
    list_a = [1, 2, 3, 4, 5]
    list_b = [4, 5, 6, 7, 8]
    print(f"Intersection of {list_a} and {list_b}: {find_intersection(list_a, list_b)}")
    print(f"Difference {list_a} - {list_b}: {find_difference(list_a, list_b)}")


    print("\n--- More Date/Time Utilities ---")
    now = datetime.now()
    print(f"Now: {now}")
    print(f"Now + 5 days and 3 hours: {add_time_to_date(now, days=5, hours=3)}")
    print(f"Day of week for 2023-10-26: {get_day_of_week('2023-10-26')}")
    print(f"Is 2024 a leap year? {is_leap_year(2024)}")
    print(f"Is 2023 a leap year? {is_leap_year(2023)}")
    print(f"Current Year: {get_current_year()}, Month: {get_current_month()}, Day: {get_current_day()}")

    print("\n--- Validation Utilities ---")
    print(f"Is 'test@example.com' a valid email? {is_valid_email_simple('test@example.com')}")
    print(f"Is 'test@example' a valid email? {is_valid_email_simple('test@example')}")
    print(f"Is '12345' an integer string? {is_integer_string('12345')}")
    print(f"Is '-123' an integer string? {is_integer_string('-123')}")
    print(f"Is '12.34' an integer string? {is_integer_string('12.34')}")
    print(f"Is '3.14' a float string? {is_float_string('3.14')}")
    print(f"Is '-0.5' a float string? {is_float_string('-0.5')}")
    print(f"Is 'abc' a float string? {is_float_string('abc')}")


    print("\n--- Miscellaneous Utilities ---")
    print(f"Generated UUID4: {generate_uuid4_string()}")

    def example_func_to_time(n):
        time.sleep(n * 0.1) # Simulate work
        return sum(range(n))

    result, time_taken = measure_execution_time(example_func_to_time, 10000)
    print(f"Example function took {time_taken:.4f} seconds. Result: {result}")