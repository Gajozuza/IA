

# Informe Técnico de Propuesta de Infraestructura de Red para Campus Universitario

## 1. Infraestructura Física Propuesta

### a. Descripción General del Entorno

El diseño se enfoca en un **Campus Universitario de tamaño mediano** que interconecta tres edificios principales (Administrativo/Docente, Aulas/Auditorio, y Residencial/Comedor). El total de usuarios estimados es de **1,500** (1,400 estudiantes y 100 personal), requiriendo conectividad de alta velocidad (mínimo 1 Gbps) y baja latencia para soportar aplicaciones críticas (ERP, e-learning, laboratorios virtuales) y servicios de alta densidad (Wi-Fi en aulas).

### b. Esquema Básico y Topología

Se implementará una **Topología Jerárquica de Tres Capas** (Núcleo, Distribución y Acceso) para garantizar escalabilidad, rendimiento y redundancia.

* **Núcleo (Core):** Ubicado en el Edificio Administrativo (A). Interconecta los tres edificios y el *router* perimetral/Firewall de salida a Internet.
* **Distribución:** Agrega el tráfico de los switches de Acceso en cada edificio, implementa políticas de seguridad (VLANs, QoS) y enrutamiento interno.
* **Acceso:** Conecta los dispositivos finales y los Puntos de Acceso (APs) en cada piso.



### c. Elementos Físicos (Hardware Pasivo)

| Elemento Físico | Descripción y Función |
| :--- | :--- |
| **Racks de 42U** | Gabinetes ubicados en cuartos de telecomunicaciones (closets de cableado) para alojar switches y paneles de parcheo, asegurando orden y seguridad. |
| **Canalizaciones** | **Ductos subterráneos** para el *backbone* de fibra óptica inter-edificios. **Bandejas portacables** para el cableado horizontal en falsos techos. |
| **Cableado Estructurado** | **Acceso:** Cable UTP **Categoría 6A (10 Gbps)** para el cableado horizontal. **Backbone:** **Fibra Óptica Monomodo** (mayor distancia y capacidad) para interconectar los edificios. |
| **Puntos de Acceso (APs)** | Dispositivos **Wi-Fi 6 (802.11ax)** distribuidos para alta densidad de usuarios en aulas y zonas comunes. Alimentados por PoE. |

***

## 2. Medios y Tecnologías de Transmisión

### a. Medios de Transmisión y Justificación

| Medio Seleccionado | Clasificación | Justificación Técnica de la Elección |
| :--- | :--- | :--- |
| **UTP Cat. 6A** | Guiado (Cobre) | **10 Gbps a 100m** y soporte de **PoE** (Power over Ethernet). El estándar de acceso actual más económico que asegura la escalabilidad de velocidad futura. |
| **Fibra Óptica Monomodo** | Guiado (Óptico) | **Alta capacidad (40/100 Gbps+)** e **inmunidad a EMI**. Indispensable para el *backbone* inter-edificios (largas distancias) para evitar cuellos de botella y asegurar la fiabilidad. |
| **Wi-Fi 6 (802.11ax)** | No Guiado (RF) | **Alta Densidad (OFDMA/MU-MIMO):** Esencial para manejar la gran cantidad de dispositivos concurrentes en aulas, mejorando la eficiencia y el rendimiento por usuario. |

### b. Tecnologías y Ventajas

* **Tecnología Ethernet/PoE:** Permite la alimentación eléctrica y la transmisión de datos a través del mismo cable UTP. **Ventaja:** Simplifica la instalación de APs, cámaras y Teléfonos IP, reduciendo el costo total de despliegue.
* **Tecnología Fibra Óptica:** Transmisión por pulsos de luz. **Ventaja:** Proporciona el ancho de banda masivo y la baja latencia necesarios en el *Core* para manejar el tráfico agregado de todo el campus.

***

## 3. Dispositivos de Interconexión

| Dispositivo | Función Principal | Configuración General |
| :--- | :--- | :--- |
| **Switches de Núcleo (L3)** | **Agregación de Tráfico** y **Enrutamiento Inter-VLAN** a velocidad de cable. | Conexiones de Fibra de 10 Gbps/40 Gbps hacia Distribución y Firewall/Router. |
| **Switches de Distribución (L3)** | **Control de Tráfico** (QoS, ACLs) y **Segmentación** (VLANs). | Enlaces de Fibra de 10 Gbps al Núcleo y enlaces UTP de 1/10 Gbps a la Capa de Acceso. |
| **Switches de Acceso (L2/PoE)** | **Conectividad a Dispositivos Finales** (Escritorios, APs). | Puertos de 1 Gbps a los usuarios con soporte PoE. Uplink de 10 Gbps a Distribución. |
| **Router Perimetral** | **Conexión al ISP** y enrutamiento externo. | Enlace de 1 Gbps al ISP. Conectado al Firewall y al Núcleo. |
| **Firewall (NGFW)** | **Seguridad Perimetral Profunda** (Inspección de Tráfico, IPS). | Ubicado lógicamente entre el Router y el Switch de Núcleo para inspeccionar todo el tráfico entrante/saliente. |

