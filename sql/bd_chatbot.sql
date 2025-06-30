-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1:3307
-- Tiempo de generación: 30-06-2025 a las 10:14:26
-- Versión del servidor: 10.4.32-MariaDB
-- Versión de PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `bd_chatbot`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `categoria`
--

CREATE TABLE `categoria` (
  `id` int(10) NOT NULL,
  `nombre` text NOT NULL,
  `descripcion` text DEFAULT NULL,
  `activo` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `categoria`
--

INSERT INTO `categoria` (`id`, `nombre`, `descripcion`, `activo`) VALUES
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
(12, 'Año Académico', 'Información sobre semestres, cursos de verano y duración del año académico.', 1),
(13, 'Convenios internacionales', 'Convenios con universidades extranjeras', 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `documento`
--

CREATE TABLE `documento` (
  `id` int(11) NOT NULL,
  `titulo` varchar(150) NOT NULL,
  `descripcion` text DEFAULT NULL,
  `url` text NOT NULL,
  `activo` tinyint(1) NOT NULL,
  `preguntaid` int(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `estado_usuario`
--

CREATE TABLE `estado_usuario` (
  `numero` varchar(20) NOT NULL,
  `estado` varchar(100) NOT NULL,
  `categoriaid` int(10) DEFAULT NULL,
  `ultima_interaccion` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `historial`
--

CREATE TABLE `historial` (
  `id` int(11) NOT NULL,
  `mensaje` text NOT NULL,
  `fecha` datetime NOT NULL DEFAULT current_timestamp(),
  `categoriaid` int(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `historial`
--

INSERT INTO `historial` (`id`, `mensaje`, `fecha`, `categoriaid`) VALUES
(1, '¿Cuáles son los requisitos para postular a Ingeniería de Sistemas?', '2025-06-01 09:15:00', NULL),
(2, '¿Dónde puedo ver mi horario de clases?', '2025-06-01 10:23:45', NULL),
(3, 'No entiendo cómo funciona la matrícula online.', '2025-06-02 14:10:12', NULL),
(4, '¿Cuándo empiezan las clases del próximo ciclo?', '2025-06-03 08:00:00', NULL),
(5, '¿Qué sucede si pierdo mi carné universitario?', '2025-06-03 16:35:20', NULL),
(6, '¿Dónde está ubicado el laboratorio de redes?', '2025-06-04 11:45:30', NULL),
(7, '¿Cómo solicito un certificado de estudios?', '2025-06-04 18:25:10', NULL),
(8, '¿Qué cursos electivos están disponibles para mi carrera?', '2025-06-05 13:05:00', NULL),
(9, 'Tengo problemas para ingresar al aula virtual.', '2025-06-05 17:50:00', NULL),
(10, '¿Qué hacer si no me aparece una asignatura en el sistema?', '2025-06-06 08:20:00', NULL);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `palabra_clave`
--

CREATE TABLE `palabra_clave` (
  `id` int(11) NOT NULL,
  `palabra` text NOT NULL,
  `PREGUNTAid` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `palabra_clave`
--

INSERT INTO `palabra_clave` (`id`, `palabra`, `PREGUNTAid`) VALUES
(1, 'créditos', 1),
(2, 'complementarios', 1),
(3, 'justificación', 2),
(4, 'inasistencias', 2),
(5, 'retiro', 3),
(6, 'semestre', 3),
(7, 'académico', 3),
(8, 'retiro', 4),
(9, 'definitivo', 4),
(10, 'reserva', 5),
(11, 'matrícula', 5),
(12, 'reincorporación', 6),
(13, 'cursos', 7),
(14, 'verano', 7),
(15, 'prácticas', 8),
(16, 'preprofesionales', 8),
(17, 'cambio', 9),
(18, 'tema', 9),
(19, 'tesis', 9),
(20, 'actualización', 10),
(21, 'datos', 10),
(22, 'tesis', 10),
(23, 'obtención', 11),
(24, 'grado', 11),
(25, 'bachiller', 11),
(26, 'sustentación', 12),
(27, 'tesis', 12),
(28, 'titulación', 13),
(29, 'idioma', 14),
(30, 'inglés', 14),
(31, 'programa', 15),
(32, 'actualización', 15),
(33, 'tesis', 15),
(34, 'vigencia', 16),
(35, 'proyecto', 16),
(36, 'tesis', 16),
(37, 'aprobado', 16);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `pregunta`
--

CREATE TABLE `pregunta` (
  `id` int(10) NOT NULL,
  `titulo` text NOT NULL,
  `respuesta` text NOT NULL,
  `CATEGORIAid` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `pregunta`
--

INSERT INTO `pregunta` (`id`, `titulo`, `respuesta`, `CATEGORIAid`) VALUES
(1, 'Créditos complementarios', 'Debe acreditar mínimamente dos (2) créditos de formación complementaria, los cuales puede desarrollarlo mediante talleres: Deportivos, Artísticos, Tutoría par, Responsabilidad social, etc.', 1),
(2, 'Justificación de inasistencias', 'El estudiante puede justificar inasistencias presentando una solicitud en el campus virtual, dentro de los 2 días hábiles posteriores a la falta, adjuntando los documentos sustentatorios según el caso:\n\n\r\na) Fallecimiento de familiar (hasta 4° grado de consanguinidad o 2° de afinidad, o cónyuge): presentar certificado de defunción y documento que acredite el parentesco.\n\r\nb) Motivos de salud: certificado médico expedido por profesional o establecimiento de salud, visado por MINSA o EsSalud. En casos de consulta médica, adjuntar comprobante de pago con datos del paciente y médico, ticket de atención, indicaciones y recetas.\n\r\nc) Citación judicial: copia legalizada notarialmente del documento de citación.\n\r\nd) Representación institucional: constancia de participación en certamen académico, deportivo, religioso u otra actividad en nombre de la Facultad o Universidad.\n\n\r\nEl Director de Escuela evaluará la solicitud y, si procede, registrará las fechas y asignaturas afectadas. Las inasistencias justificadas no deben superar el 30% del total. No se recuperan clases, prácticas ni laboratorios, pero sí evaluaciones individuales programadas. En la última semana de clases, se evaluará la pertinencia de la justificación.', 2),
(3, 'Retiro de semestre académico', 'El retiro de semestre académico es un proceso voluntario autorizado por la Dirección de Escuela, que no permite retiro parcial de asignaturas. Puede solicitarse por motivos personales, familiares, económicos o de salud, debidamente sustentados. Se debe generar la solicitud mediante el campus virtual (módulo correspondiente), indicando las causas y adjuntando los documentos justificatorios.\n\nLa Dirección de Escuela evaluará los informes académicos y de asistencia del estudiante, y si lo considera necesario, podrá solicitar una entrevista. Tiene un plazo máximo de 5 días hábiles para resolver y registrar en el sistema la última fecha de asistencia.\n\nSi el retiro académico es aprobado, el estudiante puede anularlo dentro de un plazo no mayor a 5 días hábiles, presentando una solicitud virtual a la Dirección Académica, quien evaluará y comunicará la decisión a las áreas correspondientes. No habrá reintegro de pensiones por los días involucrados a este trámite de anulación.\n\nEn caso el estudiante tuviera deuda y el retiro sea aprobado, podrá solicitar la anulación de dicha deuda al Área de Pensiones, quien evaluará la solicitud y procederá con el cierre administrativo del trámite.', 3),
(4, 'Retiro definitivo', 'El retiro definitivo se solicita por módulo virtual y es evaluado por la Dirección de Escuela. Si se realiza hasta una semana antes de finalizar el semestre, implica también retiro del semestre; después de ese plazo, solo aplica como retiro administrativo. Puede anularse con trámite virtual dentro de los 5 días siguientes si desea continuar en el semestre. Para retomar estudios en semestres posteriores, puede solicitar anulación hasta en 2 años. La Dirección Académica evalúa la solicitud y comunica la decisión a las áreas correspondientes.', 3),
(5, 'Reserva de matrícula', 'Permite diferir voluntariamente la matrícula por un semestre académico inmediato. Se solicita con sustento a través del campus virtual en fechas del calendario académico, y no debe exceder tres (3) años consecutivos o alternos, debe ser aprobado por el director de escuela. Una vez aprobada, se realiza el pago para habilitación en el campus virtual. En caso de movilidad académica saliente, la reserva se genera automáticamente luego que el coordinador de movilidad haya validado el formato de llegada del estudiante.', 4),
(6, 'Reincorporación', 'Los estudiantes que dejaron de matricularse matricularse en uno o más semestres académicos y no ha solicitado reserva de matrícula, deben solicitar su reincorporación a través del campus virtual pagando el derecho correspondiente. El trámite va dirigido a dirección de escuela. Su aprobación está sujeta a vacantes y al calendario académico. Al reincorporarse, deben firmar aceptación de plan de estudios, tarifas y normativas vigentes. No procede si el estudiante fue separado por razones académicas o disciplinarias, o si no hay vacantes disponibles.', 4),
(7, 'Cursos de verano', 'Depende de la programación de la Escuela.', 5),
(8, 'Prácticas preprofesionales', 'El estudiante debe realizar un mínimo de 260 horas de prácticas, en uno o varios centros, en modalidad presencial o virtual, a partir del VIII ciclo, sin cursos pendientes de ciclos anteriores y con condición de estudiante activo. Para iniciar sus prácticas pre profesionales, deberá realizar su trámite en el campus virtual seleccionando el trámite “CARTA DE PRESENTACIÓN” y motivo “Prácticas pre profesionales”. Debe detallar los siguientes datos: \r\n- Nombre completo de la empresa o institución.\r\n- RUC para verificar su vigencia.\r\n- Nombres y cargo de la máxima autoridad.\r\n- Dirección fiscal de la empresa.\r\n- Jefe inmediato: nombres completos y cargo del supervisor. \r\n  Nota: Si es Arquitecto, indicar N.º CAP; si es Ingeniero, N.º CIP, y debe estar habilitado para ejercer la profesión.', 6),
(9, 'Cambio de tema de tesis', 'El estudiante podrá solicitar el cambio de tema por caso fortuito o fuerza mayor, con respaldo de su asesor mediante informe (Anexo 05). La solicitud debe presentarse dentro de los 10 días hábiles desde el inicio de clases, dirigida al Director(a) de Escuela, adjuntando el informe y un nuevo proyecto (Anexo 02). Si se aprueba, el estudiante deberá reiniciar el proceso según el reglamento (Art. 6° al 22°). El procedimiento está detallado en el Anexo 06.', 7),
(10, 'Actualización de datos de tesis', 'Si se requiere mejorar redacción de título, objetivos, línea de investigación, campo OCDE., se debe solicitar directamente un trámite de “ACTUALIZACIÓN DE DATOS DE TESIS” a través de su campus virtual, el cual será atendido por el Docente de Apoyo a Tesis (DAT). El trámite administrativo y académico que se seguirá para el cambio de tema de investigación se detalla en el anexo 07.', 7),
(11, 'Obtención del grado de bachiller', 'Requiere condición de egresado en el sistema del Campus Virtual USAT, no tener deudas, pago de trámite, haber llevado un curso de trabajo de investigación que se sigue en el último semestre de estudios y cumplir los demás requisitos que establezca en el Reglamento de Grados y Títulos.Estos requisitos pueden variar de acuerdo con la normativa nacional vigente en caso\r\nCorresponda.', 8),
(12, 'Sustentación de tesis', 'Requiere grado de bachiller, conformidad del asesor (Informe que declara la tesis apta para sustentar), no tener deudas y pago de derecho de sustentación.', 8),
(13, 'Titulación', 'Para obtener el título profesional se requiere: contar con el grado de bachiller en Ingeniería de Sistemas y Computación, aprobar la tesis ante jurado, no tener deudas con la Universidad, realizar el pago correspondiente al trámite, cumplir los requisitos administrativos, y otros establecidos en el Reglamento de Grados y Títulos. Estos requisitos pueden variar según normativa nacional vigente.', 8),
(14, 'Idioma inglés', 'Es requisito de egreso. Se debe acreditar nivel intermedio (B1).', 8),
(15, 'Programa de actualización de tesis', 'Los egresados o bachilleres cuyos trabajos de investigación hayan perdido vigencia deberán inscribirse en el programa de actualización de tesis, que consta de tres fases: Proyecto, Ejecución e Informe. Cada fase debe ser tramitada virtualmente a través del campus virtual USAT (campus egresado), abonando la tasa correspondiente. El calendario es establecido por el Vicerrectorado de Investigación e incluye:\n- ETAPA PROYECTO\n- ETAPA EJECUCIÓN\n- ETAPA INFORME', 7),
(16, 'Vigencia del proyecto de tesis aprobado', 'El proyecto de tesis tiene una vigencia de 3 años desde la aprobación del acto de sustentación. Excepcionalmente, puede ampliarse 1 año más previa solicitud al Director(a) de Escuela. Vencido este plazo, pierde validez y el estudiante deberá iniciar un nuevo proceso, presentando otro tema y pagando las tasas administrativas correspondientes.\r\n\r\n', 7),
(17, '¿Cuáles son las facultades que tiene la universidad?', 'Nuestra universidad cuenta con las siguientes facultades:\r\n  \n- Facultad de Ingeniería\r\n  \n- Facultad de Humanidades\r\n  \n- Facultad de Derecho\r\n  \n- Facultad de Medicina\r\n  \n- Facultad de Ciencias Empresariales', 11),
(18, '¿Qué carreras tiene la Facultad de Ingeniería?', 'La Facultad de Ingeniería ofrece las siguientes carreras:\r\n  \n- Arquitectura\r\n  \n- Ingeniería Civil\r\n  \n- Ingeniería de Sistemas y Computación\r\n  \n- Ingeniería Industrial\r\n  \n- Ingeniería Mecánica Eléctrica', 11),
(19, '¿Qué carreras hay en la Facultad de Humanidades?', 'La Facultad de Humanidades cuenta con las siguientes carreras:\r\n  \n- Educación Secundaria\r\n  \n- Filosofía y Teología\r\n  \n- Educación Primaria\r\n  \n- Educación Inicial\r\n  \n- Comunicación', 11),
(20, '¿Qué carreras hay en la Facultad de Derecho?', 'La Facultad de Derecho ofrece la carrera profesional de Derecho.', 11),
(21, '¿Qué carreras ofrece la Facultad de Medicina?', 'La Facultad de Medicina cuenta con las siguientes carreras:\r\n  \n- Medicina\r\n  \n- Psicología\r\n  \n- Odontología\r\n  \n- Enfermería', 11),
(22, '¿Qué carreras tiene la Facultad de Ciencias Empresariales?', 'La Facultad de Ciencias Empresariales ofrece las siguientes carreras:\r\n  \n- Administración de Empresas\r\n  \n- Administración Hotelera y de Servicios Turísticos\r\n  \n- Economía\r\n  \n- Contabilidad', 11),
(23, '¿Cuántos semestres tiene el año académico?', 'El año académico se divide en dos semestres: el Semestre Académico I (de marzo a julio) y el Semestre Académico II (de agosto a diciembre), cada uno con una duración mínima de 16 semanas.', 12),
(24, '¿Cuándo inicia y termina el primer semestre?', 'El Semestre Académico I se desarrolla preferentemente entre los meses de marzo y julio, con una duración mínima de 16 semanas.', 12),
(25, '¿Cuándo se lleva a cabo el segundo semestre?', 'El Semestre Académico II se lleva a cabo preferentemente entre los meses de agosto y diciembre, también con una duración mínima de 16 semanas.', 12),
(26, '¿Existen cursos de verano?', 'Sí. La universidad organiza un periodo académico de cursos de verano entre enero y febrero, con una duración de 7 semanas incluyendo evaluaciones. Las notas obtenidas se consideran para el cálculo del promedio ponderado acumulado.', 12),
(27, '¿Quién autoriza los cursos de verano?', 'Los cursos de verano son propuestos por el Director de Escuela, autorizados por el Decano de Facultad, comunicados al Vicerrectorado Académico y ejecutados por la Dirección Académica.', 12),
(28, '¿Hay un periodo de nivelación para ingresantes?', 'Sí. La universidad puede programar un periodo de nivelación o propedéutico para los ingresantes que requieran nivelarse en las competencias del perfil de ingreso.', 12),
(29, 'cursos complementarios', '* lenguaje de señas\n* tenis de mesa\n* futsal para varones y damas\n* dibujo y pintura\n* ajedrez\n* danzas folklóricas\n* voley\n* básquet\n* etiqueta social\n* Taekwondo\n* guitarra\n* percusión', 5),
(30, 'Convenios con universidades de España', '* Universidad de Cádiz\n* Universidad de Navarra\n* Universidad Católica de Valencia San Vicente Mártir\n* Universidad de Zaragoza\n* Universidad Rey Juan Carlos\n* Universidad del País Vasco\n* Universidad Católica de Ávila (UCAV)\n* Universidad de Granada\n* Universidad Cardenal Herrera (CEU)\n* Universidad de Jaén\n* Universidad de Málaga\n* Universidad de Santiago de Compostela (USC)\n* Universitat Internacional de Catalunya (UIC)', 13),
(31, 'Convenios con universidades de Francia', '* Université de Bordeaux\n* Université Catholique de l’Ouest (UCO)', 13),
(32, 'Convenios con universidades de Italia', '* Sapienza Università di Roma\n* Università degli Studi di Bari Aldo Moro\n* Università degli Studi di Trieste', 13),
(33, 'Convenios con universidades de USA', '* Washington State University', 13),
(34, 'Convenios con universidades de Canadá', '* University of Regina', 13),
(35, 'Convenios con universidades de India', '* Lovely Professional University', 13),
(36, 'Convenios con universidades de México', '* Red de Universidades Anáhuac\n* Universidad Autónoma de Nuevo León\n* Universidad Vasco de Quiroga (UVAQ)\n* Universidad Tecnológica de San Juan del Río\n* Universidad Nacional Autónoma de México (UNAM)\n* Universidad de Monterrey', 13),
(37, 'Convenios con universidades de Argentina', '* Pontificia Universidad Católica Argentina (UCA)\n* Universidad Católica de Cuyo\n* Universidad Católica de Salta (UCASAL)\n* Universidad Nacional de Tucumán', 13),
(38, 'Convenios con universidades de Brasil', '* PUC Goiás\n* Universidade Federal do Rio de Janeiro (UFRJ)\n* La Salle\n* PUC Campinas\n* Universidad de São Paulo (USP)', 13),
(39, 'Convenios con universidades de Chile', '* Universidad de los Andes\n* Universidad Católica de Temuco\n* Pontificia Universidad Católica de Valparaíso', 13),
(40, 'Convenios con universidades de Ecuador', '* Universidad de Cuenca', 13),
(41, 'Convenios con universidades de Colombia', '* Universidad Católica de Colombia\n* Pontificia Universidad Javeriana\n* Universidad CES\n* Universidad Mariana\n* Universidad Autónoma de Occidente\n* Universidad de La Sabana\n* Fundación Universitaria Juan D Castellanos\n* Universidad Nacional de Colombia', 13),
(42, 'Improcedencia del retiro de semestre académico', 'El retiro de semestre académico no procede si el estudiante se ha retirado en dos ocasiones consecutivas o en tres ocasiones alternas dentro del mismo programa de estudios.', 3),
(43, 'Omisión de trámite de retiro', 'Si un estudiante matriculado deja de asistir a clases sin realizar el trámite de retiro de semestre, acumulará deuda de pensiones por efectos administrativos.', 3),
(44, 'Director de Escuela', 'Ing. Huilder Mera\r\nCorreo hmera.@usat.edu.pe', 10);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuarios_chat`
--

CREATE TABLE `usuarios_chat` (
  `numero` varchar(20) NOT NULL,
  `nombre` varchar(100) DEFAULT NULL,
  `fecha_registro` datetime NOT NULL DEFAULT current_timestamp(),
  `estado` tinyint(4) DEFAULT 1
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `webhook`
--

CREATE TABLE `webhook` (
  `id` int(11) NOT NULL,
  `fecha` datetime NOT NULL DEFAULT current_timestamp(),
  `dato` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `categoria`
--
ALTER TABLE `categoria`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `documento`
--
ALTER TABLE `documento`
  ADD PRIMARY KEY (`id`),
  ADD KEY `FKdocumento246863` (`preguntaid`);

--
-- Indices de la tabla `estado_usuario`
--
ALTER TABLE `estado_usuario`
  ADD PRIMARY KEY (`numero`),
  ADD KEY `FKestado_usu784846` (`categoriaid`);

--
-- Indices de la tabla `historial`
--
ALTER TABLE `historial`
  ADD PRIMARY KEY (`id`),
  ADD KEY `FKhistorial675424` (`categoriaid`);

--
-- Indices de la tabla `palabra_clave`
--
ALTER TABLE `palabra_clave`
  ADD PRIMARY KEY (`id`),
  ADD KEY `FKpalabra_cl896610` (`PREGUNTAid`);

--
-- Indices de la tabla `pregunta`
--
ALTER TABLE `pregunta`
  ADD PRIMARY KEY (`id`),
  ADD KEY `FKpregunta124192` (`CATEGORIAid`);

--
-- Indices de la tabla `usuarios_chat`
--
ALTER TABLE `usuarios_chat`
  ADD PRIMARY KEY (`numero`);

--
-- Indices de la tabla `webhook`
--
ALTER TABLE `webhook`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `categoria`
--
ALTER TABLE `categoria`
  MODIFY `id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- AUTO_INCREMENT de la tabla `documento`
--
ALTER TABLE `documento`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `historial`
--
ALTER TABLE `historial`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT de la tabla `palabra_clave`
--
ALTER TABLE `palabra_clave`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=38;

--
-- AUTO_INCREMENT de la tabla `pregunta`
--
ALTER TABLE `pregunta`
  MODIFY `id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=45;

--
-- AUTO_INCREMENT de la tabla `webhook`
--
ALTER TABLE `webhook`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `documento`
--
ALTER TABLE `documento`
  ADD CONSTRAINT `FKdocumento246863` FOREIGN KEY (`preguntaid`) REFERENCES `pregunta` (`id`);

--
-- Filtros para la tabla `estado_usuario`
--
ALTER TABLE `estado_usuario`
  ADD CONSTRAINT `FKestado_usu784846` FOREIGN KEY (`categoriaid`) REFERENCES `categoria` (`id`);

--
-- Filtros para la tabla `historial`
--
ALTER TABLE `historial`
  ADD CONSTRAINT `FKhistorial675424` FOREIGN KEY (`categoriaid`) REFERENCES `categoria` (`id`);

--
-- Filtros para la tabla `palabra_clave`
--
ALTER TABLE `palabra_clave`
  ADD CONSTRAINT `FKpalabra_cl896610` FOREIGN KEY (`PREGUNTAid`) REFERENCES `pregunta` (`id`);

--
-- Filtros para la tabla `pregunta`
--
ALTER TABLE `pregunta`
  ADD CONSTRAINT `FKpregunta124192` FOREIGN KEY (`CATEGORIAid`) REFERENCES `categoria` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
