🧭 GaiaMind · Product Brief


GaiaMind es la primera app web inteligente que convierte hábitos cotidianos en acciones sostenibles. Conectando APIs climáticas, autenticación por Google y una base de datos en la nube, permite a los usuarios registrar sus acciones ecológicas y visualizar su impacto en tiempo real. Diseñada con un enfoque gamificado, promueve hábitos verdes con métricas personalizadas y una interfaz minimalista accesible desde cualquier navegador.

---

🎯 Propósito

GaiaMind impulsa la adopción de hábitos sostenibles a través de una experiencia amigable, conectada a fuentes externas y ejecutada en infraestructura cloud. Su misión es democratizar la sostenibilidad personalizada usando tecnología ética, visual y educativa.

---

👥 Público Objetivo

- Jóvenes/adultos urbanos entre 18 y 40 años interesados en reducir su impacto ambiental.
- ONGs, escuelas y municipios que buscan una herramienta educativa y visual.

---

🧩 Funcionalidades Clave

| Funcionalidad                          | Descripción                                                                                |
|---------------------------------------|---------------------------------------------------------------------------------------------|
| 📝 Registro de acciones verdes        | Formulario para ingresar hábitos sostenibles y almacenarlos por usuario.                   |
| 🌦️ Recomendaciones inteligentes       | Sugerencias diarias basadas en clima/localización. (base lista para integrar WeatherAPI)   |
| 📈 Visualización del impacto          | Gráficos y barras de progreso generados con Chart.js, actualizados en tiempo real.         |
| 🔐 Autenticación con Google           | Login seguro mediante OAuth2 para mostrar historial personalizado.                         |
| 🌍 Mapa interactivo                   | Leaflet.js detecta ubicación actual y permite recomendaciones geolocalizadas.              |
| 🏆 Gamificación ecológica (prototipo) | Sistema visual de niveles verdes según acciones realizadas.                                |

---


| Componente         | Tecnología                            |
|--------------------|----------------------------------------|
| Hosting cloud      | DigitalOcean Droplet (Ubuntu)         |
| Backend            | Python + Flask                        |
| Base de datos      | SQLite local (lista para PostgreSQL)  |
| Frontend           | HTML5 + Bootstrap + Chart.js + Leaflet|
| Autenticación      | Flask-Dance (OAuth2 via Google)       |
| Variables seguras  | `.env` gestionado con `python-dotenv` |
| Logs               | `log.txt` + `tail` en consola         |

---

🌐 Demo en la nube

- 🌍 URL del proyecto: http://138.197.42.115:5000

---

📌 Propuesta de Valor

- Visualización inmediata del impacto personal y colectivo 🌿
- Recomendaciones adaptadas al contexto y clima ☁️
- Experiencia gamificada para mantener la motivación 🎯
- Compatible con dispositivos móviles, sin instalación 📱
- Ecosistema abierto y replicable para instituciones u ONGs 🏫

---

💡 Clasificación del Proyecto

API + Backend + Frontend

🔧 Backend
Construido en Flask (Python), maneja lógica de negocio, autenticación y reglas
🌍 API
Conexión con WeatherAPI para recomendaciones inteligentes contextualizadas
🖥️ Frontend
Interfaz web con HTML, Bootstrap, Leaflet.js y Chart.js
☁️ Infra
Desplegado en DigitalOcean con Droplet Ubuntu + base SQLite (PostgreSQL-ready)
🔐 Auth
Login con Google mediante Flask-Dance y OAuth2


---

Instalación local

1. Clonar este repositorio:

```bash
git clone https://github.com/tu-usuario/gaia-mind.git
cd gaia-mind

---

© Créditos

Desarrollado por **Lucas A. Dávila**  
2025 · GaiaMind 🌍
