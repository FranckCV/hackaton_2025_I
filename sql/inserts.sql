INSERT INTO categoria (`id`, `nombre`, `descripcion`, `activo`) VALUES
(1, 'Créditos', NULL, 1),
(2, 'Inasistencias', NULL, 1),
(3, 'Retiro', NULL, 1),
(4, 'Matrícula', NULL, 1),
(5, 'Cursos', NULL, 1),
(6, 'Prácticas', NULL, 1),
(7, 'Tesis', NULL, 1),
(8, 'Grados y Títulos', NULL, 1),
(10, 'Autoridades', 'Autoridades de la Escuela de Ingenieria en Sistema y Computacion de USAT', 1),
(11, 'Facultades', NULL, 1),
(12, 'Año Académico', 'Información sobre semestres, cursos de verano y duración del año académico.', 1);
INSERT INTO categoria (id, nombre, descripcion, activo) VALUES 
(13, 'Convenios Internacionales', 'Información sobre convenios con universidades extranjeras', 1),
(14, 'Becas', 'Becas y ayudas económicas', 1);

INSERT INTO pregunta (id, titulo, respuesta, CATEGORIAid) VALUES (1, 'Créditos complementarios', 'Debe acreditar mínimamente dos (2) créditos de formación complementaria, los cuales puede desarrollarlo mediante talleres: Deportivos, Artísticos, Tutoría par, Responsabilidad social, etc.', 1);
INSERT INTO pregunta (id, titulo, respuesta, CATEGORIAid) VALUES 
(
  2,
  'Justificación de inasistencias',
  'El estudiante puede justificar inasistencias presentando una solicitud en el campus virtual, dentro de los 2 días hábiles posteriores a la falta, adjuntando los documentos sustentatorios según el caso:\n\n
a) Fallecimiento de familiar (hasta 4° grado de consanguinidad o 2° de afinidad, o cónyuge): presentar certificado de defunción y documento que acredite el parentesco.\n
b) Motivos de salud: certificado médico expedido por profesional o establecimiento de salud, visado por MINSA o EsSalud. En casos de consulta médica, adjuntar comprobante de pago con datos del paciente y médico, ticket de atención, indicaciones y recetas.\n
c) Citación judicial: copia legalizada notarialmente del documento de citación.\n
d) Representación institucional: constancia de participación en certamen académico, deportivo, religioso u otra actividad en nombre de la Facultad o Universidad.\n\n
El Director de Escuela evaluará la solicitud y, si procede, registrará las fechas y asignaturas afectadas. Las inasistencias justificadas no deben superar el 30% del total. No se recuperan clases, prácticas ni laboratorios, pero sí evaluaciones individuales programadas. En la última semana de clases, se evaluará la pertinencia de la justificación.',
  2
);
INSERT INTO pregunta (id, titulo, respuesta, CATEGORIAid) VALUES 
(
  3,
  'Retiro de semestre académico',
  'El retiro de semestre académico es un proceso voluntario autorizado por la Dirección de Escuela, que no permite retiro parcial de asignaturas. Puede solicitarse por motivos personales, familiares, económicos o de salud, debidamente sustentados. Se debe generar la solicitud mediante el campus virtual (módulo correspondiente), indicando las causas y adjuntando los documentos justificatorios.\n\nLa Dirección de Escuela evaluará los informes académicos y de asistencia del estudiante, y si lo considera necesario, podrá solicitar una entrevista. Tiene un plazo máximo de 5 días hábiles para resolver y registrar en el sistema la última fecha de asistencia.\n\nSi el retiro académico es aprobado, el estudiante puede anularlo dentro de un plazo no mayor a 5 días hábiles, presentando una solicitud virtual a la Dirección Académica, quien evaluará y comunicará la decisión a las áreas correspondientes. No habrá reintegro de pensiones por los días involucrados a este trámite de anulación.\n\nEn caso el estudiante tuviera deuda y el retiro sea aprobado, podrá solicitar la anulación de dicha deuda al Área de Pensiones, quien evaluará la solicitud y procederá con el cierre administrativo del trámite.',
  3
);

