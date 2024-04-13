import { Col, Container } from "react-bootstrap";
import { Row } from "react-bootstrap";
import { Button } from "react-bootstrap";

import "bootstrap/dist/css/bootstrap.min.css";

export const NuevoUsuario = () => {
    return (
        <div>
            
            <h3>Crear un nuevo usuario</h3>
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
    

    );
}