import math

movies = [
    {
        "title": "The Dune Chronicles",
        "year": 2021,
        "genres": {"sci-fi", "drama"},
        "rating": 8.6,
        "duration_min": 155,
        "actors": ["T. Chalamet", "R. Ferguson", "O. Isaac"],
    },
    {
        "title": "Kitchen Stories",
        "year": 2019,
        "genres": {"comedy", "drama"},
        "rating": 7.1,
        "duration_min": 98,
        "actors": ["A. Novak", "M. Ferguson"],
    },
    {
        "title": "silent hours",
        "year": 2016,
        "genres": {"thriller", "drama"},
        "rating": 6.4,
        "duration_min": 112,
        "actors": ["J. Bloom", "K. Lee"],
    },
    {
        "title": "Comet Racers",
        "year": 2023,
        "genres": {"sci-fi", "action"},
        "rating": 5.9,
        "duration_min": 101,
        "actors": ["O. Isaac", "P. Diaz"],
    },
    {
        "title": "The Last Bakery",
        "year": 2014,
        "genres": {"comedy"},
        "rating": 7.8,
        "duration_min": 89,
        "actors": ["A. Novak", "T. Chalamet"],
    },
    {
        "title": "midnight in oslo",
        "year": 2020,
        "genres": {"thriller", "mystery"},
        "rating": 8.9,
        "duration_min": 124,
        "actors": ["K. Lee", "R. Ferguson"],
    },
    {
        "title": "Garden of Static",
        "year": 2022,
        "genres": {"drama"},
        "rating": 4.8,
        "duration_min": 137,
        "actors": ["P. Diaz", "J. Bloom"],
    },
    {
        "title": "The Quiet Algorithm",
        "year": 2024,
        "genres": {"sci-fi", "drama"},
        "rating": 9.2,
        "duration_min": 118,
        "actors": ["M. Ferguson", "O. Isaac"],
    },
    {
        "title": "Two Left Shoes",
        "year": 2011,
        "genres": {"comedy"},
        "rating": 6.0,
        "duration_min": 95,
        "actors": ["A. Novak", "K. Lee"],
    },
    {
        "title": "Red Harbor",
        "year": 2018,
        "genres": {"action", "thriller"},
        "rating": 7.3,
        "duration_min": 129,
        "actors": ["P. Diaz", "T. Chalamet"],
    },
]


# Этап 1. Переменные, числа, math
def average_rating(movies):
    """Средняя оценка каталога, округлённая до одного знака."""
    return round(sum(m["rating"] for m in movies) / len(movies), 1)


def catalog_age_stats(movies, current_year=2026):
    """Кортеж: (старейший фильм в годах, новейший, средний возраст через ceil)."""
    ages = [current_year - m["year"] for m in movies]
    return max(ages), min(ages), math.ceil(sum(ages) / len(ages))


def duration_in_hours(minutes):
    """Минуты в формат '2ч 35м' через // и %."""
    return f"{minutes // 60}ч {minutes % 60}м"


# Этап 2. Условия и match
def rating_tier(rating):
    """Категория качества: if/elif + тернарный оператор."""
    if rating >= 9:
        return "шедевр"
    elif rating >= 5:
        return "хорошо" if rating >= 7 else "средне"
    else:
        return "слабо"


def decade_label(year):
    """Метка возраста фильма через match с case _ if ..."""
    match year:
        case _ if year > 2020:
            return "новые"
        case _ if year >= 2015:
            return "недавние"
        case _:
            return "старые"

# Этап 3. Циклы
def print_non_comedy(movies):
    """Названия фильмов НЕ из жанра comedy: for + continue."""
    print("Фильмы, которые НЕ относятся к жанру комедии:")
    for movie in movies:
        if "comedy" in movie["genres"]:
            continue
        print(f"- {movie['title']}")


