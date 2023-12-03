# Guidelines

1. **Security: Authentication and Authorization**

   - _Requirement:_ The web API must enforce user authentication and authorization for all endpoints using industry-standard protocols (e.g., OAuth 2.0).
   - _Reference:_ [OWASP Authentication Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html), [OWASP Authorization Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html)

2. **Reliability: Availability**

   - _Requirement:_ The web API will be available 99.99% of the time per day under the maximum load of 10 million concurrent users.
   - _Reference:_ [ISO/IEC 25010:2011](https://www.iso.org/standard/35733.html)

3. **Performance: Response Time**

   - _Requirement:_ The API endpoints should respond to 95% of requests within 200 milliseconds under normal operating conditions.
   - _Reference:_ [ISO/IEC 25010:2011](https://www.iso.org/standard/35733.html)

4. **Maintainability: Code Documentation**

   - _Requirement:_ The codebase must have comprehensive documentation, covering API endpoints, data models, and code structure, following industry best practices.
   - _Reference:_ [GitHub Contributor Guidelines](https://docs.github.com/en/contributing)

5. **Scalability: Concurrent Users**
   - _Requirement:_ The web API must support a scalable architecture, capable of handling a linear increase in concurrent users, up to 10 million, without compromising performance.
   - _Reference:_ [ISO/IEC 25010:2011](https://www.iso.org/standard/35733.html)

# References

1. [OWASP Authentication Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html)
2. [OWASP Authorization Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html)
3. [ISO/IEC 25010:2011](https://www.iso.org/standard/35733.html)
4. [GitHub Contributor Guidelines](https://docs.github.com/en/contributing)
5. [ISO/IEC 25010:2011](https://www.iso.org/standard/35733.html)

# Project Structure

## Controller (`src.controller`):

- Contains route definitions and controller logic.
- Routes are organized using Flask's Blueprints (`books_bp`).

## Model (`src.model`):

- Defines the data model (`Book` class).
- Provides a sample in-memory data storage (`books` list).

## Overall Structure:

- The project follows a modular structure, separating concerns between models and controllers.
- The absence of a dedicated 'View' component may imply that the view aspect is tightly coupled with the controller logic in this simple API setup.

## Suggestions for Improvement:

- Introduce a clear separation of concerns by explicitly defining a 'View' component or template engine for rendering responses.
- Consider organizing the project into a more scalable structure if it is expected to grow in complexity (e.g., separate modules for routes, models, views).
- Add unit tests to ensure the reliability and correctness of the API.
