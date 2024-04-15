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
    const [Contenido, setContenido] = useState(0);
    const [Usuarios, setUsuarios] = useState([
        { id: 1, nombre: "Juan", apellidoPaterno: "Perez", apellidoMaterno: "Gomez", contrasena: "1234", correo: "ingenieria@gmail.com"},
        { id: 2, nombre: "Maria", apellidoPaterno: "Gonzalez", apellidoMaterno: "Martinez", contrasena: "rosas", correo: "hola@gmail.com"},
        { id: 3, nombre: "Pedro", apellidoPaterno: "Ramirez", apellidoMaterno: "Lopez", contrasena: "zapato", correo: "lol@gmail.com"},
    ]);

    function ActualizarListaUsuarios(nuevaLista){
        setUsuarios(nuevaLista);
    }

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
                {Contenido === 1 && <NuevoUsuario usuarios={Usuarios} funcion={ActualizarListaUsuarios}/>}
                {Contenido === 2 && <ActualizarUsuarios usuarios={Usuarios} funcion={ActualizarListaUsuarios} />}
                {Contenido === 3 && <VerUsuarios usuarios={Usuarios} />}
                {Contenido === 4 && <BorrarUsuarios  usuarios={Usuarios} funcion={ActualizarListaUsuarios}/>}
            </div>  
        </div>


    );
 } 