def first_masterpiece(movies, min_rating=9.0):
    """Первый фильм с рейтингом выше min_rating: while + break + else."""
    index = 0
    found = None
    while index < len(movies):
        if movies[index]["rating"] > min_rating:
            found = movies[index]
            break
        index += 1
    else:
        print("Шедевров не найдено")
    return found


def count_long_movies(movies, threshold=120):
    """Количество фильмов длиннее threshold: накопление в цикле for."""
    count = 0
    for movie in movies:
        if movie["duration_min"] > threshold:
            count += 1
    return count



# Этап 4. Строки
def normalize_title(title):
    """Title Case вручную через срез word[0].upper() + word[1:] (без str.title())."""
    words = []
    for word in title.split():
        words.append(word[0].upper() + word[1:])
    return " ".join(words)


def make_slug(title):
    """Слаг вида silent-hours через .lower() и .replace()."""
    return title.lower().replace(" ", "-")


def format_report_line(movie):
    """Единая строка отчёта: f-строка + duration_in_hours, жанры по алфавиту."""
    genres = ", ".join(sorted(movie["genres"]))
    duration = duration_in_hours(movie["duration_min"])
    return (
        f'"{normalize_title(movie["title"])}" ({movie["year"]}) — '
        f"{movie['rating']}/10, {duration}, жанры: {genres}"
    )


# Этап 5. Списки
def titles_sorted_by_rating(movies):
    """Названия по убыванию рейтинга: sorted + key, входной список не меняется."""
    ordered = sorted(movies, key=lambda movie: movie["rating"], reverse=True)
    return [movie["title"] for movie in ordered]


def top_n_by_rating(movies, n=3):
    """Топ-n записей (title, rating) — именно кортежи."""
    ordered = sorted(movies, key=lambda movie: movie["rating"], reverse=True)
    return [(movie["title"], movie["rating"]) for movie in ordered[:n]]



if __name__ == "__main__":
    print(f"Средняя оценка каталога: {average_rating(movies)}")
    oldest, newest, avg_age = catalog_age_stats(movies)
    print(f"Самый старый фильм: {oldest} лет, самый новый: {newest} лет")
    print(f"Средний возраст каталога: {avg_age} лет")
    print(f"155 минут = {duration_in_hours(155)}")

    print("Категории оценок (границы диапазонов):")
    for r in (9, 8.9, 7, 6.9, 5, 4.9):
        print(f"  rating_tier({r}) = {rating_tier(r)}")
    print("Метки десятилетий (границы диапазонов):")
    for y in (2024, 2021, 2020, 2015, 2014, 2011):
        print(f"  decade_label({y}) = {decade_label(y)}")

    print_non_comedy(movies)

    found = first_masterpiece(movies)
    if found:
        print(f"Первый шедевр: {found['title']} ({found['rating']})")

    print("Проверка ветки else (каталог без шедевров):")
    first_masterpiece([m for m in movies if m["rating"] <= 9.0])

    print(f"Фильмов длиннее 120 минут: {count_long_movies(movies)}")
    print(f"Фильмов длиннее 100 минут: {count_long_movies(movies, 100)}")

    print(normalize_title("silent hours"))
    print(make_slug("Silent Hours"))
    print(format_report_line(movies[7]))

    print("Отчёт по каталогу:")
    for m in movies:
        print(f"  {format_report_line(m)}")

    print("\n--- Списки ---")

    print("Названия по убыванию рейтинга:")
    for title in titles_sorted_by_rating(movies):
        print(f"  {title}")

    print(f"\nТоп-3: {top_n_by_rating(movies, 3)}")
    print(f"Топ-1: {top_n_by_rating(movies, 1)}")

    top_first = top_n_by_rating(movies, 3)[0]
    print(f"Тип записи в top_n: {type(top_first).__name__}")

    titles_before = [movie["title"] for movie in movies]
    titles_sorted_by_rating(movies)
    titles_after = [movie["title"] for movie in movies]
    print(f"Исходный список не изменён: {titles_before == titles_after}")