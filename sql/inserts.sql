INSERT INTO categoria (id, nombre, descripcion, activo) VALUES (1, 'Créditos', NULL, 1);
INSERT INTO categoria (id, nombre, descripcion, activo) VALUES (2, 'Inasistencias', NULL, 1);
INSERT INTO categoria (id, nombre, descripcion, activo) VALUES (3, 'Retiro', NULL, 1);
INSERT INTO categoria (id, nombre, descripcion, activo) VALUES (4, 'Matrícula', NULL, 1);
INSERT INTO categoria (id, nombre, descripcion, activo) VALUES (5, 'Cursos', NULL, 1);
INSERT INTO categoria (id, nombre, descripcion, activo) VALUES (6, 'Prácticas', NULL, 1);
INSERT INTO categoria (id, nombre, descripcion, activo) VALUES (7, 'Tesis', NULL, 1);
INSERT INTO categoria (id, nombre, descripcion, activo) VALUES (8, 'Grados y Títulos', NULL, 1);
INSERT INTO pregunta (id, titulo, respuesta, CATEGORIAid) VALUES (1, 'Créditos complementarios', 'Debe acreditar mínimamente dos (2) créditos de formación complementaria, los cuales puede desarrollarlo mediante talleres: Deportivos, Artísticos, Tutoría par, Responsabilidad social, etc.', 1);
INSERT INTO pregunta (id, titulo, respuesta, CATEGORIAid) VALUES (2, 'Justificación de inasistencias', 'El estudiante podrá justificar inasistencias por razones médicas, fallecimiento de familiares, citación judicial o representación institucional. Debe presentar su solicitud en el campus virtual con documentos sustentatorios, dentro de los 2 días hábiles posteriores a la inasistencia.', 2);
INSERT INTO pregunta (id, titulo, respuesta, CATEGORIAid) VALUES (3, 'Retiro de semestre académico', 'Es voluntario, autorizado por la Dirección de Escuela y no permite retiro parcial. Se solicita por motivos personales, familiares, económicos o de salud. Se debe hacer mediante el campus virtual con documentos sustentatorios.', 3);
INSERT INTO pregunta (id, titulo, respuesta, CATEGORIAid) VALUES (4, 'Retiro definitivo', 'Se solicita a través del módulo virtual. Si es durante el semestre, implica también retiro del semestre. Puede anularse con trámite dentro de 5 días. Si desea continuar estudios en semestres posteriores, tiene hasta 2 años para solicitar reincorporación.', 3);
INSERT INTO pregunta (id, titulo, respuesta, CATEGORIAid) VALUES (5, 'Reserva de matrícula', 'Permite diferir la matrícula por un semestre. Se solicita con sustento a través del campus virtual en fechas definidas. No debe exceder 3 años. Para movilidad académica saliente, se realiza automáticamente.', 4);
INSERT INTO pregunta (id, titulo, respuesta, CATEGORIAid) VALUES (6, 'Reincorporación', 'Solicitada por estudiantes que dejaron de matricularse sin reservar. Se pide a través del campus virtual, está sujeta a vacantes y calendario. No se autoriza si fue separado por razones académicas o disciplinarias.', 4);
INSERT INTO pregunta (id, titulo, respuesta, CATEGORIAid) VALUES (7, 'Cursos de verano', 'Depende de la programación de la Escuela. Debe ser consultado en una base de datos externa o actualizada mediante app web.', 5);
INSERT INTO pregunta (id, titulo, respuesta, CATEGORIAid) VALUES (8, 'Prácticas preprofesionales', 'Se deben completar 260 horas a partir del VIII ciclo, sin cursos pendientes de ciclos anteriores. Se solicita carta de presentación por campus virtual.', 6);
INSERT INTO pregunta (id, titulo, respuesta, CATEGORIAid) VALUES (9, 'Cambio de tema de tesis', 'Se realiza por caso fortuito o fuerza mayor, aprobado por el asesor. Debe presentarse informe y nuevo proyecto. Si se aprueba, se reinicia el proceso según el reglamento de tesis.', 7);
INSERT INTO pregunta (id, titulo, respuesta, CATEGORIAid) VALUES (10, 'Actualización de datos de tesis', 'Si se requiere mejorar redacción de título, objetivos, etc., se debe hacer el trámite virtual para que lo atienda el Docente de Apoyo a Tesis.', 7);
INSERT INTO pregunta (id, titulo, respuesta, CATEGORIAid) VALUES (11, 'Obtención del grado de bachiller', 'Requiere condición de egresado, no tener deudas, pago de trámite, haber llevado curso de investigación y cumplir los requisitos administrativos.', 8);
INSERT INTO pregunta (id, titulo, respuesta, CATEGORIAid) VALUES (12, 'Sustentación de tesis', 'Requiere grado de bachiller, conformidad del asesor, no tener deudas y pago de derecho de sustentación.', 8);
INSERT INTO pregunta (id, titulo, respuesta, CATEGORIAid) VALUES (13, 'Titulación', 'Requiere grado de bachiller, aprobación de tesis ante jurado, no tener deudas, pago por título y cumplimiento de requisitos administrativos.', 8);
INSERT INTO pregunta (id, titulo, respuesta, CATEGORIAid) VALUES (14, 'Idioma inglés', 'Es requisito de egreso. Se debe acreditar nivel intermedio (B1).', 8);
INSERT INTO pregunta (id, titulo, respuesta, CATEGORIAid) VALUES (15, 'Programa de actualización de tesis', 'Dirigido a egresados o bachilleres con tesis desactualizadas. Consta de tres fases: proyecto, ejecución e informe. Cada fase tiene su propio trámite y documentación.', 7);
INSERT INTO pregunta (id, titulo, respuesta, CATEGORIAid) VALUES (16, 'Vigencia del proyecto de tesis aprobado', 'El proyecto tiene vigencia de 3 años desde la aprobación. Puede ampliarse 1 año más como excepción. Luego de ese plazo, pierde validez y se debe presentar uno nuevo.', 7);
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
