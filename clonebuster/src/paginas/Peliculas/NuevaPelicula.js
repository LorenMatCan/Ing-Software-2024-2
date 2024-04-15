import { Col, Container } from "react-bootstrap";
import { Row } from "react-bootstrap";
import { Button } from "react-bootstrap";
import { useState } from "react";

import "bootstrap/dist/css/bootstrap.min.css";

export function NuevoUsuario ({usuarios, funcion})  {
    const [nombre, setNombre] = useState("");
    const [apellidoPaterno, setApellidoPaterno] = useState("");
    const [apellidoMaterno, setApellidoMaterno] = useState("");
    const [correo, setCorreo] = useState("");
    const [contrasena, setContrasena] = useState("");
    const [id, setId] = useState(usuarios.length + 1);

    const handleNombre = (event) => {
        setNombre(event.target.value);
    } 
    
    const handleApellidoPaterno = (event) => {
        setApellidoPaterno(event.target.value);
    }

    const handleApellidoMaterno = (event) => {
        setApellidoMaterno(event.target.value);
    }

    const handleCorreo = (event) => {
        setCorreo(event.target.value);
    }

    const handleContrasena = (event) => {
        setContrasena(event.target.value);
    }

    const addUsuario = () => {
        setId(id + 1);
        const nuevoUsuario = {id: id,  nombre : nombre, apellidoPaterno : apellidoPaterno, apellidoMaterno : apellidoMaterno, correo : correo, contrasena : contrasena, id : id};
        const nuevaLista = [...usuarios, nuevoUsuario];
        funcion(nuevaLista);
    }
    
    return (
        <div>
            
            <h3>Crear un nuevo usuario</h3>
            <Container>
            <Row >
                <Col>
                    <label>Nombre:</label>
                </Col>
                <Col>
                    <input type="text" required onChange={handleNombre}/>
                </Col>
                <Col>
                    <label>Apellido Paterno:</label>
                </Col>
                <Col>
                    <input type="text" required onChange={handleApellidoPaterno}/>
                </Col>
                <Col>
                    <label>Apellido Materno:</label>
                </Col>
                <Col>
                    <input type="text" required onChange={handleApellidoMaterno}/>
                </Col>
            </Row> 
            <Row>
                <Col>Contraseña: <input type="password" required onChange={handleContrasena}></input></Col>
                <Col></Col>
                <Col>Correo: <input type="email" onChange={handleCorreo}></input></Col>
            </Row>
                <Button variant="outline-light" type="submit" onClick={addUsuario}>Guardar</Button>
            </Container>

        </div>
    

    );
}