***

## 4. Cálculo y Dimensionamiento de Enlaces

### a. Determinación del Ancho de Banda Requerido

El cálculo se basa en el número de usuarios, un factor de concurrencia y la aplicación de un factor de sobredimensionamiento (1.5x) para picos de tráfico.

| Tipo de Usuario | Cantidad | BW por Usuario (Mbps) | Concurrencia | BW Total Requerido |
| :--- | :--- | :--- | :--- | :--- |
| Estudiantes | 1,400 | 1 Mbps | 30% (420 concurrentes) | 420 Mbps |
| Personal | 100 | 3 Mbps | 80% (80 concurrentes) | 240 Mbps |
| **BW Agregado Mínimo** | **1,500** | - | - | **660 Mbps** |

$$BW_{Recomendado} = BW_{Mínimo} \times Factor_{Crecimiento} = 660 \text{ Mbps} \times 1.5 = 990 \text{ Mbps}$$

### b. Propuesta de Dimensionamiento Final

| Enlace | Capacidad Propuesta | Justificación |
| :--- | :--- | :--- |
| **Salida a Internet (ISP)** | **1 Gbps (1000 Mbps)** | Capacidad estándar, coste-eficiente, y superior a los 990 Mbps calculados para manejar picos y crecimiento. |
| **Backbone Inter-Edificios** | **10 Gbps** | Necesario para evitar cuellos de botella en el tráfico interno (servidores, laboratorios) que excede el BW de salida a Internet. |
| **Acceso a Escritorio/AP** | **1 Gbps** | Velocidad estándar para la mayoría de los dispositivos actuales, garantizada por el cableado Cat. 6A. |

***

## 5. Alternativas Descartadas y Justificación

La elección de la infraestructura propuesta se realizó tras descartar otras opciones que, aunque técnicamente viables, no cumplían con los requisitos de rendimiento, escalabilidad o costo a largo plazo del campus.

### a. Alternativas de Cableado Descartadas

| Alternativa Descartada | Razón de Descarte (Costo/Rendimiento) |
| :--- | :--- |
| **UTP Cat. 5e/Cat. 6 para Acceso** | **Falta de Futuro:** Solo garantiza 1 Gbps. El costo inicial es ligeramente menor que Cat. 6A, pero la necesidad de **reemplazarlo** cuando se adopten APs o estaciones de trabajo de 2.5 Gbps o 5 Gbps (tendencia futura) resultaría en un **Costo Total de Propiedad (TCO) mucho mayor**. |
| **Fibra Óptica Multimodo (OM3/OM4) para Backbone** | **Limitación de Distancia y Escalabilidad:** Aunque es más barata y fácil de terminar que la monomodo, su capacidad para 100 Gbps solo se logra en distancias cortas (ej., menos de 150-300m). La **monomodo** es la única que garantiza la capacidad masiva y la distancia requerida para un verdadero *backbone* de campus, ofreciendo mejor **escalabilidad**. |

### b. Alternativas de Tecnologías y Diseño Descartadas

| Alternativa Descartada | Razón de Descarte (Confiabilidad/Gestión) |
| :--- | :--- |
| **Wi-Fi 5 (802.11ac)** | **Bajo Rendimiento en Alta Densidad:** Carece de las tecnologías **OFDMA** y **MU-MIMO** en *uplink* que son cruciales para manejar eficientemente la **alta concurrencia** de estudiantes en aulas. El rendimiento efectivo por usuario se degradaría rápidamente, comprometiendo los servicios de e-learning. |
| **Enlaces Inalámbricos Punto a Punto para Inter-edificios** | **Vulnerabilidad y Latencia:** Aunque más rápido de implementar que la fibra, estos enlaces son **susceptibles a las condiciones climáticas** (lluvia, niebla) e interferencias de radiofrecuencia (RF). La fibra óptica, por su inmunidad a EMI, fue la elegida para la **fiabilidad del 100%** requerida en el *backbone* académico. |
| **Diseño de Red Plana (sin capa de Distribución)** | **Falta de Segmentación y Crecimiento:** Conectar todos los switches de acceso al *Core* directamente (sin una capa de Distribución) elimina la capacidad de aplicar políticas de seguridad (ACLs/VLANs) de forma granular y eficiente, aumentando la congestión de *broadcast* y **dificultando la gestión y el diagnóstico de fallas** en una red tan grande. |