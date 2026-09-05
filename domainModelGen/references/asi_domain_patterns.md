# Patrones de dominio ASI

Lee esta referencia al evaluar estructuras recurrentes. El catálogo ayuda a encontrar clases, relaciones, atributos y responsabilidades; no fija nombres ni multiplicidades para un caso concreto.

## Patrón fundamental

1. **Colección–Trabajador:** una colección conoce y coordina objetos sobre los que cuenta, calcula o clasifica; cada trabajador conoce o calcula sobre sí mismo. Úsalo para explorar responsabilidades, no para crear una clase “colección” artificial sin significado de dominio.

## Patrones transaccionales

2. **Actor–Participante:** un actor —persona, organización u otro recurso— cumple una participación contextual.
3. **Participante–Transacción:** una persona u organización participa en un evento de negocio.
4. **Lugar–Transacción:** una transacción ocurre o queda vinculada a un lugar relevante.
5. **Ítem específico–Transacción:** una instancia individual participa directamente en una transacción.
6. **Transacción–Detalle de transacción:** una transacción agrupa líneas con información propia.
7. **Transacción–Transacción subsiguiente:** eventos de negocio se encadenan temporalmente; las multiplicidades dependen de conversiones, entregas o pagos parciales.
8. **Detalle–Detalle subsiguiente:** las líneas de transacciones sucesivas deben relacionarse individualmente.
9. **Ítem–Detalle de transacción:** el detalle referencia una descripción o tipo de ítem.
10. **Ítem específico–Detalle de transacción:** el detalle referencia la instancia individual involucrada.
11. **Ítem–Ítem específico:** separa información compartida de cada ejemplar concreto.
12. **Asociación–Otra asociación:** dos objetos se conocen mediante una asociación sin datos ni historia propios del vínculo; uno puede necesitar contar, calcular o clasificar otras asociaciones relacionadas. No implica reificar la asociación.
13. **Ítem específico–Jerarquía de ítem:** una instancia se vincula con una clasificación jerárquica relevante.

## Patrones de agregación

14. **Contenedor–Contenido:** un objeto contiene otros elementos.
15. **Contenedor–Detalle de contenedor:** el contenedor administra objetos detalle con información como cantidad o estado y responsabilidades de cálculo/clasificación. Aplicalo al contenedor más pequeño relevante del dominio, no como clase de asociación automática.
16. **Grupo–Miembro:** miembros participan de una agrupación sin perder identidad independiente.
17. **Todo–Parte:** un objeto está formado por partes identificables.
18. **Compuesto de parte–Parte:** una parte compuesta se desglosa a su vez.
19. **Paquete–Componente de paquete:** agrupación y componentes de un paquete lógico o físico del dominio.

## Patrones de plan

20. **Plan–Paso:** una definición contiene pasos previstos.
21. **Plan–Ejecución de plan:** la definición se diferencia de cada ejecución real.
22. **Paso–Ejecución de paso:** cada paso previsto puede tener ocurrencias realizadas.
23. **Ejecución de plan–Ejecución de paso:** una ejecución reúne los pasos efectivamente realizados.
24. **Plan–Versión de plan:** se conservan distintas versiones de una definición.

## Cómo decidir

Para cada patrón candidato documenta:

1. evidencia del problema que resuelve;
2. clases del dominio que asumirían los roles;
3. multiplicidades sustentadas y preguntas pendientes;
4. atributos o responsabilidades sugeridos por el patrón, marcados como derivados hasta validación;
5. consecuencias de aplicarlo o no aplicarlo.

No combines patrones por similitud verbal. En particular:

- Actor–Participante no obliga a una jerarquía `Persona–Rol`.
- Ítem–Ítem específico requiere que el negocio diferencie tipo e instancia.
- Transacción–Detalle no determina por sí sola composición ni cantidad mínima.
- Estado con historial no forma parte automática de este catálogo; surge de requisitos de vigencia o auditoría.
- Los patrones GRASP y GoF corresponden al diseño/asignación de responsabilidades de software, no al modelo conceptual del dominio.
