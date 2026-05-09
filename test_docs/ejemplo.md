# Guía de Módulo Planning

El módulo de **Planning** es fundamental en GoalBus. Se encarga de generar el cuadrante para cada expedición.

## Configuración Inicial

Para configurar las líneas de transporte, puedes usar la siguiente función en Python:

```python
def configure_route(route_id, origin, dest):
    print(f"Configuring {route_id} from {origin} to {dest}")
```

### Notas Importantes
* La ruta debe ser válida.
* El itinerario se guarda en la base de datos de expediciones.

Revisa la imagen del relevo:
![Esquema de relevo](images/relevo_diagram.png)

[Visita la documentación de GoalDriver](https://goaldriver.docs/es/)
