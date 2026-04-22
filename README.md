# Documentación del bot EPG

## Instalación

Para instalar el bot EPG, asegúrate de que tienes Python 3.6 o superior instalado en tu sistema. Luego, ejecuta el siguiente comando para instalar las dependencias necesarias:

```bash
pip install -r requirements.txt
```

## Uso

Puedes utilizar el bot EPG ejecutando el siguiente comando en tu terminal:

```bash
python bot_epg.py
```

Asegúrate de tener configurado el archivo de configuración correcto antes de ejecutar el bot.

## Formato EPG

El formato EPG es el siguiente:

- **Canal:** Nombre del canal de televisión.
- **Título:** Título del programa.
- **Descripción:** Descripción breve del programa.
- **Hora de inicio:** Hora de inicio del programa.
- **Duración:** Duración del programa en minutos.

El EPG se genera en formato XMLTV.

## Configuración de IPTV Smarters

Para configurar IPTV Smarters con el bot EPG, sigue estos pasos:

1. Abre la aplicación IPTV Smarters.
2. Ve a "Configuración" y selecciona "Añadir un nuevo usuario".
3. Introduce los detalles de tu servicio IPTV, incluyendo el nombre de usuario y la contraseña.
4. Selecciona la opción EPG y carga el archivo EPG generado por el bot.

Ahora deberías poder ver los canales y la guía de programas en IPTV Smarters.