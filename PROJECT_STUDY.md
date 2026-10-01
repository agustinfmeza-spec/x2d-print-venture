# New-Project Study — repuestos para autos anteriores al 2000
*Estudio para el X2D Print Venture. Foco: Honda, BMW y Alfa Romeo (las marcas que conocés), más repuestos generales de autos que pierden soporte y aftermarket. Incluye la idea de las polainas E36 y molduras estilo M de tu amigo.*

> **Cómo leer esto.** La demanda local la tomo de tu experiencia: estos repuestos se venden mucho acá (el ejemplo que diste es Alfa Romeo). Los casos de afuera son **ejemplos del método, no competencia**. No tengo precios locales: lo marcado **(VERIFY)** se confirma con 30 minutos en Mercado Libre, Instagram o un club de autos antes de gastar filamento. El ranking es un modelo de puntaje (`opportunities.py`), no un pronóstico.

---

## 1. Por qué autos anteriores al 2000
- **Los plásticos ya cumplieron su vida:** después de 25+ años de sol, calor y uso, las piezas interiores chicas se vuelven quebradizas y se rompen: clips, perillas, marcos de interruptores, rejillas, manijas, tapas.
- **El soporte se fue:** las marcas dejan de fabricarlas y el aftermarket solo cubre lo que se vende en volumen. Lo que queda sin cobertura es justo lo que una impresora hace bien: **piezas chicas, ajuste exacto, pocas unidades**.
- **Tu ventaja:** conocés estas marcas y sus autos, tenés contacto con clubes y dueños, y podés filmar la pieza instalada. Eso es difícil de copiar.
- **Demanda local:** vos ya viste que estos repuestos se venden bien, sobre todo Alfa Romeo. Lo tratamos como punto de partida y lo medimos con tus propias consultas (ver sección 5).

---

## 2. Ejemplos de afuera (el método, no la competencia)
Muestran que el modelo "imprimir lo que ya no se consigue" funciona y de qué formas se hace.

