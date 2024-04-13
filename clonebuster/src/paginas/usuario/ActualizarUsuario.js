import { Container } from "react-bootstrap"
import { Row } from "react-bootstrap"
import { Col } from "react-bootstrap"
import { Button } from "react-bootstrap"
import { useState } from "react"


export const ActualizarUsuarios = () => {
    const [usuario, setUsuario] = useState(true);
    return (
        <div>   
        <h3>Actualizar Usuario</h3>
        <Container>
            <Row>
                <Col>
                <label>id:</label>
                <input type="number"/>
                <Button variant="outline-light">Buscar</Button>
                </Col>
            </Row>
            {usuario ? <ActualizarUsuario/> : "Usuario no encontrado"};  
            
        </Container>
        </div>
    )
}

const ActualizarUsuario = (prop) => {
    return (
        <div>
            
        <Container>
        <Row >
            <Col>
                <label>Nombre:</label>
            </Col>
            <Col>
                <input type="text"/>
            </Col>
            <Col>
                <label>Apellido Paterno:</label>
            </Col>
            <Col>
                <input type="text"/>
            </Col>
            <Col>
                <label>Apellido Materno:</label>
            </Col>
            <Col>
                <input type="text"/>
            </Col>
        </Row> 
        <Row>
            <Col>Contraseña: <input type="password"></input></Col>
            <Col></Col>
            <Col>Correo: <input type="email"></input></Col>
        </Row>
            <Button variant="outline-light">Guardar</Button>
        </Container>
    </div>
    )
}