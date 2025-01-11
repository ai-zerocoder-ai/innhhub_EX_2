import requests
from bs4 import BeautifulSoup

# Заголовки для имитации реального пользователя
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

def get_price_from_investing(url):
    """
    Парсит текущую цену с указанной страницы Investing.com
    :param url: URL страницы
    :return: Цена как float или None в случае ошибки
    """
    try:
        response = requests.get(url, headers=HEADERS)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, "html.parser")
            # Ищем элемент с атрибутом data-test="instrument-price-last"
            price_tag = soup.find("div", {"data-test": "instrument-price-last"})
            if price_tag:
                # Удаляем запятые (заменяем на точки) и преобразуем в float
                return float(price_tag.text.replace(',', '.').strip())
        return None
    except Exception as e:
        print(f"Ошибка парсинга {url}: {e}")
        return None

def get_ttf_price():
    """
    Получает цену природного газа (TTF) с Investing.com
    :return: Цена в €/МВт·ч или None
    """
    url = "https://ru.investing.com/commodities/dutch-ttf-gas-c1-futures"
    return get_price_from_investing(url)

def get_carbon_price():
    """
    Получает цену на CO₂ (EU ETS) с Investing.com
    :return: Цена в €/тонну или None
    """
    url = "https://ru.investing.com/commodities/carbon-emissions"
    return get_price_from_investing(url)

def get_jkm_price():
    """
    Получает цену на СПГ (LNG JKM) с Investing.com
    :return: Цена в $/MMBtu или None
    """
    url = "https://ru.investing.com/commodities/lng-japan-korea-marker-platts-futures"
    return get_price_from_investing(url)

if __name__ == "__main__":
    print("Парсим данные с Investing.com...")
    ttf_price = get_ttf_price()
    print(f"Цена природного газа (TTF): {ttf_price} €/МВт·ч")

    carbon_price = get_carbon_price()
    print(f"Цена на CO₂ (EU ETS): {carbon_price} €/тонна")

    jkm_price = get_jkm_price()
    print(f"Цена на СПГ (LNG JKM): {jkm_price} $/MMBtu")
