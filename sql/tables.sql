CREATE TABLE CATEGORIA (
    id int(10) NOT NULL AUTO_INCREMENT,
    nombre text NOT NULL,
    descripción int(10),
    activo tinyint(1) NOT NULL,
    PRIMARY KEY (id)
);
CREATE TABLE HISTORIAL (
    id int(11) NOT NULL AUTO_INCREMENT,
    mensaje int(11) NOT NULL,
    fecha int(11) NOT NULL,
    respondida tinyint(1) NOT NULL,
    estado char(1) comment 'En caso de no ser respondida la pregunta:
- P: Pendiente de revisión
- R: Revisado',
    PREGUNTAid int(10),
    correo text,
    PRIMARY KEY (id)
);
CREATE TABLE PALABRA_CLAVE (
    id int(11) NOT NULL AUTO_INCREMENT,
    palabra int(11),
    PREGUNTAid int(10) NOT NULL,
    PRIMARY KEY (id)
);
CREATE TABLE PREGUNTA (
    id int(10) NOT NULL AUTO_INCREMENT,
    titulo text NOT NULL,
    respuesta text NOT NULL,
    CATEGORIAid int(10) NOT NULL,
    PRIMARY KEY (id)
);
ALTER TABLE HISTORIAL
ADD CONSTRAINT FKHISTORIAL47465 FOREIGN KEY (PREGUNTAid) REFERENCES PREGUNTA (id);
ALTER TABLE PALABRA_CLAVE
ADD CONSTRAINT FKPALABRA_CL932394 FOREIGN KEY (PREGUNTAid) REFERENCES PREGUNTA (id);
ALTER TABLE PREGUNTA
ADD CONSTRAINT FKPREGUNTA870613 FOREIGN KEY (CATEGORIAid) REFERENCES CATEGORIA (id);
