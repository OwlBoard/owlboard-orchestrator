# API Gateway (Orquestador)

Este servicio actúa como el único punto de entrada (API Gateway) para todos los microservicios de backend, usando Nginx como reverse proxy.

## Propósito

-   **Centralización:** Enruta el tráfico a los servicios correctos (`user_service`, `comments_service`, `canvas_service`, `chat_service`).
-   **Abstracción:** Oculta la topología de la red interna. Los frontends solo necesitan conocer esta URL.
-   **Simplificación:** Unifica la API bajo un prefijo `/api`.

## Rutas

-   `http://<host>/api/users/` -> `user_service`
-   `http://<host>/api/comments/` -> `comments_service`
-   `http://<host>/api/canvas/` -> `canvas_service`
-   `http://<host>/api/chat/` -> `chat_service`