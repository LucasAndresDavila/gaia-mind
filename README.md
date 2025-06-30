GaiaMind 🌱

*GaiaMind* es una app web desarrollada en Python que ayuda a las personas a incorporar hábitos sostenibles mediante sugerencias inteligentes, visualizaciones del impacto ecológico y gamificación. Utiliza APIs externas, una arquitectura cloud alojada en DigitalOcean, y tecnologías abiertas.


Qué hace GaiaMind?

- Permite registrar acciones ecológicas diarias (como usar transporte público o reducir residuos).
- Sugiere hábitos sostenibles basados en clima y ubicación, consumiendo una API externa.
- Visualiza tu impacto en un dashboard en tiempo real.
- Gamifica el progreso con puntos y niveles.

Arquitectura

- Frontend: HTML/CSS/JS o Streamlit
- Backend: Python (Flask o FastAPI)
- Base de datos: PostgreSQL
- APIs externas: WeatherAPI (clima), CarbonInterface (huella de carbono)
- Cloud: App desplegada en **DigitalOcean**


Instalación local

1. Clonar este repositorio:

```bash
git clone https://github.com/tu-usuario/gaia-mind.git
cd gaia-mind
