import random
import time

from flask import Flask, render_template, request

app = Flask(__name__)

# Preguntas y respuestas
preguntas = [
    {
        'pregunta': '¿Cuál de los siguientes NO es verdadero?',
        'alternativas': ['a. El dueño del proceso es la persona informada para cada paso del proceso', 'b. Siempre se debe consultar a alguien para cada paso del proceso', 'c. Puede haber más de una persona responsable', 'd. La responsabilidad puede ser compartida'],
        'respuesta_correcta': 'C'
    },
    {
        'pregunta': '¿Qué es esto? "El resultado de llevar a cabo una actividad, seguir un proceso o entregar un servicio de TI"',
        'alternativas': ['a. Una entrada', 'b. Un procedimiento', 'c. Un resultado', 'd. Una instrucción de trabajo'],
        'respuesta_correcta': 'c. Un resultado'
    },
    {
        'pregunta': '¿Quién es responsable de producir evidencia de que las actividades del proceso se han llevado a cabo correctamente, en forma de registros?',
        'alternativas': ['a. Practicante de proceso', 'b. Gerente de proceso', 'c. Dueño del servicio', 'd. Dueño del proceso'],
        'respuesta_correcta': 'a. Practicante de proceso'
    },
    {
        'pregunta': '¿De qué se compone un servicio de TI?',
        'alternativas': ['a. Una combinación de mejores prácticas, resultados y entradas', 'b. Una combinación de mejores prácticas, tecnología de la información y resultados', 'c. Una combinación de tecnología de la información, personas y procesos', 'd. Una combinación de controles, resultados y entradas'],
        'respuesta_correcta': 'c. Una combinación de tecnología de la información, personas y procesos'
    },
    {
        'pregunta': '¿Cuál de estas afirmaciones es / son correctas?\n1. Los servicios internos se entregan entre departamentos o unidades de negocios dentro de la misma organización.\n2. Los servicios externos son aquellos entregados a un cliente externo.',
        'zzz': '1. Los servicios internos se entregan entre departamentos o unidades de negocios dentro de la misma organización.\n2. Los servicios externos son aquellos entregados a un cliente externo.',
        'alternativas': ['a. Ambos', 'b. Ninguna', 'c. Solo 2', 'd. Solo 1'],
        'respuesta_correcta': 'a. Ambos'
    },
    {
        'pregunta': '¿Cuál de las siguientes no es una fuente reconocida de mejores prácticas de TI según ITIL?',
        'alternativas': ['a. Entrenamiento', 'b. Estándares de la industria', 'c. Auditores', 'd. Conocimiento propietario'],
        'respuesta_correcta': 'c. Auditores'
    },
    {
        'pregunta': '¿Cuál de estos no es un tipo de servicio reconocido según ITIL?',
        'alternativas': ['a. Servicio de proveedor', 'b. Habilitación de servicio', 'c. Servicio básico o central', 'd. Mejora de servicio'],
        'respuesta_correcta': 'a. Servicio de proveedor'
    },
    {
        'pregunta': '¿Para qué se utiliza el modelo RACI?',
        'alternativas': ['a. Definición de los requisitos del proceso para un nuevo servicio', 'b. Definir los roles y responsabilidades de un proceso', 'c. Definición de las diferentes responsabilidades del dueño del servicio y del dueño del proceso, del gerente y del practicante', 'd. Evaluación de riesgos para cada elemento de configuración'],
        'respuesta_correcta': 'b. Definir los roles y responsabilidades de un proceso'
    },
    {
        'pregunta': '¿Quién es responsable de garantizar que se asigne la cantidad correcta de personal a los distintos roles dentro del proceso y que comprendan lo que se les exige?',
        'alternativas': ['a. Gerente de proceso', 'b. Dueño del servicio', 'c. Practicante del proceso', 'd. Dueño del proceso'],
        'respuesta_correcta': 'a. Gerente de proceso'
    },
    {
        'pregunta': '¿Cuál de las siguientes es una razón por la cual una organización podría querer adoptar las mejores prácticas de ITIL?',
        'alternativas': ['a. Gestión de servicios de TI y controles presupuestarios', 'b. Asesoramiento en estrategia de negocio', 'c. Asesoramiento en la especificación técnica de infraestructura', 'd. Desarrollo de técnicas de programación'],
        'respuesta_correcta': 'a. Gestión de servicios de TI y controles presupuestarios'
    },
    {
        'pregunta': '¿Cuál de estas afirmaciones no es cierta?',
        'alternativas': ['a. Todo proceso debe tener un gerente de procesos', 'b. Puede haber varios practicantes de procesos para cada proceso', 'c. Puede haber varios dueños de procesos para cada proceso', 'd. Puede haber varios gerentes de procesos para cada proceso'],
        'respuesta_correcta': 'c. Puede haber varios dueños de procesos para cada proceso'
    },
    {
        'pregunta': '¿Quién dice ITIL que es responsable de identificar mejoras en un proceso?\n1. El dueño del servicio.\n2. El gerente de mejora de procesos.\n3. El gerente de procesos.\n4. El dueño del proceso.',
        'alternativas': ['a. 1 y 2 solamente', 'b. Solo 4', 'c. 1, 3 y 4 solamente', 'd. 3 y 4 solamente'],
        'respuesta_correcta': 'd. 3 y 4 solamente'
    },
    {
        'pregunta': '¿Cuántos tipos de proveedores de servicios identifica ITIL?',
        'alternativas': ['a. 4', 'b. 1', 'c. 3', 'd. 2'],
        'respuesta_correcta': 'c. 3'
    },
    {
        'pregunta': '¿Cuál de las siguientes no es una de las responsabilidades del dueño de un servicio?',
        'alternativas': ['a. Comunicarse con el cliente según sea necesario en todas las cuestiones relacionadas con la prestación del servicio', 'b. Representando el servicio en toda la organización y asistiendo a reuniones de revisión de servicios con el negocio', 'c. Ser el punto de escalamiento (notificación) para incidentes mayores que afectan el servicio', 'd. Diseñar las métricas para el proceso y garantizar que proporcionen la información necesaria para juzgar la efectividad y la eficiencia del proceso'],
        'respuesta_correcta': 'd. Diseñar las métricas para el proceso y garantizar que proporcionen la información necesaria para juzgar la efectividad y la eficiencia del proceso'
    },
    {
        'pregunta': '¿Cuál de estos no es una característica de un proceso?',
        'alternativas': ['a. Responde a un disparador', 'b. Entrega funciones', 'c. Es medible', 'd. Entrega un resultado específico'],
        'respuesta_correcta': 'b. Entrega funciones'
    },
    {
        'pregunta': '¿Cuál de estas afirmaciones describe un proveedor de servicios de TI?',
        'alternativas': ['a. Una función que proporciona controles para la infraestructura de TI', 'b. Un proveedor de servicios externo que entrega componentes de servicios', 'c. Un proveedor de servicios que proporciona servicios de TI a clientes internos o externos', 'd. Una unidad de negocios responsable de los procesos de TI'],
        'respuesta_correcta': 'c. Un proveedor de servicios que proporciona servicios de TI a clientes internos o externos'
    },
    {
        'pregunta': '¿Cuál de las siguientes es la descripción correcta de un servicio?',
        'alternativas': ['a. Entrega valor a los clientes, sin la propiedad de costos y riesgos específicos', 'b. Investiga la causa subyacente de los problemas', 'c. Restaura las operaciones normales tan pronto como sea posible', 'd. Monitorea los objetivos de acuerdo a las obligaciones contractuales'],
        'respuesta_correcta': 'a. Entrega valor a los clientes, sin la propiedad de costos y riesgos específicos'
    },
    {
        'pregunta': '¿Qué rol debería actualizar la documentación del proceso después de un cambio?',
        'alternativas': ['a. El gerente de cambio', 'b. El gerente del conocimiento', 'c. El dueño del proceso', 'd. El gerente del proceso'],
        'respuesta_correcta': 'c. El dueño del proceso'
    },
    {
        'pregunta': '¿Qué significa RACI?',
        'alternativas': ['a. Responsable, Aprobador, Consultado, Informado', 'b. Revisar, Autorizar, Consultar, Informar', 'c. Responsable, Aprobador, Consultado, Involucrado', 'd. Registrado, Evaluado, Consultado, Informado'],
        'respuesta_correcta': 'a. Responsable, Aprobador, Consultado, Informado'
    },
    {
        'pregunta': '¿Cuál de las siguientes actividades debe emprender el dueño de un servicio?\n1. Representar un servicio específico en toda la organización.\n2. Actualizar la base de datos de errores conocidos con detalles de los errores que se han identificado para el servicio\n3. Asistir a la reunión del CAB para discutir los cambios en el servicio\n4. Asistencia a revisiones de servicio con la empresa.',
        'alternativas': ['a. 1, 3 y 4 solamente', 'b. Todas las alternativas', 'c. 1 y 2 solamente', 'd. 1, 2 y 3 solamente'],
        'respuesta_correcta': 'a. 1, 3 y 4 solamente'
    },
    {
        'pregunta': 'ITIL recomienda que comprenda y documente el Perfil de los Patrones de Actividad de Negocio (PBA). ¿Cuál de estos representa las cuatro cosas que debe capturar sobre cada perfil de PBA?',
        'alternativas': ['a. Información de gestión, priorización, números de serie de activos de servicio y líneas de base de configuración', 'b. Atributos, números de serie de activos de servicio, priorización y requisitos', 'c. Clasificación, priorización, requisitos y requisitos de activos de servicio', 'd. Clasificación, atributos, requisitos y requisitos de activos de servicio'],
        'respuesta_correcta': 'd. Clasificación, atributos, requisitos y requisitos de activos de servicio'
    },
    {
        'pregunta': '¿Cuál de los siguientes no formaría parte de un acuerdo de nivel de servicio (SLA)?',
        'alternativas': ['a. Descripción del servicio', 'b. Acuerdos de continuidad del servicio', 'c. Horas de servicio', 'd. Definición de estrategia de negocio'],
        'respuesta_correcta': 'd. Definición de estrategia de negocio'
    },
    {
        'pregunta': 'Un servicio consiste en partes constituyentes, todas las cuales deben considerarse como parte del diseño. ¿Cuáles de estos se identifican como parte de la composición del servicio?\n1. Utilidad\n2. Garantía\n3. Recursos\n4.Capacidades',
        'alternativas': ['a. 1, 2 y 4', 'b. 1, 2, 3 y 4', 'c. 3y4', 'd. 1 y 2'],
        'respuesta_correcta': 'b. 1, 2, 3 y 4'
    },
    {
        'pregunta': 'Los requisitos de nivel de servicio (SLR) están relacionados con cuál de los siguientes?',
        'alternativas': ['a. Utilidad', 'b. Registros de configuración', 'c. Garantía', 'd. Registro de cambios'],
        'respuesta_correcta': 'c. Garantía'
    },
    {
        'pregunta': '¿Cuál de estos no es parte de la estructura del portafolio de servicios?',
        'alternativas': ['a. Servicios retirados', 'b. Catálogo de servicios', 'c. Registro de servicio', 'd. Tubería de servicio (pipeline service)'],
        'respuesta_correcta': 'c. Registro de servicio'
    },
    {
        'pregunta': '¿Cuál de estos representa los cinco aspectos principales considerados por el diseño de servicios en el diseño de servicios de calidad?',
        'alternativas': ['a. Arquitectura, paquete de diseño de servicios, estrategia de negocio, plan de transición de servicios y procesos', 'b. Solución, paquete de diseño de servicios, estrategia de negocios, medición y procesos', 'c. Sistemas de gestión de servicios, procesos, medición, estrategia de negocio y planes de preparación operacional del servicio', 'd. Solución, arquitectura, sistemas de gestión, procesos y medición'],
        'respuesta_correcta': 'd. Solución, arquitectura, sistemas de gestión, procesos y medición'
    },
    {
        'pregunta': '¿Cuáles de las siguientes son categorías de proveedores descritas en ITIL?\n1. Estratégico\n2. Operacional\n3. De confianza\n4. De productos básicos (Commodity)',
        'alternativas': ['a.1 y 2 solamente', 'b. Todo lo anterior', 'c. 2, 3 y 4', 'd. 1, 2 y 4'],
        'respuesta_correcta': 'd. 1, 2 y 4'
    },
    {
        'pregunta': '¿Cuál de estos cuatro activos se puede clasificar como un recurso y una capacidad?',
        'alternativas': ['a. Personas', 'b. Organización', 'c. Capital financiero', 'd. Conocimiento'],
        'respuesta_correcta': 'a. Personas'
    },
    {
        'pregunta': 'La disponibilidad se calcula utilizando la fórmula AST-DT / AST × 100. ¿A qué se refieren los términos AST y DT?',
        'alternativas': ['a. AST = objetivo de servicio asumido, DT = tiempo de entrega', 'b. AST = objetivo del servicio de disponibilidad, DT = tiempo de inactividad', 'c. AST = tiempo de servicio acordado, DT = tiempo de inactividad', 'd. AST = tiempo de servicio acordado, DT = tiempo de entrega'],
        'respuesta_correcta': 'c. AST = tiempo de servicio acordado, DT = tiempo de inactividad'
    },
    {
        'pregunta': 'La gestión de disponibilidad considera VBFs. ¿Qué significa VBF?',
        'alternativas': ['a. Visibilidad, beneficios, funcionalidad', 'b. Factores viables de negocio', 'c. Instalaciones vitales de negocios', 'd. Funciones vitales de negocio'],
        'respuesta_correcta': 'd. Funciones vitales de negocio'
    },
    {
        'pregunta': '¿Cuál de estas afirmaciones es correcta sobre el alcance de la gestión del nivel de servicio (SLM)?\n1. El alcance de SLM incluye el rendimiento de los servicios existentes que se proporcionan.\n2. El alcance de SLM incluye la definición de los componentes que conforman los servicios y sus relaciones.\n3. El alcance de SLM incluye la definición de los niveles de servicio requeridos para los servicios planificados.\n4. El alcance de SLM incluye la definición del tipo de cambios para la gestión de cambios',
        'alternativas': ['a. 1, 2, 3 y 4', 'b. 1 y 3', 'c. 2 y 4', 'd. 1, 2 y 3'],
        'respuesta_correcta': 'b. 1 y 3'
    },
    {
        'pregunta': '¿Cuál es el propósito de la etapa de ciclo de vida Estrategia de Servicio?',
        'alternativas': ['a. Identificar los procesos en uso para el ciclo de vida del servicio', 'b. Crear una base de datos de servicios para el ciclo de vida del servicio', 'c. Definir el enfoque estratégico para la gestión del servicio a lo largo del ciclo de vida del servicio', 'd. Definir los objetivos para todos los roles y responsabilidades a lo largo del ciclo de vida del servicio'],
        'respuesta_correcta': 'c. Definir el enfoque estratégico para la gestión del servicio a lo largo del ciclo de vida del servicio'
    },
    {
        'pregunta': '¿Quién define el valor de un servicio?',
        'alternativas': ['a. Gerente de procesos de la Estrategia de Servicio', 'b. Dueño de procesos de la Estrategia de Servicio', 'c. Cliente', 'd. Gerente de Relaciones de Negocio'],
        'respuesta_correcta': 'c. Cliente'
    },
    {
        'pregunta': '¿Cuál de estos es un propósito de la gestión de relaciones de negocio (BRM)?',
        'alternativas': ['a. Establecer una relación entre el proveedor de servicios y el cliente', 'b. Establecer un mecanismo para registrar las solicitudes de servicio del cliente', 'c. Gestionar la financiación de los servicios prestados a un cliente', 'd. Gestionar los servicios prestados a un cliente'],
        'respuesta_correcta': 'a. Establecer una relación entre el proveedor de servicios y el cliente'
    },
    {
        'pregunta': '¿Cuál de estos no forma parte del alcance de la gestión del portafolio de servicios?',
        'alternativas': ['a. Todos los proyectos que el cliente planea entregar', 'b. Todos los servicios que un proveedor de servicios planea entregar', 'c. Todos los servicios que un proveedor de servicios ha retirado de la operación en vivo', 'd. Todos los servicios que presta actualmente un proveedor de servicios'],
        'respuesta_correcta': 'a. Todos los proyectos que el cliente planea entregar'
    },
    {
        'pregunta': '¿Las estructuras de acuerdo de nivel de servicio multinivel pueden contener cuál de los siguientes tipos de acuerdo de nivel de servicio?',
        'alternativas': ['a. Basado en servicios, basado en tecnología y basado en clientes', 'b. Basado en servicio, basado en cliente y basado en corporación', 'c. Basado en la tecnología, en el proveedor y en el usuario', 'd. Basado en la tecnología, en el proveedor y en el cliente'],
        'respuesta_correcta': 'b. Basado en servicio, basado en cliente y basado en corporación'
    },
    {
        'pregunta': 'El diseño del servicio entrega un nuevo servicio o un cambio a un servicio existente. ¿Cuáles de los siguientes están incluidos en el diseño del servicio?\n1. Tecnología\n2. Procesos\n3. Presupuesto\n4. Políticas',
        'alternativas': ['a. 1, 2 y 3', 'b. 2 y 4', 'c. 2, 3 y 4', 'd. 1, 2, 3 y 4'],
        'respuesta_correcta': 'd. 1, 2, 3 y 4'
    },
    {
        'pregunta': '¿Cuál de estas afirmaciones sobre la gestión de las relaciones de negocio (BRM) es la más correcta?',
        'alternativas': ['a. BRM se centra en una relación de alto nivel con los clientes', 'b. BRM supervisa los objetivos del servicio para todos los servicios', 'c. BRM revisa todos los cambios de servicio', 'd. BRM se centra en la relación con los usuarios a través de la mesa de servicio'],
        'respuesta_correcta': 'a. BRM se centra en una relación de alto nivel con los clientes'
    },
    {
        'pregunta': 'El diseño del servicio tiene cuatro áreas principales que deben considerarse para ofrecer un diseño integral. ¿Cuáles de estas son las cuatro áreas?',
        'alternativas': ['a. Productos, planes, desempeño, proceso', 'b. Proceso, plan, desempeño, socios', 'c. Personas, proceso, productos, socios', 'd. Socios, planes, personas, desempeño'],
        'respuesta_correcta': 'c. Personas, proceso, productos, socios'
    },
    {
        'pregunta': '¿Cuál de las siguientes es la definición correcta del catálogo de servicios?',
        'alternativas': ['a. Una base de datos o documento con información sobre todos los servicios de TI en vivo', 'b. Justificación de un gasto particular, incluida la información sobre costos, beneficios, opciones y riesgos', 'c. El conjunto completo de servicios administrados por un proveedor de servicios, utilizado para administrar el ciclo de vida completo de todos los servicios', 'd. Un documento que describe el servicio de TI, los objetivos de nivel de servicio y las responsabilidades del proveedor de servicios de TI y del cliente'],
        'respuesta_correcta': 'a. Una base de datos o documento con información sobre todos los servicios de TI en vivo'
    },
{
        'pregunta': '¿Cuál de los siguientes son propósitos del proceso Liberaciones y Gestión de Despliegue?',
        'alternativas': ['a. 2 y 3 solamente', 'b. Todas', 'c. 1 y 3 solamente', 'd. 1 y 2 solamente'],
        'respuesta_correcta': 'd. 1 y 2 solamente'
    },
    {
        'pregunta': '¿Cuál proceso es responsable de la revisión regular de los Acuerdos de Nivel Operacional (OLA)?',
        'alternativas': ['a. Gestión de la Demanda', 'b. Gestión de Proveedores', 'c. Gestión de Niveles de Servicio', 'd. Gestión del Portafolio de Servicio'],
        'respuesta_correcta': 'c. Gestión de Niveles de Servicio'
    },
    {
        'pregunta': '¿Cuál de los siguientes NO es un objetivo de la Operación del Servicio?',
        'alternativas': ['a. Gestionar la tecnología utilizada para entregar los servicios', 'b. Pruebas exhaustivas para asegurar que el servicio está diseñado para satisfacer las necesidades del negocio', 'c. Entregar y gestionar servicios de TI', 'd. Monitorear el rendimiento de la tecnología y los procesos'],
        'respuesta_correcta': 'b. Pruebas exhaustivas para asegurar que el servicio está diseñado para satisfacer las necesidades del negocio'
    },
    {
        'pregunta': '¿La Política de Seguridad de Información debería estar disponible con qué grupos de personas?',
        'alternativas': ['a. Gerentes de negocio senior, ejecutivos de TI y el Gerente de Seguridad de la Información solamente', 'b. Gerentes de negocio senior y todo el personal de TI solamente', 'c. Todos los clientes, usuarios y personal de TI', 'd. Personal de la Gestión de Seguridad de la Información solamente'],
        'respuesta_correcta': 'c. Todos los clientes, usuarios y personal de TI'
    },
    {
        'pregunta': '¿Cuál es el objetivo PRINCIPAL de la Gestión de la Disponibilidad?',
        'alternativas': ['a. Asegurar que la disponibilidad del servicio coincida o exceda las necesidades acordadas para el negocio', 'b. Asegurar que todos los objetivos en los Acuerdos de Niveles de Servicio (SLA) sean satisfechos', 'c. Garantizar los niveles de disponibilidad para los servicios y componentes', 'd. Monitorear y reportar la disponibilidad de componentes'],
        'respuesta_correcta': 'a. Asegurar que la disponibilidad del servicio coincida o exceda las necesidades acordadas para el negocio'
    },
    {
        'pregunta': '¿A qué se refiere el término Control de Operaciones?',
        'alternativas': ['a. Es la herramienta utilizada para monitorear y presentar el estado de la infraestructura de TI y Aplicaciones', 'b. Gestionar la función de Gestión Técnica y Aplicaciones', 'c. Supervisar la ejecución y monitorear las actividades operacionales y eventos', 'd. Es el monitoreo de Service Desk del estatus de la infraestructura cuando los operadores no están disponibles'],
        'respuesta_correcta': 'c. Supervisar la ejecución y monitorear las actividades operacionales y eventos'
    },
    {
        'pregunta': '¿Qué proceso es responsable de registrar relaciones entre componentes del servicio?',
        'alternativas': ['a. Gestión de Portafolio de Servicio', 'b. Gestión de Incidentes', 'c. Gestión de Niveles de Servicio', 'd. Activo de Servicio y Gestión de la Configuración'],
        'respuesta_correcta': 'd. Activo de Servicio y Gestión de la Configuración'
    },
    {
        'pregunta': 'Con cuál de las siguientes la Transición del Servicio provee guía\n1. Mover un servicio nuevo o modificado a producción\n2. Prueba y validación\n3. Transferir el servicio hacia o desde un proveedor de servicio externo',
        'alternativas': ['a. 1 y 3 solamente', 'b. 2 solamente', 'c. 1 y 2 solamente', 'd. Todas'],
        'respuesta_correcta': 'd. Todas'
    },
    {
        'pregunta': 'Los acuerdos de requerimientos de negocio y niveles de servicio para un nuevo servicio es parte de',
        'alternativas': ['a. Operación de Servicio', 'b. Estrategia de Servicio', 'c. Diseño de Servicio', 'd. Transición de Servicio'],
        'respuesta_correcta': 'c. Diseño de Servicio'
    },
    {
        'pregunta': '¿Cuál de los siguientes se puede describir como “unidades auto-contenidas de organizaciones”?',
        'alternativas': ['a. Roles', 'b. Procesos', 'c. Funciones', 'd. Procedimientos'],
        'respuesta_correcta': 'c. Funciones'
    },
    {
        'pregunta': '¿Cuáles de los siguientes conceptos básicos están incluidos en la Gestión de Accesos?\n1. Verificar la identidad de los usuarios que piden acceso a los servicios\n2. Establecer los permisos y privilegios de sistema para permitir el acceso a usuarios autorizados\n3. Definir las políticas de seguridad para el acceso al sistema\n4. Monitorear la disponibilidad de los sistemas que los usuarios deberían tener acceso',
        'alternativas': ['a. 2 y 3 solamente', 'b. 1 y 2 solamente', 'c. 2 y 4 solamente', 'd. 1 y 3 solamente'],
        'respuesta_correcta': 'b. 1 y 2 solamente'
    },
    {
        'pregunta': '¿Cuál de las siguientes es la MEJOR descripción de un Acuerdo de Nivel Operacional (OLA)?',
        'alternativas': ['a. Un acuerdo entre dos proveedores de servicio acerca de los niveles de servicio requeridos por el cliente', 'b. Un acuerdo escrito entre el proveedor del servicio de TI y su(s) cliente(s) definiendo los objetivos clave y las responsabilidades de ambas partes', 'c. Un acuerdo entre un proveedor de servicios de TI y otra parte de la misma organización que ayuda en la provisión de los servicios', 'd. Un acuerdo entre un Service Desk tercerizado y el cliente de TI acerca de reparaciones y tiempos de respuesta'],
        'respuesta_correcta': 'c. Un acuerdo entre un proveedor de servicios de TI y otra parte de la misma organización que ayuda en la provisión de los servicios'
    },
    {
        'pregunta': '¿Cuál de las siguientes es una actividad del proceso de Activo de Servicio y Gestión de la configuración?',
        'alternativas': ['a. Cuenta todos los activos financieros de la organización', 'b. Especifica los atributos relevantes por cada elemento de configuración (CI)', 'c. Diseña modelos de servicio para justificar la implementación de ITIL', 'd. Implementa ITIL a través de la organización'],
        'respuesta_correcta': 'b. Especifica los atributos relevantes por cada elemento de configuración (CI)'
    },
    {
        'pregunta': '¿Cuál de las siguientes es una responsabilidad del dueño de proceso?',
        'alternativas': ['a. Asegurar que el proceso es realizado como está documentado', 'b. Asegurar que los objetivos específicos en un Acuerdode Nivel de Servicio (SLA) sean satisfechas', 'c. Comprar herramientas para soportar el proceso', 'd. Llevar a cabo todas las actividades definidas en el proceso'],
        'respuesta_correcta': 'a. Asegurar que el proceso es realizado como está documentado'
    },
    {
        'pregunta': '¿Para qué es usado el modelo RACI?',
        'alternativas': ['a. Definición de requerimientos para un nuevo servicio o proceso', 'b. Documentación de roles y relaciones de los stakeholders en un proceso o actividad', 'c. Análisis del impacto del negocio de un incidente', 'd. Creación de un tablero de mando mostrando el estado general de la gestión del servicio'],
        'respuesta_correcta': 'b. Documentación de roles y relaciones de los stakeholders en un proceso o actividad'
    },
    {
        'pregunta': '¿Cuál de las siguientes podrían ser almacenados en la Biblioteca Definitiva de Medios (DML)?\n1. Copias de software comprado\n2. Copias de desarrollos intermedios de software\n3. Documentación relevante de licencias\n4. El cronograma de cambios',
        'alternativas': ['a. 3 y 4 solamente', 'b. 1 y 2 solamente', 'c. 1, 2 y 3 solamente', 'd. Todas'],
        'respuesta_correcta': 'c. 1, 2 y 3 solamente'
    },
    {
        'pregunta': '¿Cuál de las siguientes son ejemplos de herramientas que podrían soportar la fase Transición del Servicio del Ciclo de Vida?\nUna herramienta que almacena versiones definitivas de software\nUna herramienta de flujo de trabajo para la gestión de cambios\nUna herramienta automatizada de distribución de software\nHerramientas de validación y pruebas',
        'alternativas': ['a. 2, 3 y 4 solamente', 'b. Todas', 'c. 1, 3 y 4 solamente', 'd. 1, 2 y 3 solamente'],
        'respuesta_correcta': 'b. Todas'
    },
    {
        'pregunta': '¿Qué tipos de cambios NO son usualmente incluidos dentro del ámbito de la Gestión de Cambio del servicio?',
        'alternativas': ['a. Cambios en una computadora mainframe', 'b. Cambios en un Acuerdo de Nivel de Servicio (SLA)', 'c. El retiro de un servicio', 'd. Cambios en una estrategia de negocio'],
        'respuesta_correcta': 'd. Cambios en una estrategia de negocio'
    },
    {
        'pregunta': '¿Cuál de las siguientes es una actividad del proceso de Activo de Servicio y Gestión de la configuración?',
        'alternativas': ['a. Cuenta todos los activos financieros de la organización', 'b. Especifica los atributos relevantes por cada elemento de configuración (CI)', 'c. Diseña modelos de servicio para justificar la implementación de ITIL', 'd. Implementa ITIL a través de la organización'],
        'respuesta_correcta': 'b. Especifica los atributos relevantes por cada elemento de configuración (CI)'
    },
    {
        'pregunta': '¿Cuál de las siguientes es una responsabilidad del dueño de proceso?',
        'alternativas': ['a. Asegurar que el proceso es realizado como está documentado', 'b. Asegurar que los objetivos específicos en un Acuerdo de Nivel de Servicio (SLA) sean satisfechas', 'c. Comprar herramientas para soportar el proceso', 'd. Llevar a cabo todas las actividades definidas en el proceso'],
        'respuesta_correcta': 'a. Asegurar que el proceso es realizado como está documentado'
    }

]

@app.route('/')
def inicio():
    # Página inicial sin pregunta
    return render_template('topicos.html', pregunta=None)

@app.route('/buscar_pregunta', methods=['POST'])
def buscar_pregunta():
    texto_busqueda = request.form['buscar_pregunta'].strip()
    
    # Buscar la pregunta en el banco de preguntas
    for p in preguntas:
        if texto_busqueda.lower() in p['pregunta'].lower():
            return render_template('topicos.html', pregunta=p)
    
    # Si no se encontró la pregunta, mostrar mensaje
    return "Pregunta no encontrada. Por favor, intenta otra búsqueda."

@app.route('/submit', methods=['POST'])
def verificar_respuesta():
    respuesta_usuario = request.form.get('pregunta1').strip()
    
    # Aquí estamos utilizando la primera pregunta solo como ejemplo
    for pregunta in preguntas:
        if respuesta_usuario == pregunta['respuesta_correcta']:
            return f"¡Correcto! La respuesta era: {pregunta['respuesta_correcta']}"
    
    return f"Incorrecto."

if __name__ == '__main__':
    app.run(debug=True)