CREATE TABLE categoria (
  id          int(10) NOT NULL AUTO_INCREMENT, 
  nombre      text NOT NULL, 
  descripcion text, 
  activo      tinyint(1) NOT NULL, 
  PRIMARY KEY (id));
CREATE TABLE pregunta (
  id          int(10) NOT NULL AUTO_INCREMENT, 
  titulo      text NOT NULL, 
  respuesta   text NOT NULL, 
  CATEGORIAid int(10) NOT NULL, 
  PRIMARY KEY (id));
CREATE TABLE palabra_clave (
  id         int(11) NOT NULL AUTO_INCREMENT, 
  palabra    text NOT NULL, 
  PREGUNTAid int(10) NOT NULL, 
  PRIMARY KEY (id));
CREATE TABLE webhook (
  id    int(11) NOT NULL AUTO_INCREMENT, 
  fecha datetime DEFAULT CURRENT_TIMESTAMP NOT NULL, 
  dato  text, 
  PRIMARY KEY (id));
CREATE TABLE estado_usuario (
  numero             varchar(20) NOT NULL, 
  estado             varchar(100) NOT NULL, 
  categoriaid        int(10), 
  ultima_interaccion datetime NOT NULL, 
  PRIMARY KEY (numero));
CREATE TABLE historial (
  id          int(11) NOT NULL AUTO_INCREMENT, 
  mensaje     text NOT NULL, 
  fecha       datetime DEFAULT CURRENT_TIMESTAMP NOT NULL, 
  categoriaid int(10), 
  PRIMARY KEY (id));
CREATE TABLE documento (
  id          int(11) NOT NULL AUTO_INCREMENT, 
  titulo      varchar(150) NOT NULL, 
  descripcion text, 
  url         text NOT NULL, 
  activo      tinyint(1) NOT NULL, 
  preguntaid  int(10), 
  PRIMARY KEY (id));
ALTER TABLE pregunta ADD CONSTRAINT FKpregunta124192 FOREIGN KEY (CATEGORIAid) REFERENCES categoria (id);
ALTER TABLE palabra_clave ADD CONSTRAINT FKpalabra_cl896610 FOREIGN KEY (PREGUNTAid) REFERENCES pregunta (id);
ALTER TABLE estado_usuario ADD CONSTRAINT FKestado_usu784846 FOREIGN KEY (categoriaid) REFERENCES categoria (id);
ALTER TABLE historial ADD CONSTRAINT FKhistorial675424 FOREIGN KEY (categoriaid) REFERENCES categoria (id);
ALTER TABLE documento ADD CONSTRAINT FKdocumento246863 FOREIGN KEY (preguntaid) REFERENCES pregunta (id);

CREATE TABLE usuarios_chat (
  numero            VARCHAR(20) NOT NULL,         
  nombre            VARCHAR(100),                 
  fecha_registro    DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  estado            TINYINT DEFAULT 1,            
  PRIMARY KEY (numero)
);
