import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';
import { Button } from 'react-bootstrap';
import { useState } from 'react';
import { NuevoUsuario } from './usuario/NuevoUsuario.js';
import { ActualizarUsuarios } from './usuario/ActualizarUsuario.js';
import { VerUsuarios } from './usuario/VerUsuarios.js';
import { BorrarUsuarios } from './usuario/BorrarUsuario.js'
import "./Usuarios.css";



export const UsuariosIndice = () => {
    const [contenido, setContenido] = useState(0);

    return (

        <div className="Contenedor">
            <h1>Usuarios</h1>
            <Row>
                <Col>
                    <Button variant="outline-light"onClick={() => setContenido(1)}>Ingresar Usuario</Button>
                </Col>
                <Col>
                    <Button variant="outline-light" onClick={() => setContenido(2)}>Actualizar Usuario</Button>
                </Col>
                <Col>
                    <Button variant="outline-light"onClick={() => setContenido(3)}>Ver Usuarios</Button>
                </Col>
                <Col>
                    <Button variant="outline-light" onClick={() => setContenido(4)}>Eliminar Usuario</Button>
                </Col>
            </Row>
            <div className="Cuerpo">
                {contenido === 1 && <NuevoUsuario />}
                {contenido === 2 && <ActualizarUsuarios />}
                {contenido === 3 && <VerUsuarios />}
                {contenido === 4 && <BorrarUsuarios />}
            </div>  
        </div>


    );
 } 

