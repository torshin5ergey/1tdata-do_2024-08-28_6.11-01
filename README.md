# Итоговая аттестация. Задание 1

Торшин Сергей

## Запуск 
1. Загрузить репозиторий
    ```bash
    git clone https://github.com/torshin5ergey/1tdata-do_2024-08-28_6.11-01.git
    ```
2. Перейти в директорию репозитория
    ```bash
    cd 1tdata-do_2024-08-28_6.11-01
    ```
3. Запуск контейнера
    - Без аргумента (по умолчанию приветствие для User)
        ```bash
        docker run --rm torshin5ergey/1tdata-do_2024-08-28_6.11-01-app
        ```
        ![](screenshot_01.jpg)
    - С аргументом
        ```bash
        docker run --rm torshin5ergey/1tdata-do_2024-08-28_6.11-01-app Alice
        ```
        ![](screenshot_02.jpg)

Ссылка на образ Python-приложения в Docker Hub: [torshin5ergey/1tdata-do_2024-08-28_6.11-01-app](https://hub.docker.com/repository/docker/torshin5ergey/1tdata-do_2024-08-28_6.11-01-app/general)