INSERT INTO pregunta (id, titulo, respuesta, CATEGORIAid) VALUES 
(
  4,
  'Retiro definitivo',
  'El retiro definitivo se solicita por módulo virtual y es evaluado por la Dirección de Escuela. Si se realiza hasta una semana antes de finalizar el semestre, implica también retiro del semestre; después de ese plazo, solo aplica como retiro administrativo. Puede anularse con trámite virtual dentro de los 5 días siguientes si desea continuar en el semestre. Para retomar estudios en semestres posteriores, puede solicitar anulación hasta en 2 años. La Dirección Académica evalúa la solicitud y comunica la decisión a las áreas correspondientes.',
  3
);
INSERT INTO pregunta (id, titulo, respuesta, CATEGORIAid) VALUES 
(
  5,
  'Reserva de matrícula',
  'Permite diferir voluntariamente la matrícula por un semestre académico inmediato. Se solicita con sustento a través del campus virtual en fechas del calendario académico, y no debe exceder tres (3) años consecutivos o alternos, debe ser aprobado por el director de escuela. Una vez aprobada, se realiza el pago para habilitación en el campus virtual. En caso de movilidad académica saliente, la reserva se genera automáticamente luego que el coordinador de movilidad haya validado el formato de llegada del estudiante.', 
  4
);
INSERT INTO pregunta (id, titulo, respuesta, CATEGORIAid) VALUES 
(
  6,
  'Reincorporación',
  'Los estudiantes que dejaron de matricularse matricularse en uno o más semestres académicos y no ha solicitado reserva de matrícula, deben solicitar su reincorporación a través del campus virtual pagando el derecho correspondiente. El trámite va dirigido a dirección de escuela. Su aprobación está sujeta a vacantes y al calendario académico. Al reincorporarse, deben firmar aceptación de plan de estudios, tarifas y normativas vigentes. No procede si el estudiante fue separado por razones académicas o disciplinarias, o si no hay vacantes disponibles.', 
  4
);
INSERT INTO pregunta (id, titulo, respuesta, CATEGORIAid) VALUES (7, 'Cursos de verano', 'Depende de la programación de la Escuela.', 5);
INSERT INTO pregunta (id, titulo, respuesta, CATEGORIAid) VALUES 
(
  8,
  'Prácticas preprofesionales',
  'El estudiante debe realizar un mínimo de 260 horas de prácticas, en uno o varios centros, en modalidad presencial o virtual, a partir del VIII ciclo, sin cursos pendientes de ciclos anteriores y con condición de estudiante activo. Para iniciar sus prácticas pre profesionales, deberá realizar su trámite en el campus virtual seleccionando el trámite “CARTA DE PRESENTACIÓN” y motivo “Prácticas pre profesionales”. Debe detallar los siguientes datos: 
- Nombre completo de la empresa o institución.
- RUC para verificar su vigencia.
- Nombres y cargo de la máxima autoridad.
- Dirección fiscal de la empresa.
- Jefe inmediato: nombres completos y cargo del supervisor. 
  Nota: Si es Arquitecto, indicar N.º CAP; si es Ingeniero, N.º CIP, y debe estar habilitado para ejercer la profesión.',
  6
);
INSERT INTO pregunta (id, titulo, respuesta, CATEGORIAid) VALUES 
(9, 'Cambio de tema de tesis', 'El estudiante podrá solicitar el cambio de tema por caso fortuito o fuerza mayor, con respaldo de su asesor mediante informe (Anexo 05). La solicitud debe presentarse dentro de los 10 días hábiles desde el inicio de clases, dirigida al Director(a) de Escuela, adjuntando el informe y un nuevo proyecto (Anexo 02). Si se aprueba, el estudiante deberá reiniciar el proceso según el reglamento (Art. 6° al 22°). El procedimiento está detallado en el Anexo 06.', 7);
INSERT INTO pregunta (id, titulo, respuesta, CATEGORIAid) VALUES (10, 'Actualización de datos de tesis', 'Si se requiere mejorar redacción de título, objetivos, línea de investigación, campo OCDE., se debe solicitar directamente un trámite de “ACTUALIZACIÓN DE DATOS DE TESIS” a través de su campus virtual, el cual será atendido por el Docente de Apoyo a Tesis (DAT). El trámite administrativo y académico que se seguirá para el cambio de tema de investigación se detalla en el anexo 07.', 7);
INSERT INTO pregunta (id, titulo, respuesta, CATEGORIAid) VALUES (11, 'Obtención del grado de bachiller', 'Requiere condición de egresado en el sistema del Campus Virtual USAT, no tener deudas, pago de trámite, haber llevado un curso de trabajo de investigación que se sigue en el último semestre de estudios y cumplir los demás requisitos que establezca en el Reglamento de Grados y Títulos.Estos requisitos pueden variar de acuerdo con la normativa nacional vigente en caso
Corresponda.', 8);
INSERT INTO pregunta (id, titulo, respuesta, CATEGORIAid) VALUES (12, 'Sustentación de tesis', 'Requiere grado de bachiller, conformidad del asesor (Informe que declara la tesis apta para sustentar), no tener deudas y pago de derecho de sustentación.', 8);
INSERT INTO pregunta (id, titulo, respuesta, CATEGORIAid) VALUES (13, 'Titulación', 'Para obtener el título profesional se requiere: contar con el grado de bachiller en Ingeniería de Sistemas y Computación, aprobar la tesis ante jurado, no tener deudas con la Universidad, realizar el pago correspondiente al trámite, cumplir los requisitos administrativos, y otros establecidos en el Reglamento de Grados y Títulos. Estos requisitos pueden variar según normativa nacional vigente.', 8);
INSERT INTO pregunta (id, titulo, respuesta, CATEGORIAid) VALUES (14, 'Idioma inglés', 'Es requisito de egreso. Se debe acreditar nivel intermedio (B1).', 8);
INSERT INTO pregunta (id, titulo, respuesta, CATEGORIAid) VALUES (15, 'Programa de actualización de tesis', 'Los egresados o bachilleres cuyos trabajos de investigación hayan perdido vigencia deberán inscribirse en el programa de actualización de tesis, que consta de tres fases: Proyecto, Ejecución e Informe. Cada fase debe ser tramitada virtualmente a través del campus virtual USAT (campus egresado), abonando la tasa correspondiente. El calendario es establecido por el Vicerrectorado de Investigación e incluye:\n- ETAPA PROYECTO\n- ETAPA EJECUCIÓN\n- ETAPA INFORME', 7);
INSERT INTO pregunta (id, titulo, respuesta, CATEGORIAid) VALUES (16, 'Vigencia del proyecto de tesis aprobado', 'El proyecto de tesis tiene una vigencia de 3 años desde la aprobación del acto de sustentación. Excepcionalmente, puede ampliarse 1 año más previa solicitud al Director(a) de Escuela. Vencido este plazo, pierde validez y el estudiante deberá iniciar un nuevo proceso, presentando otro tema y pagando las tasas administrativas correspondientes.

', 7);
INSERT INTO palabra_clave (palabra, PREGUNTAid) VALUES ('créditos', 1);
INSERT INTO palabra_clave (palabra, PREGUNTAid) VALUES ('complementarios', 1);
INSERT INTO palabra_clave (palabra, PREGUNTAid) VALUES ('justificación', 2);
INSERT INTO palabra_clave (palabra, PREGUNTAid) VALUES ('inasistencias', 2);
INSERT INTO palabra_clave (palabra, PREGUNTAid) VALUES ('retiro', 3);
INSERT INTO palabra_clave (palabra, PREGUNTAid) VALUES ('semestre', 3);
INSERT INTO palabra_clave (palabra, PREGUNTAid) VALUES ('académico', 3);
INSERT INTO palabra_clave (palabra, PREGUNTAid) VALUES ('retiro', 4);
INSERT INTO palabra_clave (palabra, PREGUNTAid) VALUES ('definitivo', 4);
INSERT INTO palabra_clave (palabra, PREGUNTAid) VALUES ('reserva', 5);
INSERT INTO palabra_clave (palabra, PREGUNTAid) VALUES ('matrícula', 5);
INSERT INTO palabra_clave (palabra, PREGUNTAid) VALUES ('reincorporación', 6);
INSERT INTO palabra_clave (palabra, PREGUNTAid) VALUES ('cursos', 7);
INSERT INTO palabra_clave (palabra, PREGUNTAid) VALUES ('verano', 7);
INSERT INTO palabra_clave (palabra, PREGUNTAid) VALUES ('prácticas', 8);
INSERT INTO palabra_clave (palabra, PREGUNTAid) VALUES ('preprofesionales', 8);
INSERT INTO palabra_clave (palabra, PREGUNTAid) VALUES ('cambio', 9);
INSERT INTO palabra_clave (palabra, PREGUNTAid) VALUES ('tema', 9);
INSERT INTO palabra_clave (palabra, PREGUNTAid) VALUES ('tesis', 9);
INSERT INTO palabra_clave (palabra, PREGUNTAid) VALUES ('actualización', 10);
INSERT INTO palabra_clave (palabra, PREGUNTAid) VALUES ('datos', 10);
INSERT INTO palabra_clave (palabra, PREGUNTAid) VALUES ('tesis', 10);
INSERT INTO palabra_clave (palabra, PREGUNTAid) VALUES ('obtención', 11);
INSERT INTO palabra_clave (palabra, PREGUNTAid) VALUES ('grado', 11);
INSERT INTO palabra_clave (palabra, PREGUNTAid) VALUES ('bachiller', 11);
INSERT INTO palabra_clave (palabra, PREGUNTAid) VALUES ('sustentación', 12);
INSERT INTO palabra_clave (palabra, PREGUNTAid) VALUES ('tesis', 12);
INSERT INTO palabra_clave (palabra, PREGUNTAid) VALUES ('titulación', 13);
INSERT INTO palabra_clave (palabra, PREGUNTAid) VALUES ('idioma', 14);
INSERT INTO palabra_clave (palabra, PREGUNTAid) VALUES ('inglés', 14);
INSERT INTO palabra_clave (palabra, PREGUNTAid) VALUES ('programa', 15);
INSERT INTO palabra_clave (palabra, PREGUNTAid) VALUES ('actualización', 15);
INSERT INTO palabra_clave (palabra, PREGUNTAid) VALUES ('tesis', 15);
INSERT INTO palabra_clave (palabra, PREGUNTAid) VALUES ('vigencia', 16);
INSERT INTO palabra_clave (palabra, PREGUNTAid) VALUES ('proyecto', 16);
INSERT INTO palabra_clave (palabra, PREGUNTAid) VALUES ('tesis', 16);
INSERT INTO palabra_clave (palabra, PREGUNTAid) VALUES ('aprobado', 16);

INSERT INTO historial (mensaje, fecha) VALUES
('¿Cuáles son los requisitos para postular a Ingeniería de Sistemas?', '2025-06-01 09:15:00'),
('¿Dónde puedo ver mi horario de clases?', '2025-06-01 10:23:45'),
('No entiendo cómo funciona la matrícula online.', '2025-06-02 14:10:12'),
('¿Cuándo empiezan las clases del próximo ciclo?', '2025-06-03 08:00:00'),
('¿Qué sucede si pierdo mi carné universitario?', '2025-06-03 16:35:20'),
('¿Dónde está ubicado el laboratorio de redes?', '2025-06-04 11:45:30'),
('¿Cómo solicito un certificado de estudios?', '2025-06-04 18:25:10'),
('¿Qué cursos electivos están disponibles para mi carrera?', '2025-06-05 13:05:00'),
('Tengo problemas para ingresar al aula virtual.', '2025-06-05 17:50:00'),
('¿Qué hacer si no me aparece una asignatura en el sistema?', '2025-06-06 08:20:00');


INSERT INTO pregunta (titulo, respuesta, CATEGORIAid) VALUES
(
  '¿Cuáles son las facultades que tiene la universidad?',
  'Nuestra universidad cuenta con las siguientes facultades:
  \n- Facultad de Ingeniería
  \n- Facultad de Humanidades
  \n- Facultad de Derecho
  \n- Facultad de Medicina
  \n- Facultad de Ciencias Empresariales',
  11
),
(
  '¿Qué carreras tiene la Facultad de Ingeniería?',
  'La Facultad de Ingeniería ofrece las siguientes carreras:
  \n- Arquitectura
  \n- Ingeniería Civil
  \n- Ingeniería de Sistemas y Computación
  \n- Ingeniería Industrial
  \n- Ingeniería Mecánica Eléctrica',
  11
),
(
  '¿Qué carreras hay en la Facultad de Humanidades?',
  'La Facultad de Humanidades cuenta con las siguientes carreras:
  \n- Educación Secundaria
  \n- Filosofía y Teología
  \n- Educación Primaria
  \n- Educación Inicial
  \n- Comunicación',
  11
),
(
  '¿Qué carreras hay en la Facultad de Derecho?',
  'La Facultad de Derecho ofrece la carrera profesional de Derecho.',
  11
),
(
  '¿Qué carreras ofrece la Facultad de Medicina?',
  'La Facultad de Medicina cuenta con las siguientes carreras:
  \n- Medicina
  \n- Psicología
  \n- Odontología
  \n- Enfermería',
  11
),
(
  '¿Qué carreras tiene la Facultad de Ciencias Empresariales?',
  'La Facultad de Ciencias Empresariales ofrece las siguientes carreras:
  \n- Administración de Empresas
  \n- Administración Hotelera y de Servicios Turísticos
  \n- Economía
  \n- Contabilidad',
  11
);


INSERT INTO pregunta (titulo, respuesta, CATEGORIAid) VALUES
(
  '¿Cuántos semestres tiene el año académico?',
  'El año académico se divide en dos semestres: el Semestre Académico I (de marzo a julio) y el Semestre Académico II (de agosto a diciembre), cada uno con una duración mínima de 16 semanas.',
  12
),
(
  '¿Cuándo inicia y termina el primer semestre?',
  'El Semestre Académico I se desarrolla preferentemente entre los meses de marzo y julio, con una duración mínima de 16 semanas.',
  12
),
(
  '¿Cuándo se lleva a cabo el segundo semestre?',
  'El Semestre Académico II se lleva a cabo preferentemente entre los meses de agosto y diciembre, también con una duración mínima de 16 semanas.',
  12
),
(
  '¿Existen cursos de verano?',
  'Sí. La universidad organiza un periodo académico de cursos de verano entre enero y febrero, con una duración de 7 semanas incluyendo evaluaciones. Las notas obtenidas se consideran para el cálculo del promedio ponderado acumulado.',
  12
),
(
  '¿Quién autoriza los cursos de verano?',
  'Los cursos de verano son propuestos por el Director de Escuela, autorizados por el Decano de Facultad, comunicados al Vicerrectorado Académico y ejecutados por la Dirección Académica.',
  12
),
(
  '¿Hay un periodo de nivelación para ingresantes?',
  'Sí. La universidad puede programar un periodo de nivelación o propedéutico para los ingresantes que requieran nivelarse en las competencias del perfil de ingreso.',
  12
);


INSERT INTO `pregunta` (`titulo`, `respuesta`, `CATEGORIAid`)
VALUES (
  'cursos complementarios',
  '* lenguaje de señas\n* tenis de mesa\n* futsal para varones y damas\n* dibujo y pintura\n* ajedrez\n* danzas folklóricas\n* voley\n* básquet\n* etiqueta social\n* Taekwondo\n* guitarra\n* percusión',
  5
);

INSERT INTO `pregunta` (`titulo`, `respuesta`, `CATEGORIAid`) VALUES
('Convenios con universidades de España',
'* Universidad de Cádiz\n* Universidad de Navarra\n* Universidad Católica de Valencia San Vicente Mártir\n* Universidad de Zaragoza\n* Universidad Rey Juan Carlos\n* Universidad del País Vasco\n* Universidad Católica de Ávila (UCAV)\n* Universidad de Granada\n* Universidad Cardenal Herrera (CEU)\n* Universidad de Jaén\n* Universidad de Málaga\n* Universidad de Santiago de Compostela (USC)\n* Universitat Internacional de Catalunya (UIC)',
13),

('Convenios con universidades de Francia',
'* Université de Bordeaux\n* Université Catholique de l’Ouest (UCO)',
13),

('Convenios con universidades de Italia',
'* Sapienza Università di Roma\n* Università degli Studi di Bari Aldo Moro\n* Università degli Studi di Trieste',
13),

('Convenios con universidades de USA',
'* Washington State University',
13),

('Convenios con universidades de Canadá',
'* University of Regina',
13),

('Convenios con universidades de India',
'* Lovely Professional University',
13),

('Convenios con universidades de México',
'* Red de Universidades Anáhuac\n* Universidad Autónoma de Nuevo León\n* Universidad Vasco de Quiroga (UVAQ)\n* Universidad Tecnológica de San Juan del Río\n* Universidad Nacional Autónoma de México (UNAM)\n* Universidad de Monterrey',
13),

('Convenios con universidades de Argentina',
'* Pontificia Universidad Católica Argentina (UCA)\n* Universidad Católica de Cuyo\n* Universidad Católica de Salta (UCASAL)\n* Universidad Nacional de Tucumán',
13),

('Convenios con universidades de Brasil',
'* PUC Goiás\n* Universidade Federal do Rio de Janeiro (UFRJ)\n* La Salle\n* PUC Campinas\n* Universidad de São Paulo (USP)',
13),

('Convenios con universidades de Chile',
'* Universidad de los Andes\n* Universidad Católica de Temuco\n* Pontificia Universidad Católica de Valparaíso',
13),

('Convenios con universidades de Ecuador',
'* Universidad de Cuenca',
13),

('Convenios con universidades de Colombia',
'* Universidad Católica de Colombia\n* Pontificia Universidad Javeriana\n* Universidad CES\n* Universidad Mariana\n* Universidad Autónoma de Occidente\n* Universidad de La Sabana\n* Fundación Universitaria Juan D Castellanos\n* Universidad Nacional de Colombia',
13);


INSERT INTO pregunta (titulo, respuesta, CATEGORIAid) VALUES 
(
  'Improcedencia del retiro de semestre académico',
  'El retiro de semestre académico no procede si el estudiante se ha retirado en dos ocasiones consecutivas o en tres ocasiones alternas dentro del mismo programa de estudios.',
  3
);
INSERT INTO pregunta (titulo, respuesta, CATEGORIAid) VALUES 
(
  'Omisión de trámite de retiro',
  'Si un estudiante matriculado deja de asistir a clases sin realizar el trámite de retiro de semestre, acumulará deuda de pensiones por efectos administrativos.',
  3
);

INSERT INTO pregunta (titulo, respuesta, CATEGORIAid) VALUES 
('Director de Escuela', 'Ing. Huilder Mera\r\nCorreo hmera.@usat.edu.pe', 10);

INSERT INTO pregunta (titulo, respuesta, CATEGORIAid) VALUES 
('Becas', 'Se otorgan becas por rendimiento académico en estricto orden de mérito', 14);


INSERT INTO `documento` (`id`, `titulo`, `descripcion`, `url`, `activo`, `preguntaid`) VALUES
(1, 'Manual de sustentación de tesis', 'Manual para hacer una correcta sustentacion de tesis', 'https://franckcv.pythonanywhere.com/static/docs/MANUAL_SUSTENTACION_TESIS_V3.pdf', 1, NULL),
(2, 'Plan de estudios 2017', 'Plan de estudios para la carrera de ingenieria en sistemas hecho en 2017', 'https://franckcv.pythonanywhere.com/static/docs/sistemas2017-v3.pdf', 1, NULL),
(3, 'Plan de estudios 2025', 'Plan de estudios para la carrera de ingenieria en sistemas hecho en 2025', 'https://franckcv.pythonanywhere.com/static/docs/sistemas2025.pdf', 1, NULL),
(4, 'Cartilla pensiones 2025', 'La presente Cartilla establece las normas para el proceso administrativo de matrícula, el pago de la misma, así como el de pensiones y demás aspectos conexos vigentes del Semestre Académico 2025-1.', 'https://franckcv.pythonanywhere.com/static/docs/CartillaPensiones2025IFinal28.01.25.pdf', 1, NULL),
(5, 'Cartilla Informativa Cursos de verano 2025', '', 'https://franckcv.pythonanywhere.com/static/docs/CARTILLAiNFORMATIVACursosVerano2025Final19.11.24.pdf', 1, NULL),
(6, 'Directiva de ayuda economica pregrado 2025', 'Directiva que brinda información respecto a las becas por ayuda económica ', 'https://franckcv.pythonanywhere.com/static/docs/Directiva_de_Ayuda_Economica_Pregrado_V5.pdf', 1, 10);

