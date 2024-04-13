import { Row } from "react-bootstrap";
import { Col } from "react-bootstrap";
import { Button } from "react-bootstrap";
import { Container } from "react-bootstrap";    


export const BorrarUsuarios = () => {
    return (
        <div>   
        <h3>BorrarUsuario</h3>
        <Container>
            <Row>
                <Col>
                <label>id:</label>
                <input type="number"/>
                <Button variant="outline-light">BorrarUsuario</Button>
                </Col>
            </Row>            
        </Container>
        <Container>
            <h3 >Borrar todos los usuarios</h3>
            <Button variant="outline-light">Borrar todos los usuarios</Button>
         
        </Container>
        </div>
    );
}