# Clean Architecture Project in Python

This project is inspired by Programador Lhama playlist about clean architecture. The playlist shows the guidelines and practices described by Robert C. Martin.

Follow this link to the [Clean Architecture by Programador Lhama](https://www.youtube.com/watch?v=2nvbgwFE_0Y&list=PLAgbpJQADBGK0opZ8ZuDX3zDjQck_QKMy) playlist.

# Introduction

Clean Architecture is a way to organize code so it's easier to understand, test, and maintain. It uses separation of responsibilities and interdependence of frameworks, databases, and user interfaces.

# Project Structure

```
/src
  /domain
    - entities
    - repositories
    - usecases
  /data
    - repositories
    - models
    - datasources
  /presentation
    - controllers
    - views
    - viewmodels
```

- Domain: Store business rules and entities.
- Data: Repository and data source implementations.
- Presentation: Visualization layer, including controllers and user interface.
