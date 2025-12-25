# SauceDemo Autotests Project 🚀

Проект по автоматизации тестирования сайта [Saucedemo](https://www.saucedemo.com/) с использованием современного стека технологий.

## 📊 Статус CI/CD
| Platform | Status | Report |
| :--- | :--- | :--- |
| **GitHub Actions** | ![GitHub](https://github.com/Emir120802/saucedemo-autotests/actions/workflows/run_tests.yml/badge.svg) | [Allure on GitHub](https://emir120802.github.io/saucedemo-autotests/) |
| **GitLab CI** | ![GitLab](https://gitlab.com/emir_02/saucedemo-autotests/badges/main/pipeline.svg) | [Allure on GitLab](https://emir_02.gitlab.io/saucedemo-autotests/) |

## 🛠 Технологии
* **Python** — основной язык разработки.
* **Playwright** — мощный инструмент для управления браузером.
* **Pytest** — фреймворк для организации и запуска тестов.
* **Allure Report** — детальная визуализация результатов тестирования.

## 💡 Особенности проекта
* **Multi-Cloud CI/CD**: Настроены пайплайны как в GitHub Actions, так и в GitLab CI.
* **Page Object Model (POM)**: Чистая архитектура тестов.
* **Auto-reporting**: Скриншоты при падениях прикрепляются к Allure автоматически.
* **Mobile Emulation**: Тестирование мобильной версии (iPhone 14).

## 🚀 Локальный запуск
1. `pip install -r requirements.txt`
2. `playwright install`
3. `pytest`