| Ejemplo | Qué enseña | Fuente |
|---|---|---|
| **Porsche Classic** | Imprime repuestos de autos fuera de producción (plásticos en SLS, metal en SLM); unos 9 repuestos impresos dentro de un catálogo de ~52.000, como la palanca de embrague del 959. Valida la categoría "repuesto discontinuado". | [Porsche Newsroom](https://newsroom.porsche.com/en/company/porsche-classic-3d-printer-spare-parts-sls-printer-production-cars-innovative-14816.html) |
| **Mercedes-Benz Classic** | Base impresa del espejo interior del 300 SL, vendida por un service partner. | [VoxelMatters](https://www.voxelmatters.com/mercedes-3d-printed-spare-parts/) |
| **Vendedores de Etsy** | Tiendas chicas venden reproducciones: bezels de ventilación del Chevy C10 (1964–66), portavasos y cenicero del Audi A4 B6/B7, molduras del BMW E30. | [Etsy](https://www.etsy.com/market/car_part_3d_printed) |
| **Freshmade 3D** | Piezas difíciles de conseguir para clásicos, aliada con un taller de restauración. Modelo: *asociarse con quien restaura*. | [Wilson Auto](https://wilsonauto.com/cant-find-a-classic-car-part-no-problem-make-it-with-a-3d-printer/) |
| **HV3DWorks** | Otro taller chico de reproducciones. | [hv3dworks.com](https://hv3dworks.com/) |

**Lo que copiamos:** nicho por marca y modelo, ajuste verificado en el auto, alianza con talleres y clubes, y fotos de la pieza instalada. Un blog que encontré habla de ingresos de siete cifras con este negocio; es contenido de marketing y no usé esos números.

---

## 3. Marcas y modelos objetivo (la lista vive en el dashboard)
En la app, la pestaña **Parts targets** tiene estas marcas con un estado por línea (idea, validating, designed, printed, selling, dropped) y una nota. El Log ahora pide **marca y modelo/año** en cada lead, y el dashboard muestra qué marca trae trabajo.

| Marca | Modelos (antes del 2000) | Tipos de pieza a revisar |
|---|---|---|
| **Alfa Romeo** | 33, 145, 146 · 155, 156 (primera gen), 164 · Spider y GTV 916 | Rejillas de ventilación, tapas de manijas y tiradores, marcos de interruptores, piezas de consola, clips |
| **BMW** | E30 · E36 · E34, E28 | Clips de puertas y molduras, rejillas, tapas de interruptores, clips de levantavidrios, tapas de extremo |
| **Honda** | Civic EG/EK, Integra DC2 · Accord CD/CE, Prelude · CRX, Civic EF | Perillas de climatizador y radio, marcos de interruptores, clips, tapas de consola y guantera |
| **Generales** | Cualquier auto anterior al 2000 | Kits de clips, pasacables, tapas de caja de fusibles, tapas de brazos de limpiaparabrisas, soportes que no son de presión |

> Estos son **tipos de pieza que suelen fallar**, no un listado verificado. Para cada modelo, pedí a dueños y administradores de club que nombren las piezas exactas que no consiguen y cargalas en la nota.

**Otras marcas que suelen perder soporte y podrían sumarse:** Fiat/Lancia, Peugeot 205/405, Renault 9/11/19/21, Ford Escort/Sierra, VW Golf Mk3, Mercedes W124/W201.

---

## 4. Ranking de ideas
Puntaje 1–5 en demanda local, ajuste a la X2D, margen, vacío de oferta (piezas que el mercado perdió), esfuerzo, sinergia con tus marcas y red, y riesgo. Pesos 20/20/20/15/10/10/5 en `opportunities.py`.

| # | Idea | Material | Tier | Puntaje |
|--|--|--|--|--|
| 1 | Alfa Romeo 33/145/155/164/916: interior trim, vents, handles | ASA/ABS | B/C | 4.75 |
| 2 | BMW E30/E36/E34: interior clips, trim, regulator clips | ASA/PETG | A/B | 4.50 |
| 3 | Honda Civic/Integra/Accord/CRX: interior plastics | ASA/PETG | A/B | 4.50 |
| 4 | General clip & retainer kits (any pre-2000 car) | ASA/PETG | A | 4.15 |
| 5 | E36 hardware kits: skirt brackets, molding clips, end caps | ASA/PETG+PA6-CF | B | 4.10 |
| 6 | Camera car-mount accessories (Rawspeed) | PA6-CF/PETG | B/C | 4.10 |
| 7 | General non-pressure brackets and mounts | PA6-CF/ASA | B/C | 4.05 |
| 8 | Aux-light brackets / mate mount | PA6-CF | C | 4.05 |
| 9 | Track-day mounts (camera, logger, dash) | PA6-CF | C | 3.90 |
| 10 | Model-specific console/cupholder inserts | ASA | B | 3.90 |
| 11 | UTN / SGS tooling, jigs, prototypes | PETG/PA6-CF | B/C | 3.85 |
| 12 | Model-specific phone mounts | ASA | B | 3.85 |
| 13 | Custom badges/emblems (own designs) | ASA/PETG | A/B | 3.75 |
| 14 | Patterns for casting rare bodies and panels | PLA/PETG+finish | C | 3.60 |
| 15 | Gauge pods / aux gauge housings | ASA | B | 3.55 |
| 16 | STL licensing (Printables/Cults) | digital | - | 3.25 |
| 17 | M-style side moldings in segments | TPU/ASA | B | 3.15 |
| 18 | Full E36 side skirts, segmented FDM | ASA | C | 2.40 |

**Cómo leerlo**
- **Primeros tres lugares:** las piezas interiores de Alfa Romeo, BMW y Honda. Son chicas, en ASA o PETG, con demanda que ya conocés y contenido que podés filmar en un auto real.
- **Cuarto lugar:** kits de clips y retenes para cualquier auto anterior al 2000. Cuesta poco, rota rápido y sirve de puerta de entrada.
- **Piezas que sostienen cámaras, luces o herramientas en un auto en movimiento:** diseñalas con cable de seguridad e indicá sus límites. No imprimas piezas de frenos, dirección ni cinturones.
- **Cambiá los pesos o puntajes** en `opportunities.py` si tus prioridades son otras.

---

## 5. La idea de tu amigo: polainas E36 y molduras estilo M
**Polainas completas: mala opción para una sola X2D**
- La cama es de 256×256×260 mm. Una polaina E36 mide más o menos 1,6–1,9 m **(VERIFY)**, así que son **7–8 segmentos por lado**, con uniones, relleno y lijado.
- Estimación (no medida): 8–14 h por segmento, unas **120–200 h de impresión por par**. Tu capacidad realista es ~200 h/mes, o sea 60–100% de un mes por un solo par.
- Piso de precio: la cuota exige que la máquina gane **al menos ARS 2.000 por hora** solo para cubrirse (395.000 / ~200 h). Un par de 160 h necesitaría **ARS 650 mil o más**, sin pintura ni tu trabajo. Compará con lo que paga un cliente por un par importado o de fibra **(VERIFY)**.
- El acabado (imprimación, lijado, pintura) cuesta muchas horas que la impresora no hace por vos.

**Donde sí conviene imprimir con tu amigo**
1. **Kits de herrajes:** soportes, clips, tapas de extremo y plantillas de alineación para polainas y molduras. Son chicos, calzan justo y suelen faltar o estar rotos en autos viejos.
2. **Piezas patrón:** imprimís y terminás el master, sacás moldes de silicona y colás o laminás copias. Un master sirve para muchas copias.
3. **Autos locales sin aftermarket:** para modelos sin polainas de ABS o fibra, un set segmentado a medida puede ser un producto aparte, cotizado por trabajo.
4. **Molduras estilo M:** una tira larga es sobre todo un problema de uniones y acabado. Probá una sola tira de prueba, en TPU o ASA, antes de ofrecerla.

**Cómo trabajar juntos:** vos imprimís y terminás herrajes y patrones; él vende, instala y se ocupa de la pintura. Probalo en **un solo auto** y filmalo para Rawspeed. Dejen por escrito antes del primer trabajo quién es dueño de los diseños, quién compra el material y quién responde por reclamos.

---

## 6. Materiales para estos proyectos (rango de la X2D)
| Material | Sirve para | Dónde se usa | Ojo con |
|---|---|---|---|
| PLA/PLA+ | Patrones, prototipos | Piezas patrón, pruebas de ajuste | Se ablanda cerca de 55 °C: nunca dentro de un auto caliente |
| PETG | Uso general, plantillas | Clips, plantillas, kits de retenes | Calor moderado solamente |
| ASA/ABS | Interior y exterior, UV y calor | Piezas interiores, polainas, molduras, soportes | Requiere la cámara cerrada y ventilación |
| TPU 95A | Sellos, molduras flexibles | Molduras estilo M, tapas flexibles | Lento; probar con el AMS |
| PA6-CF / PAHT-CF | Soportes, montajes, bajo el capot | Herrajes con carga, soportes de luces | Filamento seco y boquilla endurecida |
| Soporte para PA/PET o ABS | Voladizos en piezas de ingeniería | Piezas con socavones | Nunca PLA como soporte |
| PC, PC-CF, PPS-CF | Fuera del rango de la X2D | – | Evitá piezas que los necesiten |

Si tu "FDM Materials Engineering Reference" difiere de esta tabla, pegala en un chat nuevo y la alineo.

---

## 7. Validar antes de comprar filamento (2 semanas, sin impresora)
| Paso | Qué hacer | Sirve si |
|---|---|---|
| 1 | Preguntá en 3 clubes o grupos (Honda, BMW, Alfa Romeo) qué piezas no consiguen | 5 o más pedidos concretos por marca |
| 2 | Encuesta en stories: "¿Qué pieza de tu Honda, BMW o Alfa no se consigue más?" | 20 o más respuestas con piezas específicas |
| 3 | Mirá en Mercado Libre los precios que se ven para esas piezas | Al menos 3 referencias de precio por pieza |
| 4 | Cotizá 3 piezas pedidas: material + horas × ARS 2.000 + acabado | Precio de al menos el doble del costo de material |
| 5 | Preventa de 3 piezas con descuento | 3 señas |

Cargá cada pedido en el dashboard (Log data) con marca, modelo/año, fuente y tier, y cada línea de la pestaña **Parts targets** con su estado.

---

## 8. Riesgos específicos
| Riesgo | Cómo se maneja |
|---|---|
| Logos de marca (óvalo BMW, rayas M, escudo Alfa, H de Honda) | No copies logos ni la marca tricolor M. Vendé formas "compatibles con" y tus propios diseños |
| Derechos de diseño en carrocería | Revisá si hay registros locales sobre diseños de polainas con marca **(VERIFY)** |
| Variaciones entre años y versiones | Medí el auto real; vendé por año y modelo con guía de ajuste |
| El acabado se come el margen | Vendé piezas crudas o con imprimación y que otro pinte |
| Calor y UV | ASA o PA6-CF en exterior y en interior caliente; probá una muestra al sol y fotografiala |
| Piezas de seguridad | Nada de frenos, dirección, cinturones ni refrigeración a presión |
| Dependencia de tu amigo | Reparto por escrito, cola de pedidos y plazo fijo |

---

## 9. Próximos pasos
1. Hacé los pasos 1–3 de la validación esta semana.
2. Con las respuestas, completá la nota de cada modelo en **Parts targets** y quedate con las 3 líneas más pedidas.
3. Pedile a tu amigo los años exactos del E36 y las 3 piezas que más le piden.
4. Cuando llegue la impresora, imprimí un kit de herrajes y una pieza patrón, y filmá ambos.

*Archivos: `opportunities.py` (modelo de puntaje) y `opportunities.csv` (salida ordenada).*
